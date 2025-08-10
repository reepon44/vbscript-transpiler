import ir.nodes
from gen.VBScriptVisitor import VBScriptVisitor
from gen.VBScriptParser import VBScriptParser
from ir.vbscriptMapping import VB_TO_PY_OBJ_MAP, VB_TO_PY_FUNC_MAP

def assign_openfile_bodies(nodes):
    result = []
    i = 0
    while i < len(nodes):
        node = nodes[i]
        # Rekursiv in Kontrollstrukturen aufrufen
        if hasattr(node, "body") and isinstance(node.body, list):
            node.body = assign_openfile_bodies(node.body)
            result.append(node)
            i += 1
            continue
        if isinstance(node, ir.nodes.OpenFile) and node.var_name:
            body = []
            i += 1
            while i < len(nodes):
                n = nodes[i]
                if isinstance(n, ir.nodes.CloseFile) or (isinstance(n, ir.nodes.Assignment) and n.var_name):
                    i += 1
                    continue
                if isinstance(n, ir.nodes.OpenFile):
                    # Rekursiv behandeln
                    sub_nodes = assign_openfile_bodies(nodes[i:])
                    result.append(ir.nodes.OpenFile(var_name=node.var_name, path=node.path, mode=node.mode, body=sub_nodes))
                    return result
                body.append(n)
                i += 1
            result.append(ir.nodes.OpenFile(var_name=node.var_name, path=node.path, mode=node.mode, body=body))
        else:
            result.append(node)
            i += 1
    return result

class VBScriptToIRVisitor(VBScriptVisitor):
    known_arrays = []
    imports = []

    def visitProg(self, ctx: VBScriptParser.ProgContext):
        raw_nodes = []
        for line in ctx.line():
            result = self.visit(line)
            if result:
                if isinstance(result, list):
                    raw_nodes.extend(result)
                else:
                    raw_nodes.append(result)
        # Almost mandatory import for production environment
        #self.imports.append(ir.nodes.Import(path="vb_Translation"))
        final_nodes = self.imports + raw_nodes
        return final_nodes


    def visitLine(self, ctx: VBScriptParser.LineContext):
        stmts = []
        for stmt in ctx.statement():
            if stmt:
                result = self.visit(stmt)
                if result is not None:
                    if isinstance(result, list):
                        stmts.extend(result)
                    else:
                        stmts.append(result)
        return stmts


    def visitStmtAssignment(self, ctx: VBScriptParser.StmtAssignmentContext):
        assign = ctx.assignment()
        var_name = None
        right_func_call = None
        right_proc_call = None
        if assign.assignable().functionCall():
            lhs_func_call = assign.assignable().functionCall()
            func_name = lhs_func_call.IDENTIFIER().getText()
            if func_name.lower() in self.known_arrays:
                #var_name = f"{func_name}[{self.visit(lhs_func_call.argList())}]"
                var_name = ir.nodes.DictionaryAccess(name=func_name, key=lhs_func_call.argList().getText())
            else:
                var_name = func_name
        elif assign.assignable():
            var_name = assign.assignable().getText()
        # rechtsseitig ein functionCall oder procedureCall oder expr
        try:
            if assign.exprWithOp().op.text == '+':
                left = self.visit(assign.exprWithOp().valueExpr(0))
                op = assign.exprWithOp().getText()
                right = self.visit(assign.exprWithOp().valueExpr(1))
                return ir.nodes.Assignment(var_name=var_name, value=ir.nodes.Addition(left=left, right=right))
        except:
            pass
        if assign.exprWithOp().valueExpr(0).functionCall():
            right_func_call = assign.exprWithOp().valueExpr(0).functionCall()
        elif assign.exprWithOp().valueExpr(0).procedureCall():
            right_proc_call = assign.exprWithOp().valueExpr(0).procedureCall()

        if right_func_call:
            if isinstance(right_func_call, list):
                func_name = right_func_call[0].IDENTIFIER().getText().lower()
            else:
                func_name = right_func_call.IDENTIFIER().getText().lower()
            if func_name == "createobject":
                arg = right_func_call.argList().expr(0).getText().strip('"').lower()
                if arg == "scripting.filesystemobject":
                    #return ir.nodes.Assignment(var_name=var_name, value="FileSystemObject()")
                    pass
                elif arg == "scripting.dictionary":
                    self.known_arrays.append(var_name)
                    return ir.nodes.Assignment(var_name=var_name, value="{}")
            elif func_name == "split":
                self.known_arrays.append(var_name)
                return ir.nodes.Assignment(var_name=var_name, value=self.visit(right_func_call))
            else:
                function = self.visit(right_func_call)
                #args = ""
                #if isinstance(right_func_call, list):
                #    for arg in right_func_call[0].argList().expr():
                #        args+= arg.getText()
                #else :
                #    for arg in right_func_call.argList().expr():
                #        args+= arg.getText()
                return ir.nodes.Assignment(var_name=var_name, value=function)

        elif right_proc_call:
            obj_name = right_proc_call.IDENTIFIER(0).getText()
            proc_name = right_proc_call.IDENTIFIER(1).getText().lower()
            if proc_name == "opentextfile":
                path = right_proc_call.argList().expr(0).getText().strip('"')
                if right_proc_call.argList().expr(1):
                    mode = right_proc_call.argList().expr(1).getText()
                else: mode = '1'
                return ir.nodes.OpenFile(var_name=var_name, path=path, mode=mode, body=None)
            elif proc_name == "openastextstream":
                return ir.nodes.OpenFile(var_name=var_name, path=obj_name.strip(), mode='1', body=None)
            else:
                return ir.nodes.Assignment(var_name=var_name, value=f"{obj_name}.{proc_name}")
        else:
            values = []
            for value in assign.exprWithOp().valueExpr():
                values.append(value.getText())
            return ir.nodes.Assignment(var_name=var_name, value=values)
    
    def visitDoUntilLoop(self, ctx: VBScriptParser.DoUntilLoopContext):
        condition = ctx.expr().getText()
        body = []
        for line in ctx.line():
            stmts = self.visit(line)
            if isinstance(stmts, list):
                body.extend(stmts)
            else :
                body.append(stmts)
        if ".atendofstream" in condition.lower():
            return ir.nodes.DoUntilStreamEnd(file=condition.split('.')[0], body=body)
        else:
            return ir.nodes.DoUntilLoop(condition=condition, body=body)
    
    def visitProcedureCall(self, ctx: VBScriptParser.ProcCallContext):
        obj = ctx.IDENTIFIER(0).getText()
        proc = ctx.IDENTIFIER(1).getText()
        module = None
        try:
            module = VB_TO_PY_OBJ_MAP.get((None, proc))
        except:
            pass
        if module and module[0]:
            self.imports.append(ir.nodes.Import(path=module[1]))
        arg = []
        if ctx.argList():
            for args in ctx.argList().expr():
                arg.append(self.visit(args))
        return ir.nodes.Procedure(obj_name=obj, proc_name=proc, arg=arg)

    def visitStmtOther(self, ctx: VBScriptParser.StmtOtherContext):
        expr = ctx.expr().getText()
        if expr.lower().startswith("file.readline"):
            return ir.nodes.PrintStatement("line")
        elif expr.lower() == "file.close":
            return ir.nodes.CloseFile("file")
        elif expr.lower() == "log_start":
            return ir.nodes.FunctionCall(name="log_start", args=None)
        return None
    
    def visitForEachLoop(self, ctx):
        iterable = ctx.expr(1).getText()
        variable = ctx.expr(0).getText()
        body = []
        for line in ctx.line():
            stmts = self.visit(line)
            if isinstance(stmts,list):
                body.extend(stmts)
            else :
                body.append(stmts)
        if ".files" in iterable:
            return ir.nodes.ForEachFile(iterable=iterable, variable=variable, body=body)
        else:
            return ir.nodes.ForEachLoop(iterable=iterable, variable=variable, body=body)
    
    def visitIfMultiLine(self, ctx):
        if ctx.expr():
            condition = ctx.expr().getText()
        elif ctx.comparison():
            condition = self.visit(ctx.comparison())
        if_body = []
        else_body = []
        elif_body = []
        elif_conditions = []
        for line in ctx.thenBlock.line():
            stmts = self.visit(line)
            if isinstance(stmts, list):
                if_body.extend(stmts)
            else :
                if_body.append(stmts)
        if ctx.ELSE():
            for line in ctx.elseBlock.line():
                stmts = self.visit(line)
                if isinstance(stmts, list):
                    else_body.extend(stmts)
                else:
                    else_body.append(stmts)
        elif ctx.elseifBlock():
            for block in ctx.elseifBlock():
                if block.comparison():
                    elif_conditions.append(self.visit(block.comparison()))
                for line in block.block().line():
                    stmts = self.visit(line)
                    if isinstance(stmts, list):
                        elif_body.extend(stmts)
                    else:
                        elif_body.append(stmts)
        return ir.nodes.IfMultiLine(condition=condition, ifBody=if_body, elseBody=else_body, elifBody=elif_body, elifConditions=elif_conditions)

    def visitFunctionCall(self, ctx):
        name = ctx.IDENTIFIER().getText()
        if name in self.known_arrays:
            key = self.visit(ctx.argList())
            return ir.nodes.DictionaryAccess(name=name, key=key)
        try:
            func_map = VB_TO_PY_FUNC_MAP.get(name)
            if func_map["import"]:
                double_imp = False
                for imp in self.imports:
                    if imp.path == func_map["import"]:
                        double_imp = True
                if double_imp == False:
                    self.imports.append(ir.nodes.Import(path=func_map["import"]))
        except:
            pass
        if ctx.argList():
            args = self.visit(ctx.argList())
            return ir.nodes.FunctionCall(name=name, args=args)
        elif ctx.expr() :
            if isinstance(ctx.expr().primaryExpr(), VBScriptParser.ExprConcatContext):
                args = self.visit(ctx.expr().primaryExpr())
                return ir.nodes.FunctionCall(name=name, args=args)
    
    def visitArgList(self, ctx):
        args = []
        for arg in ctx.expr():
            args.append(self.visit(arg))
        return ir.nodes.ListVariable(values=args)
    
    def visitTerminal(self, node):
        return node.getText()
    
    def visitStmtExecuteGlobal(self, ctx: VBScriptParser.ExecuteglobalStmtContext):
        if ctx.executeglobalStmt():
            context = ctx.executeglobalStmt()
            if context.expr().primaryExpr().functionCall().IDENTIFIER().getText().lower() == "createobject":
                if context.expr().chainedCall(0).IDENTIFIER().getText().lower() == "opentextfile":
                    self.imports.append(ir.nodes.Import(context.expr().chainedCall(0).argList().expr(0).primaryExpr().STRING().getText()))
                
    def visitComparison(self, ctx: VBScriptParser.ComparisonContext):
        leftValue = self.visit(ctx.expr(0).primaryExpr())
        rightValue = self.visit(ctx.expr(1).primaryExpr())
        return ir.nodes.Comparison(leftValue=leftValue, rightValue=rightValue)
    
    def visitExprConcat(self, ctx: VBScriptParser.ExprConcatContext):
        Strings = []
        for expr in ctx.primaryExpr():
            if isinstance(expr, (VBScriptParser.ExprConcatContext | VBScriptParser.ExprStringContext | VBScriptParser.ExprIdentContext)):
               Strings.append(self.visit(expr)) 
        return " + ".join(Strings)

    def visitExprString(self, ctx):
        return ctx.getText()
    
    def visitValueExpr(self, ctx):
        if isinstance((ctx, VBScriptParser.STRING | VBScriptParser.IDENTIFIER | VBScriptParser.NUMBER)):
            return ctx.getText()
        else:
           return self.visit(ctx)
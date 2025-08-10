from gen.VBScriptVisitor import VBScriptVisitor
from gen.VBScriptParser import VBScriptParser

class VBScriptToPythonVisitor(VBScriptVisitor):

    #def visitProg(self, ctx: VBScriptParser.ProgContext):
    #    lines = []
    #    for stmt in ctx.statement():
    #        line = self.visit(stmt)
    #        if line is not None:
    #            lines.append(line)
    #    return "\n".join(lines)
    
    def visitProg(self, ctx: VBScriptParser.ProgContext):
        return "\n".join(self.visit(line) for line in ctx.line())
    
    def visitLine(self, ctx: VBScriptParser.LineContext):
        stmts = [self.visit(stmt) for stmt in ctx.statement()]
        stmts = [s for s in stmts if s is not None]
        return " ".join(stmts)

    def visitStmtAssignment(self, ctx: VBScriptParser.StmtAssignmentContext):
        var = ctx.assignment().IDENTIFIER().getText()
        if ctx.assignment().functionCall():
            value = self.visit(ctx.assignment().functionCall())
        else:
            value = self.visit(ctx.assignment().expr())
        return f"{var} = {value}"

    def visitStmtFunctionCall(self, ctx: VBScriptParser.StmtFunctionCallContext):
        return self.visit(ctx.functionCall())

    def visitStmtOther(self, ctx: VBScriptParser.StmtOtherContext):
        return self.visit(ctx.expr())

    def visitFunctionCall(self, ctx: VBScriptParser.FunctionCallContext):
        func_name = ctx.IDENTIFIER().getText()
        if ctx.argList():
            args = self.visit(ctx.argList())
        else:
            args = ""
        return f"{func_name}({args})"

    def visitArgList(self, ctx: VBScriptParser.ArgListContext):
        args = [self.visit(expr) for expr in ctx.expr()]
        return ", ".join(args)
    
    def visitStmtExecuteGlobal(self, ctx: VBScriptParser.StmtExecuteGlobalContext):
        return self.visit(ctx.getChild(0))
    
    def visitExecuteglobalStmt(self, ctx):
        expr_code = self.visit(ctx.expr())
        return f"exec({expr_code})"

    def visitDoUntilLoop(self, ctx: VBScriptParser.StmtDoUntilLoopContext):
        condition = self.visit(ctx.expr())
        body = "\n".join(self.visit(line) for line in ctx.line())
        return f"while not({condition}):\n" + body

    #def visitExpr(self, ctx: VBScriptParser.ExprContext):
    #    if ctx.STRING():
    #        return ctx.STRING().getText()
    #    elif ctx.NUMBER():
    #        return ctx.NUMBER().getText()
    #    elif ctx.IDENTIFIER():
    #        return ctx.IDENTIFIER().getText()
    #    elif ctx.functionCall():
    #        return self.visit(ctx.functionCall())
    #    elif ctx.expr():
    #        return self.visit(ctx.expr())
    #    else:
    #        return "/* unknown expr */"

    def visitExpr(self, ctx: VBScriptParser.ExprContext):
    # Binäre Operatoren mit zwei Unterausdrücken
        if len(ctx.expr()) == 2:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))

            if ctx.PLUS():
                return f"({left} + {right})"
            elif ctx.MINUS():
                return f"({left} - {right})"
            elif ctx.STAR():
                return f"({left} * {right})"
            elif ctx.DIV():
                return f"({left} / {right})"
            elif ctx.AMP():
                return f"str({left}) + str({right})"  # Stringverkettung in Python
            else:
                return f"/* unknown binary op */ {left} ? {right}"

        # Member-Zugriff: expr '.' IDENTIFIER
        elif len(ctx.expr()) == 1 and ctx.IDENTIFIER() and ctx.DOT():
            obj = self.visit(ctx.expr(0))
            attr = ctx.IDENTIFIER().getText()
            return f"{obj}.{attr}"

        # Funktionsaufruf auf Ausdruck: expr '.' functionCall
        elif ctx.functionCall() and len(ctx.expr()) == 1:
            obj = self.visit(ctx.expr(0))
            func = self.visit(ctx.functionCall())
            return f"{obj}.{func}"

        # Eigenständiger Funktionsaufruf
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())

        # Literale
        elif ctx.STRING():
            return ctx.STRING().getText()
        elif ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()

        # Falls nichts erkannt wird
        return "/* unknown expr */"

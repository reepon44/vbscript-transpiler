# Generated from ./grammar/VBScript.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .VBScriptParser import VBScriptParser
else:
    from VBScriptParser import VBScriptParser

# This class defines a complete generic visitor for a parse tree produced by VBScriptParser.

class VBScriptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by VBScriptParser#prog.
    def visitProg(self, ctx:VBScriptParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#line.
    def visitLine(self, ctx:VBScriptParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#stmtIfBlock.
    def visitStmtIfBlock(self, ctx:VBScriptParser.StmtIfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#stmtFunctionCall.
    def visitStmtFunctionCall(self, ctx:VBScriptParser.StmtFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#procCall.
    def visitProcCall(self, ctx:VBScriptParser.ProcCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#stmtAssignment.
    def visitStmtAssignment(self, ctx:VBScriptParser.StmtAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#stmtExecuteGlobal.
    def visitStmtExecuteGlobal(self, ctx:VBScriptParser.StmtExecuteGlobalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#stmtDoUntilLoop.
    def visitStmtDoUntilLoop(self, ctx:VBScriptParser.StmtDoUntilLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#stmtForEachLoop.
    def visitStmtForEachLoop(self, ctx:VBScriptParser.StmtForEachLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#stmtOther.
    def visitStmtOther(self, ctx:VBScriptParser.StmtOtherContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#ifBlock.
    def visitIfBlock(self, ctx:VBScriptParser.IfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#ifMultiLine.
    def visitIfMultiLine(self, ctx:VBScriptParser.IfMultiLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#elseifBlock.
    def visitElseifBlock(self, ctx:VBScriptParser.ElseifBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#ifSingleLine.
    def visitIfSingleLine(self, ctx:VBScriptParser.IfSingleLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#doUntilLoop.
    def visitDoUntilLoop(self, ctx:VBScriptParser.DoUntilLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#forEachLoop.
    def visitForEachLoop(self, ctx:VBScriptParser.ForEachLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#functionCall.
    def visitFunctionCall(self, ctx:VBScriptParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#procedureCall.
    def visitProcedureCall(self, ctx:VBScriptParser.ProcedureCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#argList.
    def visitArgList(self, ctx:VBScriptParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#assignment.
    def visitAssignment(self, ctx:VBScriptParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#assignable.
    def visitAssignable(self, ctx:VBScriptParser.AssignableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#exprWithOp.
    def visitExprWithOp(self, ctx:VBScriptParser.ExprWithOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#comparison.
    def visitComparison(self, ctx:VBScriptParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#concatenation.
    def visitConcatenation(self, ctx:VBScriptParser.ConcatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#exprChained.
    def visitExprChained(self, ctx:VBScriptParser.ExprChainedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#exprFunc.
    def visitExprFunc(self, ctx:VBScriptParser.ExprFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#exprParen.
    def visitExprParen(self, ctx:VBScriptParser.ExprParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#exprSub.
    def visitExprSub(self, ctx:VBScriptParser.ExprSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#exprConcat.
    def visitExprConcat(self, ctx:VBScriptParser.ExprConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#exprProc.
    def visitExprProc(self, ctx:VBScriptParser.ExprProcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#exprAdd.
    def visitExprAdd(self, ctx:VBScriptParser.ExprAddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#exprDiv.
    def visitExprDiv(self, ctx:VBScriptParser.ExprDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#exprString.
    def visitExprString(self, ctx:VBScriptParser.ExprStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#exprIdent.
    def visitExprIdent(self, ctx:VBScriptParser.ExprIdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#exprMult.
    def visitExprMult(self, ctx:VBScriptParser.ExprMultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#exprNumber.
    def visitExprNumber(self, ctx:VBScriptParser.ExprNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#chainedCall.
    def visitChainedCall(self, ctx:VBScriptParser.ChainedCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#valueExpr.
    def visitValueExpr(self, ctx:VBScriptParser.ValueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#executeglobalStmt.
    def visitExecuteglobalStmt(self, ctx:VBScriptParser.ExecuteglobalStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBScriptParser#block.
    def visitBlock(self, ctx:VBScriptParser.BlockContext):
        return self.visitChildren(ctx)



del VBScriptParser
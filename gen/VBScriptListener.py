# Generated from ./grammar/VBScript.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .VBScriptParser import VBScriptParser
else:
    from VBScriptParser import VBScriptParser

# This class defines a complete listener for a parse tree produced by VBScriptParser.
class VBScriptListener(ParseTreeListener):

    # Enter a parse tree produced by VBScriptParser#prog.
    def enterProg(self, ctx:VBScriptParser.ProgContext):
        pass

    # Exit a parse tree produced by VBScriptParser#prog.
    def exitProg(self, ctx:VBScriptParser.ProgContext):
        pass


    # Enter a parse tree produced by VBScriptParser#line.
    def enterLine(self, ctx:VBScriptParser.LineContext):
        pass

    # Exit a parse tree produced by VBScriptParser#line.
    def exitLine(self, ctx:VBScriptParser.LineContext):
        pass


    # Enter a parse tree produced by VBScriptParser#stmtIfBlock.
    def enterStmtIfBlock(self, ctx:VBScriptParser.StmtIfBlockContext):
        pass

    # Exit a parse tree produced by VBScriptParser#stmtIfBlock.
    def exitStmtIfBlock(self, ctx:VBScriptParser.StmtIfBlockContext):
        pass


    # Enter a parse tree produced by VBScriptParser#stmtFunctionCall.
    def enterStmtFunctionCall(self, ctx:VBScriptParser.StmtFunctionCallContext):
        pass

    # Exit a parse tree produced by VBScriptParser#stmtFunctionCall.
    def exitStmtFunctionCall(self, ctx:VBScriptParser.StmtFunctionCallContext):
        pass


    # Enter a parse tree produced by VBScriptParser#procCall.
    def enterProcCall(self, ctx:VBScriptParser.ProcCallContext):
        pass

    # Exit a parse tree produced by VBScriptParser#procCall.
    def exitProcCall(self, ctx:VBScriptParser.ProcCallContext):
        pass


    # Enter a parse tree produced by VBScriptParser#stmtAssignment.
    def enterStmtAssignment(self, ctx:VBScriptParser.StmtAssignmentContext):
        pass

    # Exit a parse tree produced by VBScriptParser#stmtAssignment.
    def exitStmtAssignment(self, ctx:VBScriptParser.StmtAssignmentContext):
        pass


    # Enter a parse tree produced by VBScriptParser#stmtExecuteGlobal.
    def enterStmtExecuteGlobal(self, ctx:VBScriptParser.StmtExecuteGlobalContext):
        pass

    # Exit a parse tree produced by VBScriptParser#stmtExecuteGlobal.
    def exitStmtExecuteGlobal(self, ctx:VBScriptParser.StmtExecuteGlobalContext):
        pass


    # Enter a parse tree produced by VBScriptParser#stmtDoUntilLoop.
    def enterStmtDoUntilLoop(self, ctx:VBScriptParser.StmtDoUntilLoopContext):
        pass

    # Exit a parse tree produced by VBScriptParser#stmtDoUntilLoop.
    def exitStmtDoUntilLoop(self, ctx:VBScriptParser.StmtDoUntilLoopContext):
        pass


    # Enter a parse tree produced by VBScriptParser#stmtForEachLoop.
    def enterStmtForEachLoop(self, ctx:VBScriptParser.StmtForEachLoopContext):
        pass

    # Exit a parse tree produced by VBScriptParser#stmtForEachLoop.
    def exitStmtForEachLoop(self, ctx:VBScriptParser.StmtForEachLoopContext):
        pass


    # Enter a parse tree produced by VBScriptParser#stmtOther.
    def enterStmtOther(self, ctx:VBScriptParser.StmtOtherContext):
        pass

    # Exit a parse tree produced by VBScriptParser#stmtOther.
    def exitStmtOther(self, ctx:VBScriptParser.StmtOtherContext):
        pass


    # Enter a parse tree produced by VBScriptParser#ifBlock.
    def enterIfBlock(self, ctx:VBScriptParser.IfBlockContext):
        pass

    # Exit a parse tree produced by VBScriptParser#ifBlock.
    def exitIfBlock(self, ctx:VBScriptParser.IfBlockContext):
        pass


    # Enter a parse tree produced by VBScriptParser#ifMultiLine.
    def enterIfMultiLine(self, ctx:VBScriptParser.IfMultiLineContext):
        pass

    # Exit a parse tree produced by VBScriptParser#ifMultiLine.
    def exitIfMultiLine(self, ctx:VBScriptParser.IfMultiLineContext):
        pass


    # Enter a parse tree produced by VBScriptParser#elseifBlock.
    def enterElseifBlock(self, ctx:VBScriptParser.ElseifBlockContext):
        pass

    # Exit a parse tree produced by VBScriptParser#elseifBlock.
    def exitElseifBlock(self, ctx:VBScriptParser.ElseifBlockContext):
        pass


    # Enter a parse tree produced by VBScriptParser#ifSingleLine.
    def enterIfSingleLine(self, ctx:VBScriptParser.IfSingleLineContext):
        pass

    # Exit a parse tree produced by VBScriptParser#ifSingleLine.
    def exitIfSingleLine(self, ctx:VBScriptParser.IfSingleLineContext):
        pass


    # Enter a parse tree produced by VBScriptParser#doUntilLoop.
    def enterDoUntilLoop(self, ctx:VBScriptParser.DoUntilLoopContext):
        pass

    # Exit a parse tree produced by VBScriptParser#doUntilLoop.
    def exitDoUntilLoop(self, ctx:VBScriptParser.DoUntilLoopContext):
        pass


    # Enter a parse tree produced by VBScriptParser#forEachLoop.
    def enterForEachLoop(self, ctx:VBScriptParser.ForEachLoopContext):
        pass

    # Exit a parse tree produced by VBScriptParser#forEachLoop.
    def exitForEachLoop(self, ctx:VBScriptParser.ForEachLoopContext):
        pass


    # Enter a parse tree produced by VBScriptParser#functionCall.
    def enterFunctionCall(self, ctx:VBScriptParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by VBScriptParser#functionCall.
    def exitFunctionCall(self, ctx:VBScriptParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by VBScriptParser#procedureCall.
    def enterProcedureCall(self, ctx:VBScriptParser.ProcedureCallContext):
        pass

    # Exit a parse tree produced by VBScriptParser#procedureCall.
    def exitProcedureCall(self, ctx:VBScriptParser.ProcedureCallContext):
        pass


    # Enter a parse tree produced by VBScriptParser#argList.
    def enterArgList(self, ctx:VBScriptParser.ArgListContext):
        pass

    # Exit a parse tree produced by VBScriptParser#argList.
    def exitArgList(self, ctx:VBScriptParser.ArgListContext):
        pass


    # Enter a parse tree produced by VBScriptParser#assignment.
    def enterAssignment(self, ctx:VBScriptParser.AssignmentContext):
        pass

    # Exit a parse tree produced by VBScriptParser#assignment.
    def exitAssignment(self, ctx:VBScriptParser.AssignmentContext):
        pass


    # Enter a parse tree produced by VBScriptParser#assignable.
    def enterAssignable(self, ctx:VBScriptParser.AssignableContext):
        pass

    # Exit a parse tree produced by VBScriptParser#assignable.
    def exitAssignable(self, ctx:VBScriptParser.AssignableContext):
        pass


    # Enter a parse tree produced by VBScriptParser#exprWithOp.
    def enterExprWithOp(self, ctx:VBScriptParser.ExprWithOpContext):
        pass

    # Exit a parse tree produced by VBScriptParser#exprWithOp.
    def exitExprWithOp(self, ctx:VBScriptParser.ExprWithOpContext):
        pass


    # Enter a parse tree produced by VBScriptParser#comparison.
    def enterComparison(self, ctx:VBScriptParser.ComparisonContext):
        pass

    # Exit a parse tree produced by VBScriptParser#comparison.
    def exitComparison(self, ctx:VBScriptParser.ComparisonContext):
        pass


    # Enter a parse tree produced by VBScriptParser#concatenation.
    def enterConcatenation(self, ctx:VBScriptParser.ConcatenationContext):
        pass

    # Exit a parse tree produced by VBScriptParser#concatenation.
    def exitConcatenation(self, ctx:VBScriptParser.ConcatenationContext):
        pass


    # Enter a parse tree produced by VBScriptParser#exprChained.
    def enterExprChained(self, ctx:VBScriptParser.ExprChainedContext):
        pass

    # Exit a parse tree produced by VBScriptParser#exprChained.
    def exitExprChained(self, ctx:VBScriptParser.ExprChainedContext):
        pass


    # Enter a parse tree produced by VBScriptParser#exprFunc.
    def enterExprFunc(self, ctx:VBScriptParser.ExprFuncContext):
        pass

    # Exit a parse tree produced by VBScriptParser#exprFunc.
    def exitExprFunc(self, ctx:VBScriptParser.ExprFuncContext):
        pass


    # Enter a parse tree produced by VBScriptParser#exprParen.
    def enterExprParen(self, ctx:VBScriptParser.ExprParenContext):
        pass

    # Exit a parse tree produced by VBScriptParser#exprParen.
    def exitExprParen(self, ctx:VBScriptParser.ExprParenContext):
        pass


    # Enter a parse tree produced by VBScriptParser#exprSub.
    def enterExprSub(self, ctx:VBScriptParser.ExprSubContext):
        pass

    # Exit a parse tree produced by VBScriptParser#exprSub.
    def exitExprSub(self, ctx:VBScriptParser.ExprSubContext):
        pass


    # Enter a parse tree produced by VBScriptParser#exprConcat.
    def enterExprConcat(self, ctx:VBScriptParser.ExprConcatContext):
        pass

    # Exit a parse tree produced by VBScriptParser#exprConcat.
    def exitExprConcat(self, ctx:VBScriptParser.ExprConcatContext):
        pass


    # Enter a parse tree produced by VBScriptParser#exprProc.
    def enterExprProc(self, ctx:VBScriptParser.ExprProcContext):
        pass

    # Exit a parse tree produced by VBScriptParser#exprProc.
    def exitExprProc(self, ctx:VBScriptParser.ExprProcContext):
        pass


    # Enter a parse tree produced by VBScriptParser#exprAdd.
    def enterExprAdd(self, ctx:VBScriptParser.ExprAddContext):
        pass

    # Exit a parse tree produced by VBScriptParser#exprAdd.
    def exitExprAdd(self, ctx:VBScriptParser.ExprAddContext):
        pass


    # Enter a parse tree produced by VBScriptParser#exprDiv.
    def enterExprDiv(self, ctx:VBScriptParser.ExprDivContext):
        pass

    # Exit a parse tree produced by VBScriptParser#exprDiv.
    def exitExprDiv(self, ctx:VBScriptParser.ExprDivContext):
        pass


    # Enter a parse tree produced by VBScriptParser#exprString.
    def enterExprString(self, ctx:VBScriptParser.ExprStringContext):
        pass

    # Exit a parse tree produced by VBScriptParser#exprString.
    def exitExprString(self, ctx:VBScriptParser.ExprStringContext):
        pass


    # Enter a parse tree produced by VBScriptParser#exprIdent.
    def enterExprIdent(self, ctx:VBScriptParser.ExprIdentContext):
        pass

    # Exit a parse tree produced by VBScriptParser#exprIdent.
    def exitExprIdent(self, ctx:VBScriptParser.ExprIdentContext):
        pass


    # Enter a parse tree produced by VBScriptParser#exprMult.
    def enterExprMult(self, ctx:VBScriptParser.ExprMultContext):
        pass

    # Exit a parse tree produced by VBScriptParser#exprMult.
    def exitExprMult(self, ctx:VBScriptParser.ExprMultContext):
        pass


    # Enter a parse tree produced by VBScriptParser#exprNumber.
    def enterExprNumber(self, ctx:VBScriptParser.ExprNumberContext):
        pass

    # Exit a parse tree produced by VBScriptParser#exprNumber.
    def exitExprNumber(self, ctx:VBScriptParser.ExprNumberContext):
        pass


    # Enter a parse tree produced by VBScriptParser#chainedCall.
    def enterChainedCall(self, ctx:VBScriptParser.ChainedCallContext):
        pass

    # Exit a parse tree produced by VBScriptParser#chainedCall.
    def exitChainedCall(self, ctx:VBScriptParser.ChainedCallContext):
        pass


    # Enter a parse tree produced by VBScriptParser#valueExpr.
    def enterValueExpr(self, ctx:VBScriptParser.ValueExprContext):
        pass

    # Exit a parse tree produced by VBScriptParser#valueExpr.
    def exitValueExpr(self, ctx:VBScriptParser.ValueExprContext):
        pass


    # Enter a parse tree produced by VBScriptParser#executeglobalStmt.
    def enterExecuteglobalStmt(self, ctx:VBScriptParser.ExecuteglobalStmtContext):
        pass

    # Exit a parse tree produced by VBScriptParser#executeglobalStmt.
    def exitExecuteglobalStmt(self, ctx:VBScriptParser.ExecuteglobalStmtContext):
        pass


    # Enter a parse tree produced by VBScriptParser#block.
    def enterBlock(self, ctx:VBScriptParser.BlockContext):
        pass

    # Exit a parse tree produced by VBScriptParser#block.
    def exitBlock(self, ctx:VBScriptParser.BlockContext):
        pass



del VBScriptParser
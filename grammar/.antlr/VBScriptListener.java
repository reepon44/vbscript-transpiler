// Generated from c:/Bachelorarbeit/grammar/VBScript.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link VBScriptParser}.
 */
public interface VBScriptListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link VBScriptParser#script}.
	 * @param ctx the parse tree
	 */
	void enterScript(VBScriptParser.ScriptContext ctx);
	/**
	 * Exit a parse tree produced by {@link VBScriptParser#script}.
	 * @param ctx the parse tree
	 */
	void exitScript(VBScriptParser.ScriptContext ctx);
	/**
	 * Enter a parse tree produced by {@link VBScriptParser#line}.
	 * @param ctx the parse tree
	 */
	void enterLine(VBScriptParser.LineContext ctx);
	/**
	 * Exit a parse tree produced by {@link VBScriptParser#line}.
	 * @param ctx the parse tree
	 */
	void exitLine(VBScriptParser.LineContext ctx);
	/**
	 * Enter a parse tree produced by {@link VBScriptParser#callStmt}.
	 * @param ctx the parse tree
	 */
	void enterCallStmt(VBScriptParser.CallStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link VBScriptParser#callStmt}.
	 * @param ctx the parse tree
	 */
	void exitCallStmt(VBScriptParser.CallStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link VBScriptParser#argList}.
	 * @param ctx the parse tree
	 */
	void enterArgList(VBScriptParser.ArgListContext ctx);
	/**
	 * Exit a parse tree produced by {@link VBScriptParser#argList}.
	 * @param ctx the parse tree
	 */
	void exitArgList(VBScriptParser.ArgListContext ctx);
	/**
	 * Enter a parse tree produced by {@link VBScriptParser#args}.
	 * @param ctx the parse tree
	 */
	void enterArgs(VBScriptParser.ArgsContext ctx);
	/**
	 * Exit a parse tree produced by {@link VBScriptParser#args}.
	 * @param ctx the parse tree
	 */
	void exitArgs(VBScriptParser.ArgsContext ctx);
}
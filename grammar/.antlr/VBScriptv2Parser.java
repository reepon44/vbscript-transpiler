// Generated from c:/Bachelorarbeit/grammar/VBScriptv2.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class VBScriptv2Parser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, ID=24, STRING=25, 
		NUMBER=26, BUILT_IN_FUNCTION=27, WS=28, NEWLINE=29, COMMENT=30;
	public static final int
		RULE_start = 0, RULE_line = 1, RULE_statement = 2, RULE_functionCall = 3, 
		RULE_builtInFunctionCall = 4, RULE_parameters = 5, RULE_expression = 6, 
		RULE_assignment = 7, RULE_ifStatement = 8, RULE_loopStatement = 9, RULE_otherStatements = 10;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "line", "statement", "functionCall", "builtInFunctionCall", 
			"parameters", "expression", "assignment", "ifStatement", "loopStatement", 
			"otherStatements"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "','", "'='", "'If'", "'Then'", "'Else'", "'End If'", 
			"'For'", "'To'", "'Step'", "'Next'", "'While'", "'Wend'", "'Call'", "'Dim'", 
			"'Set'", "'Class'", "'End Class'", "'Function'", "'End Function'", "'Sub'", 
			"'End Sub'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			"ID", "STRING", "NUMBER", "BUILT_IN_FUNCTION", "WS", "NEWLINE", "COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "VBScriptv2.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public VBScriptv2Parser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StartContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(VBScriptv2Parser.EOF, 0); }
		public List<LineContext> line() {
			return getRuleContexts(LineContext.class);
		}
		public LineContext line(int i) {
			return getRuleContext(LineContext.class,i);
		}
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_start);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(25);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 257401376L) != 0)) {
				{
				{
				setState(22);
				line();
				}
				}
				setState(27);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(28);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LineContext extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public BuiltInFunctionCallContext builtInFunctionCall() {
			return getRuleContext(BuiltInFunctionCallContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public LineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_line; }
	}

	public final LineContext line() throws RecognitionException {
		LineContext _localctx = new LineContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_line);
		try {
			setState(35);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(30);
				statement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(31);
				functionCall();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(32);
				builtInFunctionCall();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(33);
				expression();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(34);
				assignment();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
		}
		public LoopStatementContext loopStatement() {
			return getRuleContext(LoopStatementContext.class,0);
		}
		public OtherStatementsContext otherStatements() {
			return getRuleContext(OtherStatementsContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_statement);
		try {
			setState(43);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(37);
				functionCall();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(38);
				expression();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(39);
				assignment();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(40);
				ifStatement();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(41);
				loopStatement();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(42);
				otherStatements();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(VBScriptv2Parser.ID, 0); }
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public BuiltInFunctionCallContext builtInFunctionCall() {
			return getRuleContext(BuiltInFunctionCallContext.class,0);
		}
		public FunctionCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCall; }
	}

	public final FunctionCallContext functionCall() throws RecognitionException {
		FunctionCallContext _localctx = new FunctionCallContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_functionCall);
		int _la;
		try {
			setState(52);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(45);
				match(ID);
				setState(46);
				match(T__0);
				setState(48);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 251658240L) != 0)) {
					{
					setState(47);
					parameters();
					}
				}

				setState(50);
				match(T__1);
				}
				break;
			case BUILT_IN_FUNCTION:
				enterOuterAlt(_localctx, 2);
				{
				setState(51);
				builtInFunctionCall();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BuiltInFunctionCallContext extends ParserRuleContext {
		public TerminalNode BUILT_IN_FUNCTION() { return getToken(VBScriptv2Parser.BUILT_IN_FUNCTION, 0); }
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public BuiltInFunctionCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_builtInFunctionCall; }
	}

	public final BuiltInFunctionCallContext builtInFunctionCall() throws RecognitionException {
		BuiltInFunctionCallContext _localctx = new BuiltInFunctionCallContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_builtInFunctionCall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			match(BUILT_IN_FUNCTION);
			setState(55);
			match(T__0);
			setState(57);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 251658240L) != 0)) {
				{
				setState(56);
				parameters();
				}
			}

			setState(59);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParametersContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public ParametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameters; }
	}

	public final ParametersContext parameters() throws RecognitionException {
		ParametersContext _localctx = new ParametersContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_parameters);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			expression();
			setState(66);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__2) {
				{
				{
				setState(62);
				match(T__2);
				setState(63);
				expression();
				}
				}
				setState(68);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(VBScriptv2Parser.STRING, 0); }
		public TerminalNode NUMBER() { return getToken(VBScriptv2Parser.NUMBER, 0); }
		public TerminalNode ID() { return getToken(VBScriptv2Parser.ID, 0); }
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_expression);
		try {
			setState(73);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(69);
				match(STRING);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(70);
				match(NUMBER);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(71);
				match(ID);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(72);
				functionCall();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(VBScriptv2Parser.ID, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(ID);
			setState(76);
			match(T__3);
			setState(77);
			expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfStatementContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public IfStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStatement; }
	}

	public final IfStatementContext ifStatement() throws RecognitionException {
		IfStatementContext _localctx = new IfStatementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_ifStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(79);
			match(T__4);
			setState(80);
			expression();
			setState(81);
			match(T__5);
			setState(82);
			statement();
			setState(85);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__6) {
				{
				setState(83);
				match(T__6);
				setState(84);
				statement();
				}
			}

			setState(87);
			match(T__7);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LoopStatementContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(VBScriptv2Parser.ID, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public LoopStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_loopStatement; }
	}

	public final LoopStatementContext loopStatement() throws RecognitionException {
		LoopStatementContext _localctx = new LoopStatementContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_loopStatement);
		int _la;
		try {
			setState(107);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__8:
				enterOuterAlt(_localctx, 1);
				{
				setState(89);
				match(T__8);
				setState(90);
				match(ID);
				setState(91);
				match(T__3);
				setState(92);
				expression();
				setState(93);
				match(T__9);
				setState(94);
				expression();
				setState(97);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__10) {
					{
					setState(95);
					match(T__10);
					setState(96);
					expression();
					}
				}

				setState(99);
				statement();
				setState(100);
				match(T__11);
				}
				break;
			case T__12:
				enterOuterAlt(_localctx, 2);
				{
				setState(102);
				match(T__12);
				setState(103);
				expression();
				setState(104);
				statement();
				setState(105);
				match(T__13);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OtherStatementsContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(VBScriptv2Parser.ID); }
		public TerminalNode ID(int i) {
			return getToken(VBScriptv2Parser.ID, i);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public OtherStatementsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_otherStatements; }
	}

	public final OtherStatementsContext otherStatements() throws RecognitionException {
		OtherStatementsContext _localctx = new OtherStatementsContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_otherStatements);
		int _la;
		try {
			setState(149);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__14:
				enterOuterAlt(_localctx, 1);
				{
				setState(109);
				match(T__14);
				setState(110);
				match(ID);
				}
				break;
			case T__15:
				enterOuterAlt(_localctx, 2);
				{
				setState(111);
				match(T__15);
				setState(112);
				match(ID);
				setState(117);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__2) {
					{
					{
					setState(113);
					match(T__2);
					setState(114);
					match(ID);
					}
					}
					setState(119);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case T__16:
				enterOuterAlt(_localctx, 3);
				{
				setState(120);
				match(T__16);
				setState(121);
				match(ID);
				setState(122);
				match(T__3);
				setState(123);
				expression();
				}
				break;
			case T__17:
				enterOuterAlt(_localctx, 4);
				{
				setState(124);
				match(T__17);
				setState(125);
				match(ID);
				setState(126);
				statement();
				setState(127);
				match(T__18);
				}
				break;
			case T__19:
				enterOuterAlt(_localctx, 5);
				{
				setState(129);
				match(T__19);
				setState(130);
				match(ID);
				setState(131);
				match(T__0);
				setState(133);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 251658240L) != 0)) {
					{
					setState(132);
					parameters();
					}
				}

				setState(135);
				match(T__1);
				setState(136);
				statement();
				setState(137);
				match(T__20);
				}
				break;
			case T__21:
				enterOuterAlt(_localctx, 6);
				{
				setState(139);
				match(T__21);
				setState(140);
				match(ID);
				setState(141);
				match(T__0);
				setState(143);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 251658240L) != 0)) {
					{
					setState(142);
					parameters();
					}
				}

				setState(145);
				match(T__1);
				setState(146);
				statement();
				setState(147);
				match(T__22);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u001e\u0098\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0001\u0000\u0005\u0000"+
		"\u0018\b\u0000\n\u0000\f\u0000\u001b\t\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001$\b"+
		"\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0003\u0002,\b\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0003"+
		"\u00031\b\u0003\u0001\u0003\u0001\u0003\u0003\u00035\b\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0003\u0004:\b\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0005\u0005A\b\u0005\n\u0005\f\u0005"+
		"D\t\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006"+
		"J\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\bV\b\b\u0001\b\u0001\b\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0003\tb\b"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0003"+
		"\tl\b\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0005\nt\b\n\n"+
		"\n\f\nw\t\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003\n\u0086\b\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003\n\u0090\b\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0003\n\u0096\b\n\u0001\n\u0000\u0000\u000b"+
		"\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0000\u0000\u00a8"+
		"\u0000\u0019\u0001\u0000\u0000\u0000\u0002#\u0001\u0000\u0000\u0000\u0004"+
		"+\u0001\u0000\u0000\u0000\u00064\u0001\u0000\u0000\u0000\b6\u0001\u0000"+
		"\u0000\u0000\n=\u0001\u0000\u0000\u0000\fI\u0001\u0000\u0000\u0000\u000e"+
		"K\u0001\u0000\u0000\u0000\u0010O\u0001\u0000\u0000\u0000\u0012k\u0001"+
		"\u0000\u0000\u0000\u0014\u0095\u0001\u0000\u0000\u0000\u0016\u0018\u0003"+
		"\u0002\u0001\u0000\u0017\u0016\u0001\u0000\u0000\u0000\u0018\u001b\u0001"+
		"\u0000\u0000\u0000\u0019\u0017\u0001\u0000\u0000\u0000\u0019\u001a\u0001"+
		"\u0000\u0000\u0000\u001a\u001c\u0001\u0000\u0000\u0000\u001b\u0019\u0001"+
		"\u0000\u0000\u0000\u001c\u001d\u0005\u0000\u0000\u0001\u001d\u0001\u0001"+
		"\u0000\u0000\u0000\u001e$\u0003\u0004\u0002\u0000\u001f$\u0003\u0006\u0003"+
		"\u0000 $\u0003\b\u0004\u0000!$\u0003\f\u0006\u0000\"$\u0003\u000e\u0007"+
		"\u0000#\u001e\u0001\u0000\u0000\u0000#\u001f\u0001\u0000\u0000\u0000#"+
		" \u0001\u0000\u0000\u0000#!\u0001\u0000\u0000\u0000#\"\u0001\u0000\u0000"+
		"\u0000$\u0003\u0001\u0000\u0000\u0000%,\u0003\u0006\u0003\u0000&,\u0003"+
		"\f\u0006\u0000\',\u0003\u000e\u0007\u0000(,\u0003\u0010\b\u0000),\u0003"+
		"\u0012\t\u0000*,\u0003\u0014\n\u0000+%\u0001\u0000\u0000\u0000+&\u0001"+
		"\u0000\u0000\u0000+\'\u0001\u0000\u0000\u0000+(\u0001\u0000\u0000\u0000"+
		"+)\u0001\u0000\u0000\u0000+*\u0001\u0000\u0000\u0000,\u0005\u0001\u0000"+
		"\u0000\u0000-.\u0005\u0018\u0000\u0000.0\u0005\u0001\u0000\u0000/1\u0003"+
		"\n\u0005\u00000/\u0001\u0000\u0000\u000001\u0001\u0000\u0000\u000012\u0001"+
		"\u0000\u0000\u000025\u0005\u0002\u0000\u000035\u0003\b\u0004\u00004-\u0001"+
		"\u0000\u0000\u000043\u0001\u0000\u0000\u00005\u0007\u0001\u0000\u0000"+
		"\u000067\u0005\u001b\u0000\u000079\u0005\u0001\u0000\u00008:\u0003\n\u0005"+
		"\u000098\u0001\u0000\u0000\u00009:\u0001\u0000\u0000\u0000:;\u0001\u0000"+
		"\u0000\u0000;<\u0005\u0002\u0000\u0000<\t\u0001\u0000\u0000\u0000=B\u0003"+
		"\f\u0006\u0000>?\u0005\u0003\u0000\u0000?A\u0003\f\u0006\u0000@>\u0001"+
		"\u0000\u0000\u0000AD\u0001\u0000\u0000\u0000B@\u0001\u0000\u0000\u0000"+
		"BC\u0001\u0000\u0000\u0000C\u000b\u0001\u0000\u0000\u0000DB\u0001\u0000"+
		"\u0000\u0000EJ\u0005\u0019\u0000\u0000FJ\u0005\u001a\u0000\u0000GJ\u0005"+
		"\u0018\u0000\u0000HJ\u0003\u0006\u0003\u0000IE\u0001\u0000\u0000\u0000"+
		"IF\u0001\u0000\u0000\u0000IG\u0001\u0000\u0000\u0000IH\u0001\u0000\u0000"+
		"\u0000J\r\u0001\u0000\u0000\u0000KL\u0005\u0018\u0000\u0000LM\u0005\u0004"+
		"\u0000\u0000MN\u0003\f\u0006\u0000N\u000f\u0001\u0000\u0000\u0000OP\u0005"+
		"\u0005\u0000\u0000PQ\u0003\f\u0006\u0000QR\u0005\u0006\u0000\u0000RU\u0003"+
		"\u0004\u0002\u0000ST\u0005\u0007\u0000\u0000TV\u0003\u0004\u0002\u0000"+
		"US\u0001\u0000\u0000\u0000UV\u0001\u0000\u0000\u0000VW\u0001\u0000\u0000"+
		"\u0000WX\u0005\b\u0000\u0000X\u0011\u0001\u0000\u0000\u0000YZ\u0005\t"+
		"\u0000\u0000Z[\u0005\u0018\u0000\u0000[\\\u0005\u0004\u0000\u0000\\]\u0003"+
		"\f\u0006\u0000]^\u0005\n\u0000\u0000^a\u0003\f\u0006\u0000_`\u0005\u000b"+
		"\u0000\u0000`b\u0003\f\u0006\u0000a_\u0001\u0000\u0000\u0000ab\u0001\u0000"+
		"\u0000\u0000bc\u0001\u0000\u0000\u0000cd\u0003\u0004\u0002\u0000de\u0005"+
		"\f\u0000\u0000el\u0001\u0000\u0000\u0000fg\u0005\r\u0000\u0000gh\u0003"+
		"\f\u0006\u0000hi\u0003\u0004\u0002\u0000ij\u0005\u000e\u0000\u0000jl\u0001"+
		"\u0000\u0000\u0000kY\u0001\u0000\u0000\u0000kf\u0001\u0000\u0000\u0000"+
		"l\u0013\u0001\u0000\u0000\u0000mn\u0005\u000f\u0000\u0000n\u0096\u0005"+
		"\u0018\u0000\u0000op\u0005\u0010\u0000\u0000pu\u0005\u0018\u0000\u0000"+
		"qr\u0005\u0003\u0000\u0000rt\u0005\u0018\u0000\u0000sq\u0001\u0000\u0000"+
		"\u0000tw\u0001\u0000\u0000\u0000us\u0001\u0000\u0000\u0000uv\u0001\u0000"+
		"\u0000\u0000v\u0096\u0001\u0000\u0000\u0000wu\u0001\u0000\u0000\u0000"+
		"xy\u0005\u0011\u0000\u0000yz\u0005\u0018\u0000\u0000z{\u0005\u0004\u0000"+
		"\u0000{\u0096\u0003\f\u0006\u0000|}\u0005\u0012\u0000\u0000}~\u0005\u0018"+
		"\u0000\u0000~\u007f\u0003\u0004\u0002\u0000\u007f\u0080\u0005\u0013\u0000"+
		"\u0000\u0080\u0096\u0001\u0000\u0000\u0000\u0081\u0082\u0005\u0014\u0000"+
		"\u0000\u0082\u0083\u0005\u0018\u0000\u0000\u0083\u0085\u0005\u0001\u0000"+
		"\u0000\u0084\u0086\u0003\n\u0005\u0000\u0085\u0084\u0001\u0000\u0000\u0000"+
		"\u0085\u0086\u0001\u0000\u0000\u0000\u0086\u0087\u0001\u0000\u0000\u0000"+
		"\u0087\u0088\u0005\u0002\u0000\u0000\u0088\u0089\u0003\u0004\u0002\u0000"+
		"\u0089\u008a\u0005\u0015\u0000\u0000\u008a\u0096\u0001\u0000\u0000\u0000"+
		"\u008b\u008c\u0005\u0016\u0000\u0000\u008c\u008d\u0005\u0018\u0000\u0000"+
		"\u008d\u008f\u0005\u0001\u0000\u0000\u008e\u0090\u0003\n\u0005\u0000\u008f"+
		"\u008e\u0001\u0000\u0000\u0000\u008f\u0090\u0001\u0000\u0000\u0000\u0090"+
		"\u0091\u0001\u0000\u0000\u0000\u0091\u0092\u0005\u0002\u0000\u0000\u0092"+
		"\u0093\u0003\u0004\u0002\u0000\u0093\u0094\u0005\u0017\u0000\u0000\u0094"+
		"\u0096\u0001\u0000\u0000\u0000\u0095m\u0001\u0000\u0000\u0000\u0095o\u0001"+
		"\u0000\u0000\u0000\u0095x\u0001\u0000\u0000\u0000\u0095|\u0001\u0000\u0000"+
		"\u0000\u0095\u0081\u0001\u0000\u0000\u0000\u0095\u008b\u0001\u0000\u0000"+
		"\u0000\u0096\u0015\u0001\u0000\u0000\u0000\u000f\u0019#+049BIUaku\u0085"+
		"\u008f\u0095";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
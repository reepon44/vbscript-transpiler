grammar VBScript;

prog: line* EOF ;

line
    : (statement (':' statement)*)? NEWLINE 

    ;

statement
    : ifBlock                  # stmtIfBlock
    | functionCall             # stmtFunctionCall
    | procedureCall            # procCall
    | assignment               # stmtAssignment
    | executeglobalStmt        # stmtExecuteGlobal
    | doUntilLoop              # stmtDoUntilLoop
    | forEachLoop              # stmtForEachLoop
    | expr                     # stmtOther
    ;

ifBlock
    :ifMultiLine
    |ifSingleLine
    ;

// ifMultiLine
//     : IF LPAREN? (expr | comparison) RPAREN? THEN NEWLINE
//       thenBlock=block
//       ((ELSEIF | ELSE) (expr | comparison) THEN NEWLINE elseBlock=block)?
//       END IF
//     ;

ifMultiLine
    : IF LPAREN? (expr | comparison) RPAREN? THEN NEWLINE
      thenBlock=block                           // thenBlock
      (elifBlock=elseifBlock)*                  // zero or more elseif branches
      (ELSE NEWLINE elseBlock=block)?           // optional else branch
      END IF
    ;

elseifBlock
    : ELSEIF LPAREN? (expr | comparison) RPAREN? THEN NEWLINE block
    ;

ifSingleLine
    : IF expr THEN statement (ELSE statement)?
    ;

doUntilLoop
    : DO UNTIL expr NEWLINE line* LOOP
    ;

forEachLoop
    : FOR EACH expr IN expr NEWLINE line* NEXT
    ;

functionCall
    : IDENTIFIER '(' argList? ')'
    | IDENTIFIER expr
    ;

procedureCall
    : IDENTIFIER '.' IDENTIFIER (('(' argList? ')') | argList | '.' procedureCall )?
    ;

argList
    : expr (',' expr)*
    ;

assignment
    : SET? lhs=assignable '='rhs=exprWithOp
    ;

assignable
: IDENTIFIER
| functionCall    // z. B. dictionary("key")
;

exprWithOp
    : left=valueExpr
      (op=(PLUS | MINUS | DIV | STAR) right=valueExpr)?
    ;

comparison
    : left=expr EQ right=expr
    | left=expr EQ right=expr
    ;

concatenation
    : primaryExpr AMP primaryExpr (AMP primaryExpr)*
    ;

expr
    : primaryExpr (DOT chainedCall)*     # exprChained
    ;

primaryExpr
    : functionCall  #exprFunc
    | procedureCall #exprProc
    | IDENTIFIER    #exprIdent
    | STRING    #exprString
    | NUMBER    #exprNumber
    | LPAREN expr RPAREN    #exprParen
    | primaryExpr AMP primaryExpr #exprConcat
    | primaryExpr PLUS primaryExpr  #exprAdd
    | primaryExpr MINUS primaryExpr #exprSub
    | primaryExpr STAR primaryExpr  #exprMult
    | primaryExpr DIV primaryExpr   #exprDiv
    ;
    
chainedCall
    : IDENTIFIER (LPAREN argList? RPAREN)?
    ;



//expr
//    : expr AMP expr             
//    | expr PLUS expr            
//    | expr MINUS expr           
//    | expr STAR expr            
//    | expr DIV expr             
//    | STRING
//    | NUMBER
//    | IDENTIFIER
////    | expr '.' IDENTIFIER
////    | expr '.' functionCall
//    | functionCall
//    | procedureCall
//    ;

valueExpr
    : functionCall
    | procedureCall
    | expr
    ;

executeglobalStmt
    : EXECUTEGLOBAL expr
    ;

block
    :line*
    ;

// Lexer

DO
    : [dD][oO]
    ;

UNTIL
    : [uU][nN][tT][iI][lL]
    ;

LOOP
    : [lL][oO][oO][pP]
    ;

SET
    : [sS][eE][tT]
    ;

IF
    : [iI][fF]
    ;

THEN
    : [tT][hH][eE][nN]
    ;

ELSE
    : [eE][lL][sS][eE]
    ;

ELSEIF
    : [eE][lL][sS][eE] [iI][fF]
    ;

ENDIF
    : [eE][nN][dD] [iI][fF]
    ;

END
    : [eE][nN][dD]
    ;

FOR
    : [fF][oO][rR]
    ;

EACH
    : [eE][aA][cC][hH]
    ;

IN
    : [iI][nN]
    ;

NEXT
    : [nN][eE][xX][tT]
    ;

EXECUTEGLOBAL
    : [eE][xX][eE][cC][uU][tT][eE][gG][lL][oO][bB][aA][lL]
    ;

IDENTIFIER
    : [a-zA-Z_] [a-zA-Z_0-9]* 
    ;

NUMBER
    : [0-9]+ ('.' [0-9]+)?
    ;

STRING
    : '"' (~["\r\n])* '"'
    ;

AMP     : '&' ;     
PLUS    : '+' ;     
MINUS   : '-' ;
STAR    : '*' ;
DIV     : '/' ;
EQ      : '=' ;
NEQ     : '<>' ;
LT      : '<' ;
LE      : '<=' ;
GT      : '>' ;
GE      : '>=' ;
LPAREN  : '(' ;
RPAREN  : ')' ;
COMMA   : ',' ;
DOT     : '.' ;
COLON   : ':' ;
SEMI    : ';' ;
NEWLINE : '\r'? '\n' ;

COMMENT
    : '\'' ~[\r\n]* -> skip
    ;

WS
    : [ \t]+ -> skip
    ;

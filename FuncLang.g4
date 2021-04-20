
grammar FuncLang;


statements:
    (statement SEMICOLON )+;

statement:
    simplestmt
    | funcdef
    ;

simplestmt:
    expr
    | assign
    | LCBR simplestmt (SEMICOLON simplestmt)* RCBR
    ;

funcdef:
    ID LPAR (ID ( COMMA ID)*)? RPAR COLON simplestmt;

assign:
    ID (COMMA ID)* EQ expr;

expr:
    comp 
    | conditional;

conditional:
    condition=comp QUESTION ifcase=simplestmt COLON elsecase=simplestmt;

comp:
    right=boolean (op=(LT|LTE|GT|GTE|CEQ) left=boolean)*;

boolean:
    right=sumsub (op=(OR|AND|XOR) sumsub)*
    | NOT sumsub
    | LNOT sumsub;

sumsub:
    right=multdiv (op=(PLUS|MINUS) left=multdiv)*;

multdiv:
    right=exp (op=(MULT|DIV) left=exp)*;

exp:
    right=atom (POW left=atom)?;

atom:
    val=value
    | LPAR ival=simplestmt RPAR
    | ID LPAR (params)? RPAR
    | lval=lst;

params:
    expr (COMMA expr)*
    | DOLLAR listexpr=expr
    ;

lst:
    LBR  (expr ( COMMA expr)*)?  RBR;

value:
    INT
    | STRING
    | ID
    ;


INT:        [0-9]+;
PLUS:       '+';
MINUS:      '-';
MULT:       '*';
DIV:        '/';
LPAR:       '(';
RPAR:       ')';
POW:        '**';
LT:         '<';
LTE:        '<=';
GT:         '>';
GTE:        '>=';
CEQ:        '==';
COMMA:      ',';
ID:         [a-zA-Z][a-zA-Z0-9]*;
DQUOTE:     '"';
QUESTION:   '?';
COLON:      ':';
EQ:         '=';
SEMICOLON:  ';';
OR:         '|';
AND:        '&';
XOR:        '^';
NOT:        '~';
LNOT:       '!';
LBR:        '[';
RBR:        ']';
LCBR:       '{';
RCBR:       '}';
DOLLAR:     '$';
STRING:     DQUOTE ~["\r\n]* DQUOTE;
COMMENT:    '#' ~[\n]* -> skip;
WS:         [ \r\n\t]+ -> skip;

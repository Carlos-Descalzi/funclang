
grammar FuncLang;


statements:
    (statement SEMICOLON )+;

statement:
    expr
    | funcdef
    ;

funcdef:
    ID LPAR (ID ( COMMA ID)*)? RPAR COLON body=expr;

expr:
    comp 
    | conditional;

conditional:
    condition=comp QUESTION ifcase=expr COLON elsecase=expr;

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
    | LPAR ival=expr RPAR
    | ID LPAR (expr ( COMMA expr)*)? RPAR;

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
STRING:     DQUOTE ~["\r\n]* DQUOTE;
WS:         [ \r\n\t]+ -> skip;

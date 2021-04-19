# Generated from FuncLang.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FuncLangParser import FuncLangParser
else:
    from FuncLangParser import FuncLangParser

# This class defines a complete listener for a parse tree produced by FuncLangParser.
class FuncLangListener(ParseTreeListener):

    # Enter a parse tree produced by FuncLangParser#statements.
    def enterStatements(self, ctx:FuncLangParser.StatementsContext):
        pass

    # Exit a parse tree produced by FuncLangParser#statements.
    def exitStatements(self, ctx:FuncLangParser.StatementsContext):
        pass


    # Enter a parse tree produced by FuncLangParser#statement.
    def enterStatement(self, ctx:FuncLangParser.StatementContext):
        pass

    # Exit a parse tree produced by FuncLangParser#statement.
    def exitStatement(self, ctx:FuncLangParser.StatementContext):
        pass


    # Enter a parse tree produced by FuncLangParser#funcdef.
    def enterFuncdef(self, ctx:FuncLangParser.FuncdefContext):
        pass

    # Exit a parse tree produced by FuncLangParser#funcdef.
    def exitFuncdef(self, ctx:FuncLangParser.FuncdefContext):
        pass


    # Enter a parse tree produced by FuncLangParser#expr.
    def enterExpr(self, ctx:FuncLangParser.ExprContext):
        pass

    # Exit a parse tree produced by FuncLangParser#expr.
    def exitExpr(self, ctx:FuncLangParser.ExprContext):
        pass


    # Enter a parse tree produced by FuncLangParser#conditional.
    def enterConditional(self, ctx:FuncLangParser.ConditionalContext):
        pass

    # Exit a parse tree produced by FuncLangParser#conditional.
    def exitConditional(self, ctx:FuncLangParser.ConditionalContext):
        pass


    # Enter a parse tree produced by FuncLangParser#comp.
    def enterComp(self, ctx:FuncLangParser.CompContext):
        pass

    # Exit a parse tree produced by FuncLangParser#comp.
    def exitComp(self, ctx:FuncLangParser.CompContext):
        pass


    # Enter a parse tree produced by FuncLangParser#boolean.
    def enterBoolean(self, ctx:FuncLangParser.BooleanContext):
        pass

    # Exit a parse tree produced by FuncLangParser#boolean.
    def exitBoolean(self, ctx:FuncLangParser.BooleanContext):
        pass


    # Enter a parse tree produced by FuncLangParser#sumsub.
    def enterSumsub(self, ctx:FuncLangParser.SumsubContext):
        pass

    # Exit a parse tree produced by FuncLangParser#sumsub.
    def exitSumsub(self, ctx:FuncLangParser.SumsubContext):
        pass


    # Enter a parse tree produced by FuncLangParser#multdiv.
    def enterMultdiv(self, ctx:FuncLangParser.MultdivContext):
        pass

    # Exit a parse tree produced by FuncLangParser#multdiv.
    def exitMultdiv(self, ctx:FuncLangParser.MultdivContext):
        pass


    # Enter a parse tree produced by FuncLangParser#exp.
    def enterExp(self, ctx:FuncLangParser.ExpContext):
        pass

    # Exit a parse tree produced by FuncLangParser#exp.
    def exitExp(self, ctx:FuncLangParser.ExpContext):
        pass


    # Enter a parse tree produced by FuncLangParser#atom.
    def enterAtom(self, ctx:FuncLangParser.AtomContext):
        pass

    # Exit a parse tree produced by FuncLangParser#atom.
    def exitAtom(self, ctx:FuncLangParser.AtomContext):
        pass


    # Enter a parse tree produced by FuncLangParser#value.
    def enterValue(self, ctx:FuncLangParser.ValueContext):
        pass

    # Exit a parse tree produced by FuncLangParser#value.
    def exitValue(self, ctx:FuncLangParser.ValueContext):
        pass



del FuncLangParser
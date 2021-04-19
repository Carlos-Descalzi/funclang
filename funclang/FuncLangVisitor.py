# Generated from FuncLang.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FuncLangParser import FuncLangParser
else:
    from FuncLangParser import FuncLangParser

# This class defines a complete generic visitor for a parse tree produced by FuncLangParser.

class FuncLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FuncLangParser#statements.
    def visitStatements(self, ctx:FuncLangParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncLangParser#statement.
    def visitStatement(self, ctx:FuncLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncLangParser#funcdef.
    def visitFuncdef(self, ctx:FuncLangParser.FuncdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncLangParser#expr.
    def visitExpr(self, ctx:FuncLangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncLangParser#conditional.
    def visitConditional(self, ctx:FuncLangParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncLangParser#comp.
    def visitComp(self, ctx:FuncLangParser.CompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncLangParser#boolean.
    def visitBoolean(self, ctx:FuncLangParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncLangParser#sumsub.
    def visitSumsub(self, ctx:FuncLangParser.SumsubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncLangParser#multdiv.
    def visitMultdiv(self, ctx:FuncLangParser.MultdivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncLangParser#exp.
    def visitExp(self, ctx:FuncLangParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncLangParser#atom.
    def visitAtom(self, ctx:FuncLangParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncLangParser#value.
    def visitValue(self, ctx:FuncLangParser.ValueContext):
        return self.visitChildren(ctx)



del FuncLangParser
from funclang.FuncLangVisitor import FuncLangVisitor
from funclang.FuncLangLexer import FuncLangLexer
from funclang.FuncLangParser import FuncLangParser
import antlr4
import sys


class BaseFunction:
    def call(self, ctx, param_values):
        return 1


class SplitFunction(BaseFunction):
    def call(self, ctx, param_values):
        p = param_values[0]
        if p:
            return (p[0], p[1:])
        raise Exception("Empty list")


class HeadFunction(BaseFunction):
    def call(self, ctx, param_values):
        p = param_values[0]
        if p:
            return p[0]
        raise Exception("Empty list")


class PrintFunction(BaseFunction):
    def call(self, ctx, param_values):
        print(*param_values)
        return 1


class Function(BaseFunction):
    def __init__(self, parent, name, params, body):
        self._parent = parent
        self._name = name
        self._params = params
        self._body = body

    def call(self, ctx, param_values):
        func_vars = dict(zip(self._params, param_values))
        self._parent.push_ctx(func_vars)
        result = ctx.visit(self._body)
        self._parent.pop_ctx()
        return result


class Visitor(FuncLangVisitor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._context_stack = [{}]
        self._functions = {}
        self._functions["print"] = PrintFunction()
        self._functions["split"] = SplitFunction()
        self._functions["head"] = HeadFunction()

    def push_ctx(self, data):
        self._context_stack.append(data)

    def pop_ctx(self):
        d = self._context_stack.pop()

    def get_vars(self):
        return self._context_stack[-1] if self._context_stack else {}

    def get_var(self, name):
        if len(self._context_stack) > 0:
            value = self._context_stack[-1].get(name)
            if value is not None:
                return value
        raise KeyError(name)

    def set_var(self, name, value):
        if name in self._context_stack[-1]:
            raise Exception("Variable already defined")
        self._context_stack[-1][name] = value

    def visitFuncdef(self, ctx):
        ids = [i.getText() for i in ctx.ID()]
        func_name, params = ids[0], ids[1:]
        self._functions[func_name] = Function(self, func_name, params, ctx.body)
        return self._functions[func_name]

    def visitAssign(self, ctx):
        var_names = ctx.ID()
        var_values = self.visit(ctx.expr())
        if not isinstance(var_values, tuple):
            var_values = (var_values,)

        if len(var_names) != len(var_values):
            raise Exception("Unable to match all variables")

        for k, v in zip(var_names, var_values):
            self.set_var(k.getText(), v)

        return 1

    def visitComp(self, ctx):
        booleans = ctx.boolean()
        right = self.visit(booleans[0])

        for i, left in enumerate(booleans[1:]):
            left = self.visit(left)
            if ctx.LT(i):
                return 1 if right < left else 0
            elif ctx.LTE(i):
                return 1 if right <= left else 0
            elif ctx.GT(i):
                return 1 if right > left else 0
            elif ctx.GTE(i):
                return 1 if right >= left else 0
            else:
                return 1 if right == left else 0
        return right

    def visitBoolean(self, ctx):
        subsums = ctx.sumsub()

        right = self.visit(subsums[0])

        if ctx.NOT():
            return ~right
        elif ctx.LNOT():
            if isinstance(right, int):
                return 0 if right > 0 else 1
            else:
                return 0 if right else 1
        else:
            for i, left in enumerate(subsums[1:]):
                left = self.visit(left)
                if ctx.OR(i):
                    right |= left
                elif ctx.AND(i):
                    right &= left
                elif ctx.XOR(i):
                    right ^= left

        return right

    def visitSumsub(self, ctx):
        multdiv = ctx.multdiv()
        right = self.visit(multdiv[0])

        for i, left in enumerate(multdiv[1:]):
            left = self.visit(left)
            if ctx.PLUS(i):
                right += left
            elif ctx.MINUS(i):
                right -= left

        return right

    def visitConditional(self, ctx):
        condition = self.visit(ctx.condition)

        if condition:
            return self.visit(ctx.ifcase)
        return self.visit(ctx.elsecase)

    def visitMultdiv(self, ctx):
        exp = ctx.exp()
        right = self.visit(exp[0])

        for i, left in enumerate(exp[1:]):
            left = self.visit(left)
            if ctx.MULT(i):
                right *= left
            elif ctx.DIV(i):
                right /= left
        return right

    def visitExp(self, ctx):
        right = self.visit(ctx.right)

        if ctx.POW():
            right **= self.visit(ctx.left)

        return right

    def visitAtom(self, ctx):
        if ctx.val:
            return self.visit(ctx.val)
        elif ctx.ival:
            return self.visit(ctx.ival)
        elif ctx.lval:
            return self.visit(ctx.lval)
        elif ctx.ID():
            func_name = ctx.ID().getText()
            params = self.visit(ctx.params())
            return self._functions[func_name].call(self, params)

    def visitParams(self, ctx):
        if ctx.DOLLAR():
            return self.visit(ctx.listexpr)
        return [self.visit(e) for e in ctx.expr()]

    def visitLst(self, ctx):
        return [self.visit(e) for e in ctx.expr()]

    def visitValue(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]
        elif ctx.ID:
            return self.get_var(ctx.ID().getText())


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py [inputfilename]")
        sys.exit(1)

    input_stream = antlr4.FileStream(sys.argv[1])
    lexer = FuncLangLexer(input_stream)
    tokens = antlr4.CommonTokenStream(lexer)
    parser = FuncLangParser(tokens)
    tree = parser.statements()
    visitor = Visitor()
    visitor.visit(tree)

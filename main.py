from abc import ABC, abstractmethod


class Lisp:
    @abstractmethod
    def eval(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def __repr__(self):
        return str(self)

    def __neg__(self):
        return Neg(self)

    def __add__(self, other):
        return Add(self, other)

    def __sub__(self, other):
        return Sub(self, other)

    def __mul__(self, other):
        return Mul(self, other)

    def __truediv__(self, other):
        return TrueDiv(self, other)

    def __rtruediv__(self, other):
        return RTrueDiv(self, other)

    def __floordiv__(self, other):
        return FloorDiv(self, other)

    def __rfloordiv__(self, other):
        return RFloorDiv(self, other)


class Number(Lisp):
    def __init__(self, value):
        if type(value) != int and type(value) != float:
            raise ValueError("value must be of type Variable")
        self.value = value

    def eval(self):
        return self.value

    def __str__(self):
        return str(self.value)


class Unary(Lisp):
    def __init__(self, a):
        if not isinstance(a, Lisp):
            raise ValueError("a must be a Variable")
        self.a = a

class Neg(Unary):
    def eval(self):
        return -self.a.eval()

    def __str__(self):
        return "(- %s)" % str(self.a)


class Binary(Lisp):
    def __init__(self, a, b):
        if not isinstance(a, Lisp) or not isinstance(b, Lisp):
            raise ValueError("a and b must both be a Variable")
        self.a = a
        self.b = b

class Add(Binary):
    def eval(self):
        return self.a.eval() + self.b.eval()

    def __str__(self):
        return "(+ %s %s)" % (str(self.a), str(self.b))

class Sub(Binary):
    def eval(self):
        return self.a.eval() + self.b.eval()

    def __str__(self):
        return "(- %s %s)" % (str(self.a), str(self.b))

class Mul(Binary):
    def eval(self):
        return self.a.eval() + self.b.eval()

    def __str__(self):
        return "(* %s %s)" % (str(self.a), str(self.b))

class TrueDiv(Binary):
    def eval(self):
        return self.a.eval() / self.b.eval()

    def __str__(self):
        return "(/ %s %s)" % (str(self.a), str(self.b))

class RTrueDiv(Binary):
    def eval(self):
        return self.b.eval() / self.a.eval()

    def __str__(self):
        return "(/ %s %s)" % (str(self.b), str(self.a))

class FloorDiv(Binary):
    def eval(self):
        return self.a.eval() // self.b.eval()

    def __str__(self):
        return "(// %s %s)" % (str(self.a), str(self.b))

class RFloorDiv(Binary):
    def eval(self):
        return self.b.eval() // self.a.eval()

    def __str__(self):
        return "(// %s %s)" % (str(self.b), str(self.a))


class Ternary(Lisp):
    def __init__(self, a, b, c):
        if not isinstance(a, Lisp) or not isinstance(b, Lisp) or not isinstance(c, Lisp):
            raise ValueError("a, b and c must all be an instance of Variable")
        self.a = a
        self.b = b
        self.c = c

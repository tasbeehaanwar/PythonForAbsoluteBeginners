#Dimond Shape Problem

class A:
    def meth(self):
        print("This is method fromm class A")
class B(A):
    def meth(self):
        print("This is method fromm class A")
class C(A):
    def meth(self):
        print("This is method fromm class C")
class D(B,C):
    def meth(self):
        print("This is method fromm class D")

a=A()
b=B()
c=C()
d=D()

# d.meth()
# c.meth()
# d.meth()
c.meth()
d.meth()
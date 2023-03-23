class A:
    def methodA(self):
        print("Ini class A")

class B:
    def methodB(self):
        print("Ini class B")

class C(A,B):
    pass

object = C()

object.methodA()
object.methodB()
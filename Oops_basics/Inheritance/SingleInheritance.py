#single inheritance -> one parent-> one child
class parent:
    def method1(self):
        print("parent method")
class child(parent):
    def method2(self):
        print("child method")

obj = child()
obj.method1()
obj.method2()
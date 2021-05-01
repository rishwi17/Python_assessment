class Parent:
    var = 5


class Child(Parent):
    var = 10

    def foo(self):
        print(super().var)

    def bar(self):
        print(self.var)


obj = Child()
obj.foo()
obj.bar()

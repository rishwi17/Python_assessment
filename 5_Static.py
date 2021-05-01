class MyClass:
    static_member1 = 10
    static_member2 = 'Hello'

    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def func1(self):
        print('{0} {1}'.format(self.static_member1, self.static_member2))

    @staticmethod
    def static_func1(self):
        print('{0} {1}'.format(self.var1, self.var2))

    @staticmethod
    def static_func2(self):
        self.func1()

    def func2(self):
        self.static_func1(self)
        self.static_func2(self)


obj = MyClass(5, 10)

obj.func1()
MyClass.static_func1(obj)
MyClass.static_func2(obj)
obj.func2()

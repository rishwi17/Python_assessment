class ClassA:
    def selfFuncA1(self):
        print('Class A func1')

    def selfFuncA2(self):
        print('Class A func2')

    def overrideFunc(self):
        print('Class A override function')


class ClassB(ClassA):
    def selfFuncB1(self):
        print('Class B func1')

    def selfFuncB2(self):
        print('Class B func2')

    def overrideFunc(self):
        print('Class B override function')

    def parentFunc(self):
        super().overrideFunc()


class ClassC(ClassB):
    def selfFuncC1(self):
        print('Class C func1')

    def selfFuncC2(self):
        print('Class C func2')

    def overrideFunc(self):
        print('Class C override function')

    def parentFunc(self):
        super().overrideFunc()


objA = ClassA()
objB = ClassB()
objC = ClassC()

objA.selfFuncA1()
objA.selfFuncA2()
objA.overrideFunc()

objB.selfFuncB1()
objB.selfFuncB1()
objB.overrideFunc()

objC.selfFuncC1()
objC.selfFuncC2()
objC.parentFunc()

objB.parentFunc()
objC.parentFunc()

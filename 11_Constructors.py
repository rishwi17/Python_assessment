class Something:
    def __init__(self, *args):
        if len(args) == 0:
            self.x = 0

        elif len(args) == 1:
            self.x = args[0]

        elif len(args) == 2:
            self.x = args[0] * args[1]


obj1 = Something()
obj2 = Something('hello')
obj3 = Something(5, 10)

print(obj1.x)
print(obj2.x)
print(obj3.x)

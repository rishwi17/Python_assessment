Name = 'Rishwi Prakash'
print(Name)

# single line Comment

'''
  Multi line Comment '''


class sampleclass:  # class in python
    x = 100


k = sampleclass()
print(k.x)


class circles:  # objects, method
    def __init__(self, radius, area):
        self.radius = radius
        self.area = area


c1 = circles(5, 113.5)
print(c1.radius)
print(c1.area)


x = int(5)

y = float(10)

z = bool(15)

a = str(1)

print(x, y, z, a)


m = 'global variable'


def attachwords():
    m = 'local variable'
    print('This is definitely a ' + m)


attachwords()
print('This is definitely a ' + m)


def whatsyourname():
    print(input('Type your name here: '))


whatsyourname()

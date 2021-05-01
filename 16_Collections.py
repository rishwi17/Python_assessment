list = []

for x in range(10):
    list.append(str(x))

print(list)

list.append('Hello')

i = iter(list)
try:
    while True:
        print(next(i))
except:
    print('End of iteration')

list.insert(3, 'Three')
print(list)

print('Three' in list)
x = list[2]
print(len(list))
list.clear()
print(list)


dict = {
    1: 'Rishwi',
    2: 'Benson',
    3: 'Lohith',
    4: 'Rithesh',
    5: 'Vedant',
    6: 'Laukik',
    7: 'Laurel',
    8: 'Rishab',
    9: 'Yash',
    10: 'Vishwesh'
}

copy_dict = dict.copy()
print(copy_dict)
dict.update({11: 'Anurag'})
print(dict)
print(dict[4])
print(13 in dict.keys())
print('Rithesh' in dict.values())
print(not bool(dict))
print(len(dict))
print(dict.keys())
print(dict.values())
print(dict.pop(11))
print(dict)


s = set()

for x in range(10):
    s.add(str(x))

print(s)
s.add('Rishwi')
print(s)
s.remove('Rishwi')
print(s)

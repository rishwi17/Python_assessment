try:
    print(10 / 0)

except ArithmeticError:
    print('First Except')

except IOError:
    print('Second Except')

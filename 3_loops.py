for _ in range(10):
    print("Bright IT Career")

x = 1
while x <= 20:
    print(x)
    x += 1

numbers = [45, 675, 42, 2, 12, 133, 567, 87, 1, 0]
for i in numbers:
    if(i % 2 == 0):
        print(f"{i} is even")
    else:
        print(f"{i} is odd")


lis = [int(x) for x in input("Enter three numbers: ").split()]
if lis[0] > lis[1]:
    if lis[0] > lis[2]:
        print(f"{lis[0]} is the biggest")
    else:
        print(f"{lis[2]} is the biggest")
elif lis[1] > lis[2]:
    print(f"{lis[1]} is the biggest")
else:
    print(f"{lis[2]} is the biggest")


i = 10
while i <= 100:
    count = i % 2
    if count == 0:
        print(i)
    i += 1


x = int(input('Enter a number: '))
temp = x
n = 0
sumu = 0
# for order
while(x != 0):
    n = n + 1
    x = x // 10

x = temp
# for armstong
while(x != 0):
    rem = x % 10
    x = x // 10
    sumu = sumu + pow(rem, n)

if sumu == temp:
    print(f"{temp} is an armstrong number")
else:
    print(f'{temp} is not an armstrong number')


n = int(input("Enter a number: "))
cnt = 0
for i in range(2, n):
    if n % i == 0:
        cnt = 1
        break
if cnt == 0:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")


x = int(input("Enter a number: "))
temp = x
rev = 0
while(temp != 0):
    rem = temp % 10
    rev = rev * 10 + rem
    temp = temp // 10

if rev == x:
    print("The given number is a palindrome")
else:
    print("The given number is not a palindrome")

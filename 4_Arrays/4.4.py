temp=0
list1=list(map(int,input().split()))
finder=int(input("Enter a number to find:"))
for i in list1:
    if(i==finder):
        temp=i
if(temp!=0):
    print(f"Number found at index= {list1.index(temp)}")
else:
    print("Number not found")
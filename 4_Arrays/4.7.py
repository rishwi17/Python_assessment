list1=list(map(int,input().split()))

new=int(input("Enter the number you wish to add: "))
ind=int(input("Enter the index at which you want to add the number: "))
list1.insert(ind,new)
print(f"New list={list1}")
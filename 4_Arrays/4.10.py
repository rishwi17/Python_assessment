list1=list(map(int,input().split()))
dupe=int(input("Enter value to find duplicates: "))
print(f"Number of times {dupe} repeats is {list1.count(dupe)}")
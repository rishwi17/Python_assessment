list1=list(map(int,input().split()))
list2=list(map(int,input().split()))

print("The common numbers in both the arrays are:")
newlist=[x for x in list1 if x in list2]
print(newlist)

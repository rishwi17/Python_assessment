list1=list(map(int,input().split()))
def checker(num,l):
    count=0
    for i in l:
        if(num==i):
            count+=1
    if count!=0:
        print(f"{num} is present in the array")
    else:
        print(f"{num} is not present in the array")


checker(12,list1)
checker(23,list1)
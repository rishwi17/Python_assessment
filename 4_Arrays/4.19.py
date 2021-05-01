import random

def finder(l):
    ll=0
    ul=100
    while(ll<=ul):
        mid=(ll+ul)//2
        if(l[mid]!=mid+1 and l[mid-1]==mid):
            return mid+1
        elif(l[mid]==mid+1):
            ll=mid+1
        else:
            ul=mid-1


list1=list(range(1,101))
list1.remove(random.randint(1,101))
print(list1)
miss=finder(list1)
print(f"Missing number={miss}")

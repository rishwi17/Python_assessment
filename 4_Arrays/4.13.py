l=list(map(int,input().split()))
newlist=sorted(list(set(l)))[-2]
print(newlist)
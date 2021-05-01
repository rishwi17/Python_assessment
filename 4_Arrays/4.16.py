def answer(li):
    li.sort()
    diff=li[-1]-li[0]
    print(f"Difference={diff}")

l=list(map(int,input().split()))
answer(l)



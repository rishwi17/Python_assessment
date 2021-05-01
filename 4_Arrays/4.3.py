try:
    l=list(map(int,input().split()))
    finder=int(input("Enter number to find Index:"))
    print(f"Index= {l.index(finder)}")
except ValueError:
    print('Number is not found')
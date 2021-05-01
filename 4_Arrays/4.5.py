try:
    list1=list(map(int,input().split()))
    remove=int(input("Enter the number to be removed: "))
    list1.remove(remove)
    print("New array is")
    print(list1)
except ValueError:
    print("Number doesn't exist in the array")
def facn(n):
    re=1
    if n == 1 or n==0:
        return 1
    for i in range(1,n+1):
        re=re*i
    return re
no=int(input("enter the number :"))
print("Factorial is",facn(no))
    
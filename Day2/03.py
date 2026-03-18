list=[]
a=int(input("enter the beginning of the list "))
b=int(input("enter the end of the list "))
c=int(input("enter the steps of the list "))
for i in range(a,b,c):
    list.append(i)
print(list)
list.reverse()
print(list)
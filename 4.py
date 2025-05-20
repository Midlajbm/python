n=int(input("enter the value of row= "))
f=int(input("enter the value of col= "))
print("the table is created")
for i in range(1,n+1,1):
    for j in range(1,f+1,1):
        print(i//j,"* ",end="")
    print("")
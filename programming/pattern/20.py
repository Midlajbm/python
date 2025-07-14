n=5
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if i+j==n+1:
           print("* ",end='')
        else:
            print("  ",end='')
            
    for j in range(1,n+1,1):
        if i-1==j:
           print("* ",end='')
        else:
            print("  ",end='')
    print()
        
n=5
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
         if i==j-1:
           print("* ",end='')
         else:
            print("  ",end='')
    for j in range(1,n+1,1):

       if i+j==n+1-2:
           print("* ",end='')
       else:
            print("  ",end='')
    print()

       
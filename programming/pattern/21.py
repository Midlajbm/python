n=5
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if i==n or j==n or i+j==n+1:
           print("* ",end='')
        else:
            print("  ",end='')
            
    for j in range(1,n+1,1):
        if i==j or i==n or j==1 :
           print("* ",end='')
        else:
            print("  ",end='')
    print()
        
n=5
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
         if i==j or i==1 or j==n:
           print("* ",end='')
         else:
            print("  ",end='')
    for j in range(1,n+1,1):

       if i+j==n+1 or i==1 or j==1:
           print("* ",end='')
       else:
            print("  ",end='')
    print()

       
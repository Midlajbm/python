#for i in range(1,5+1,1):
 #   for j in range(1,5+1,1):
 #       if(i==5 or j==1 or i==j ):
  #         print("* ",end="")
  ##      else:
           #print("  ",end="")
#    print("")


for i in range(1,5+1,1):
    for j in range(1,5+1,1):
        if( i==1 or i==5 or j==1 or j==5
        or j==i  or i+j==5+1):
           print("* ",end="")
        else:
           print("  ",end="")
    print("")
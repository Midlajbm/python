#n=5
#for i in range(1,n+1,1):
 #   for j in range(1,i+1,1):
  #      print("* ",end="")
   # print("")

#n=5
#for i in range(1,n+1,1):
 #   for j in range(1,n-i+1+1,1):
   #     print("* ",end="")
   # print("")

n = 5
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * i)
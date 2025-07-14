def even(num):
    if num%2==0:
        return True
    else:
        return False
    
# L=[1,2,3,4,5]
# i=0
# while i <= 4:
#     data=L[i]
#     choice=even(data)
#     if choice==True:
#         print(L[i])
#     i=i+1

# using filter function
l=[1,2,3,4,5]
res=list(filter(even,l))
print(res)


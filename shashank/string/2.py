#remove duplicate values from string
str=input("enter a sting: ")
print(str)
str1=""
for i in str:
    if i in str1:
        pass
    else:
        str1=str1+i
print(str1)
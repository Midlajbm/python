#reverse the string every letter
str=input("Enter a string: ")
rev=""
for i in str:
    rev=i+rev
print("Reversed string is:", rev)

#reversing word by word
str=input("enter the string:")
str1=str.split()
print(str)
print(str1) 
rev=""
for i in str1:
    rev=i+" "+rev
print("Reversed string is: ", rev)
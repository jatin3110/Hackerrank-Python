# Say "Hello, World!" With Python

print("Hello, World!")

# Python If-Else

N = int(input().strip())
n= N
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and (n>=2 and n<5):
    print("Not Weird")
elif n % 2 == 0 and (n>=6 and n<=20):
    print("Weird")
elif n % 2 == 0 and (n>20):
    print("Not Weird")   

# Arithmetic Operators

a = int(input())
b = int(input())
c = a+b
print(c)
d = a-b 
print (d)
e = a*b
print(e)

# Python: Division

a = int(input())
b = int(input())
# (for integer devision)
print (a//b)  
print (a/b)
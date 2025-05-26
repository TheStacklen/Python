#map_filter
add=lambda a,b:a+b
print(add(78,3))
mul=lambda a,b:a*b
print(mul(12,2))
div=lambda a,b:a/b
print(div(12,2))
remaindar=lambda a,b:a%b
print(remaindar(12,5))
floor=lambda a,b:a//b
print(floor(12,5))
even=lambda x:x%2==0
print(12)
chech=lambda x: "even" if x%2==0 else "odd"
print(chech(13))
def square(n):
    return n**2
list1=[12,10,9,8,7,6,5]
print(list(map(square,list1)))
print(list(map(lambda a:a**2,list1)))
def length(n):
    return len(n)
str1=["saklen","aarif","abdullah","abdulhafiz","danish"]
print(list(map(length,str1)))

str1=["saklen","aarif","abdullah","abdulhafiz","danish"]
print(list(map(lambda a:len(a),str1)))
def discount(n):
    return n-n*10/100
list1=[100,200,300,400,900,700,800,500]
print(list1)
print(list(map(discount,list1)))
print(list(map(lambda a:a-a*10/100,list1)))
list1=[12,11,24,14,15,78,26]
list2=[89,76,89,56,34,90,34]
def add(a,b):
    return a+b
print(list(map(add,list1,list2)))
def add(a,b):
    return a+" "+b
frist_name=["Saklen","Abdullah","Aarif"]
last_name=["Ansari","Ansari","Khan"]
print(list(map(add,frist_name,last_name)))
def check(x):
    if x%2==0:
        return False
    else:
        return True
list1=[12,13,14,15,16,17,18,19]
print(list(filter(check,list1)))
def check(x):
    if x%2==0:
        return True
    else:
        return False
print(list(filter(check,list1)))
print("        ")
print(list(filter(lambda a:a%2==0,list1)))
print(list(filter(lambda a:a%2!=0,list1)))
#reduce
from functools import reduce
list3=[67,89,0,67,56]
print(list3)
print(reduce(lambda A,B:A*B,list3))
def add(a,b):
    return a+b
print(reduce(add,list3))
print(reduce(lambda a,b:a*b,range(1,6)))
factorial=1
for i in range(1,6):
    factorial*=i
print(factorial)
num=int(input("Enter Any Number :"))
f=1
for i in range(1,num+1):
    f*=i
print(f)
    
    
        



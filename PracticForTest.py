#what is python?
'''
python is a widely-used, general purpose high level programming language
released in 1991 by guido van rossum

python is designed to be highly readable and easy to use for biginner
and experts

it is known for its simplicity and varsatility and powerfull libraries
'''
# python basic syntax
#print fanction
##print("Hello World")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>datatype<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
##numeric(integers)(23,53,45,46,57,89,01,24)
##pointing(float)(7.9,78.00,843.8)
##text(string)("76tgvfhjkl.hgg876")
##boolean(True OR False)
##complex(3j)
##collection datatype
##list[]
##tuple()
##set{}
##dict{}
##range()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>string method<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#string method:-length(),indexing,slicing,uppercase,lowercase(),capitalize()
#split(),formate mathod,replace mathod
'''
str1="saklen"
print(str1)
#indexing
print(str1[1])
print(str1.index("a"))
#length
print(len(str1))
#slicing
print(str1[0:len(str1):1])
print(str1[-1:len(str1):-1])
#upper()
print(str1.upper()) #all covert into uppercase
#lower()
print(str1.lower())#all convert into lowercase
#capitalize()
print(str1.capitalize()) #conver into first latter uppercase
#split()-separate
print(str1.split("a"))

#count()
print(str1.count("a"))
#format method
num=10
print(f"this is your number {num}")
#replace method
print(str1.replace("k","q"))
'''
#type converssion
'''
num=10
print(num,type(num))
f_num=float(num)
print(f_num,type(f_num))
floatt=20.0
print(floatt,type(floatt))
int_num=int(floatt)
print(int_num)
name="2131"
print(float(name))
print(int(name))
num=98765
print(float(num))
print(str(num))
'''
'''
#inpute function
num1=int(input("Enter The First Number: "))
num2=int(input("Enter The Second Number: "))
print(num1*num2)
'''

##datatypes (numeric(integer),pointing(float),complex,textty(string),)
#numeric types: int(integers)
'''
num1=90
print(num1,type(num1))
#float (floating-point number)
float1=90.6
print(float1,type(float1))
#complex
complex1=3j
print(complex1,type(complex1))
#Text type: str(string of characters)
str1="this is string"
print(str1,type(str1))
'''
#sequance/coloction type (list[](mutable),tuple()(immable),set{}
#dictionary{},range(sequential numbers),mapping type:-dictionary()
#key-vaue pairs,boolean type(True or False))
#list (mutable)
'''
list1=[90,10.5,"saklen",True,False]
print(list1,type(list1))
#tuple ()
tup1=("python",90,90.5,True)
print(tup1,type(tup1))
#set
set1=(90,10.5,"saklen",True,False)
print(set1,type(set1))
#range (sequential numbers)
r=range(1,50)
print(r,type(r))
#Mapping type:dict (key-value pairs)
dict1={"Name1":"Ali","Name2":"Sadaf","Name3":"Falak"}
print(dict1,type(dict1))
print(dict1["Name2"])
#Add Name
dict1["Name4"]="saqib"
print(dict1)
#Change Name
dict1["Name3"]="saqib"
print(dict1)
#boolean type: bool (True/False)
bool1=True
bool2=False
print(bool1)
print(bool2)
print(type(bool1),type(bool2))
'''

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>String<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
'''
str1="falak"
#length :- the len function return the number of element
print(len(str1))
#indexing :- indexing start from 0
print(str1[1])
print(str1.index("a"))
#nagative indexing :- start from -1
print(str1[-1])
#sllicing :-slicing is used to obtain a portion of a sequence
print(str1[1:len(str1):1])
print(str1[-1::-1])
#comman string method
#capitalize,uppercase,lowercase
print(str1.capitalize())
print(str1.upper())
print(str1.lower())
'''
#Question.txt from class room
'''
#Qs1
my_str="World"
print(my_str[-2])
print(my_str[3])
#Qs2
str1="PythonProgramming"
print(str1[0:6:1])
#Qs3
str1="Complete"
print(str1[-1:3:-1])
#Qs4
a="Hello"
b="World"
print(a+" "+b)
#qs5
num=14
result=num%7==0
print(result)
#Qs6
a=17
b=4
division=17/4
print(division)
floor=a//b
print(floor)
remainder=a%b
print(remainder)
'''
#python operators
#operators are used to perform operations on variable and value.
#arithmatic operator :-(addition(+),Subtraction(-),Multiplication(*),Division(/),
#FloorDivision(//),modulus(%))
#Addition
'''
num1=20
num2=3
str1="Saklen"
str2="Ansari"
print(num1+num2)
print(str1+" "+str2)
#Subtraction
print(num1-num2)
#Multiplication
print(num1*num2)
#Division
print(num1/num2)#return the exact quotient
#FloorDivision
print(num1//num2)
#modulus
print(num1%num2)
'''
#Comparision Operators
#used to compare values.
'''
> Greater than
 < Less than
 == Equal to
 >= Greater than or equal to
 <= Less than or equal to
 != Not equal to
'''
'''
num1=12
print(num1>11)
print(num1<11)
print(num1==12)
print(num1>=13)
print(num1<=13)
print(num1!=13)
'''
#Assignment Operators :- used to assign values to variable
'''
 =  `   Assigns the value
 +=     x += 3 (Equivalent to x = x + 3)
 -=     x -= 3 (Equivalent to x = x - 3)
 *=     x *= 3 (Equivalent to x = x * 3)
 /=     x /= 3 (Equivalent to x = x / 3)
 '''
'''
num1=50
num1+=90
print(num1)
num1-=23
print(num1)
num1*=2
print(num1)
num1/=2
print(num1)
'''
#Logical Operators :- Logical operator are used to combine conditional
#statements
#And:-returns True if both are statements True
#or :- returns True if at least one statement is True
#not :-reverses the result (True become false, and vise versa)
'''
num=4
div_by2=num%2==0
print(div_by2)
div_by3=num%3==0
print(div_by3)
print("and ",div_by2 and div_by3)
print("or ",div_by2 or div_by3)
print("not ", not(div_by3))
'''
'''
str1="Python Programming"
#use replace method
rep_str=str1.replace("P","s")
print(rep_str)
print(rep_str)
print(str1.replace("P","k"))
#split method
split_str=str1.split(" ")
print(split_str)
#MaxSplit
str4="Hello World Good Afternoon Everyone"
max_split=str4.split("o",maxsplit=2)
print(max_split)
'''
'''
#Qs1 from class room (if else)
#WAP to check whether user is eligible to vote or not
age=int(input("Enter Your Age :"))
if age<=0:
    print("please enter the valid age")
elif age>=18:
    print("Eligible for vote")
elif age<18:
    print("Not Eligible for vote")
else:
    print("enter valid age")
'''
#Qs2
#WAP to print whether a number is
##divisible by 2 or divisible by 3 or divisible by both
'''
num=int(input("Enter Any Number :"))
if num%2==0 and num%3==0:
    print("divisible by both")
elif num%2==0:
    print("divisible by 2")
elif num%3==0:
    print("divisible by 3")
else:
    print("not divisible by 2 or 3")
    '''
#Q3
##WAP to print "Positive", "Negative", or "Zero" based on a number's value.
'''
try:
    user=int(input("Enter Any Number:"))
    if user>0:
        print("positive")
    elif user<0:
        print("negative")
    elif user==0:
        print("zero")
    else:
        print("error")
except:
    print("enter the number not string")
    '''
#Q4  
##WAP to  print which among the any three given numbers (num1, num2, num3)
#is the greatest.
'''
num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
num3=int(input("enter the third number: "))
if num1>num2 and num1>num3:
    print(f"{num1} is greatest {num2} and {num3}")
elif num2>num1 and num2>num3:
    print(f"{num2} is greatest {num1} and {num3}")
elif num3>num1 and num3>num2:
    print(f"{num3} is greatest {num1} and {num2}")
   '''
#Q5
##WAP to determine if a triangle is equilateral, isosceles, or scalene based
#on its side lengths.
'''
Scalene Triangle: All three sides are of different lengths.
Isosceles Triangle: Any of Two sides are equal length, and the third side is
different.
Equilateral Triangle: All three sides are of equal length. 
'''
'''
s1=int(input("enter the first side :"))
s2=int(input("enter the second side :"))
s3=int(input("enter the third side :"))
if s1!=s2 and s2!=s3:
    print("scalene triangle")
elif (s1==s2 and s2!=s3) or (s2==s3 and s1!=s2) or (s3==s1 and s3!=s1):
    print("Isosceles Triangle")
elif s1==s2 and s2==s3:
    print("Equilateral Triangle")
'''

#list:- list is a collection of items
'''
l1=[90,"python",True,False,90.5]
print(l1)
#indexing
print(l1[1])
print(l1.index("python"))
print(len(l1))
#slicing
print("   ")
print(l1[1:len(l1):1])
print(l1)
#insert
l1.insert(5,"ali")
print(l1)
#append
l1.append(1000)
print(l1)
#remove
l1.remove("ali")
print(l1)
#pop
pop=l1.pop(3)
print(pop)
print(l1)
l1.clear()
print(l1)
l2=[90,"python",True,False,90.5]
print(l2)
##del(l2)
print(l2)
l2=[90,"python",True,False,90.5]
l2.extend((89,90,"falak"))
print(l2)
#adding two list
add=l2+l2
print(add)
list1=[12,11,35,9,3,5,2,90,1,4,45]
#reverse()
print("   ")
print(list1)
print(list1[-1::-1])
list1.reverse()
print(list1)
print("  ")
#sort()
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
sorted_list=sorted(list1)
print(sorted_list)
sorted_list=sorted(list1,reverse=True)
print(sorted_list)
#tuple
t1=(90,"python",True,False,90.5,90,90)
print(t1)
print(t1.index("python"))
print(t1[3])
print(t1.count(90))
#add two tuple
t1=(90,"python",True,False,90.5,90,90)
t2=(90,"python",True,False,90.5)
print(t1+t2)
#set
s1={90,"python",True,False,90.5,90,90}
print(s1)
s1.add(4)
print(s1)
set1={1,2,4,5,10,12}
set2={4,2,1,9,2}
print(set1.union(set2))
print(set1.intersection(set2))
'''
#Dictionary
'''
dict1={"name":"abdullah","age":20,"department":"parmacy"}
print(dict1)
print(dict1["name"])
#keys()
print(dict1.keys())
#values()
print(dict1.values())
#change
dict1["name"]="nadeem"
print(dict1)
#add key value
dict1["enrollment"]=876543
print(dict1)
print("department" in dict1)
print("branch" in dict1)
#pop
age=dict1.pop("age")
print(age)
print(dict1)
#items()
a=list(dict1.items())
print("   ")
print(a[0])
b=list(dict1.items())
print(b[1])
#enumerate function
list1=["saklen","abdullah","aarif","abdulhafiz"]
print(list(enumerate(list1)))
print(tuple(enumerate(list1)))
#zip
list2=["ansari","khan","saifi","khan"]
print(list(zip(list1,list2)))
list3=[1,2,3,4,5]
print(list(zip(list1,list2,list3)))
'''
#practic
'''
a="Hello World"
print(a.replace("l","m"))
print("{}".format(a))
#list (mutable)
l1=[12,13,14,15,16]
print(l1)
#change element
l1[1]=90
print(l1)
#add element
l1.insert(3,99)
print(l1)
l1.append(100)
print(l1)
#remove element
l1.remove(99)
print(l1)
pop=l1.pop()
print(l1)
print(pop)
in_pop=l1.pop(0)
print(l1)
print(in_pop)
print(l1)
##del(l1)
##print(l1)
l4=["python","programming","language","ali"]
print("saad".join(l4))
'''
#assingment
##
##1. Write a program to print the division of the cubes of two user inputted
##numbers. (1 mark)
'''
user1=int(input("enter the first number :"))
user2=int(input("enter the second number:"))
cube1=user1**3
cube2=user2**3
division_cube=cube1/cube2
print(division_cube)
'''
##
##2.Given a list: [100,200,300,400,500] , extract [400,300,200] from the given
##list using slicing. (1 mark)
'''
list1=[100,200,300,400,500]
print(list1[-2:-5:-1])
'''
##
##3.Given a list : grades = [85, 90, 78, 92, 88] , change element  78 to 87
##in the list and print the index of element 92.      (1 mark)
'''
grades = [85, 90, 78, 92, 88]
grades[2]=87
print(grades)
print(grades.index(92))
'''
##
##4. Write a program to sort a given list in descending  order and then find
##the sum of all its elements.
##NumList = [23, 56, 1, 33, 90, 17, 29, 77, 43, 18, 6] . (1 mark)
'''
NumList=[23, 56, 1, 33, 90, 17, 29, 77, 43, 18, 6]
NumList.sort(reverse=True)
print(NumList)
print(len(NumList))
sum_of=0
for i in NumList:
    sum_of+=i
print(sum_of)
'''    
##
##5. Write a program to check whether a user inputted number is even or odd.
##if input is 12: print output as "12 is even number" (2 marks)
'''
num1=int(input("Enter The Any Number :"))
if num1%2==0:
    print(f"{num1} is even number")
else:
    print(f"{num1} is odd number")
'''
##
##6.Given : fruits = ["apple", "banana", "cherry"] , add "orange" at the end
##of the list and add "grape" at 4th index.  (2 marks)
'''
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.insert(4,"grape")
print(fruits)
'''
##
##7. Given a paragraph:
##"The concept of fitness encompasses both physical and mental health.Achieving
##fitness is essential for leading a fulfilling life. Key principles of
##maintaining fitness include regular exercise a balanced diet proper hydration
##and sufficient sleep."
##Find the index of the word 'fitness' and print the sentence: "fitness include
##regular exercise a balanced diet proper hydration" . ( 2 marks)

##s='''The concept of fitness encompasses both physical and mental health.Achieving
##fitness is essential for leading a fulfilling life. Key principles of
##maintaining fitness include regular exercise a balanced diet proper hydration
##and sufficient sleep.'''
##print(s.index("fitness"))
##print(s[159])
##print(s.index("sleep"))
##print(s[159:246:1])
##
##8.Given list of animals: animals = ["dog", "cat", "rabbit", "hamster",
##                                    "parrot"].Remove the animal "cat"
##from the list, then pop the last animal and store it in a variable. Then,
##clear all remaining animals from the list. Print the list after each
##operation, including the popped animal (element). (2 marks)
'''
animals = ["dog", "cat", "rabbit", "hamster","parrot"]
animals.remove("cat")
print(animals)
p_element=animals.pop()
print(animals)
animals.clear()
print(animals)
'''
##9. Given the string text = "apple, banana, cherry, date", change "banana"
##with "orange,"  and then split the string into a list of fruits and reverse
##that list.(2 marks)
'''
str1="apple, banana, cherry, date"
print(str1.replace("banana","orange"))
sp=str1.split(" ")
print(sp)
sp.reverse()
print(sp)
'''
##10. Write a Python program that takes a user’s age as input and determines
##their life stage based on the following criteria:
##
##If the age is less than 13, print "You are a child."
##If the age is between 13 and 19 , print "You are a teenager."
##If the age is between 20 and 64 , print "You are an adult."
##If the age is 65 or older, print "You are a senior."      ( 3 marks)
'''
age=int(input("Enter Your Age :"))
if age<=0:
    print("please enter the valid age")
elif age<13:
    print("you are child")
elif age>=13 and age<=19:
    print("you are a teenager")
elif age>=20 and age<=64:
    print("you are adult")
elif age>=65:
    print("you are senior")
else:
    print("enter the valid age")
'''
##11. Write a program to create a calculator that performs four mathematical
##operations on two numbers. Both the numbers and the operator must be a valid
##user input. Print a message along with the result using formatted string or
##returns a message of invalid operator otherwise. Operations to be performed
##- Subtraction, Multiplication, Addition and Floor. (3 marks)
'''
num1=int(input("enter the first number :"))
operator=input("enter the operator for operation :")
num2=int(input("enter the second number :"))
if (operator=="+" or operator=="-" or operator=="*" or operator=="//"):
    if operator=="+":
        print(f"addition of {num1} and {num2} is ",num1+num2)
    elif operator=="-":
        print(f"subtraction of {num1} and {num2} is ",num1-num2)
    elif operator=="*":
        print(f"multiplication of {num1} and {num2} is ",num1*num2)
    elif operator=="//":
        print(f"FloorDivision of {num1} and {num2} is ",num1//num2)
else:
    print("invalid operator")
'''

#practic2
#list method
'''
dict1={"a":10,"b":20,"c":30,"d":40}
print(dict1.keys())
print(dict1.values())
##print((dict1.values())[1])
dict2={"name":"abdullah","age":20,"department":"parmacy","semester":1,"cgpa":8}
print(dict2)
dict2["department"]="IT"
print(dict2)
dict2["subject"]=["dsa","m3"]
print(dict2)
dict2["subject"].append("python")
print(dict2)
dict2["subject"][2]="java"
print(dict2)
print(dict2.items())
list1=["saklen","abdullah","aarif","abdulhafiz"]
print(list(enumerate(list1)))
list2=[10,20,30,40,50]
print(list(zip(list2,list1)))
'''
#ForLoop
'''
range() return a sequence of numbers
syntax:range(start,stop,step)
default start is 0,step is 1
Negetive step for reverse order
'''
'''
#list, tuple,set,dictionary
print(list(range(1,100)))
print(tuple(range(1,100)))
print(set(range(1,100)))
print(list(range(100,0,-1)))
#1-50 even numbers
print(list(range(2,51,2)))
#WAP to print 0-50
print(list(range(51)))
for i in range(10):
    print(i,"hello")
for i in range(50):
    if i%2==0:
        print(i)
#Qs1
even_num=[]
odd_num=[]
for i in range(50):
    if i%2==0:
        even_num.append(i)
    else:
        odd_num.append(i)
print("even numbers :",even_num)
print("odd numbeers :",odd_num)

##import copy
##list1=123
##copy_list=copy.copy(list1)
##copy_list.revese()
##print(copy_list)
##print(reverse_list)
##num=1234
##reverse_num=int(str(num)[-1::-1])
##print(reverse_num)
#Qs3
list1=["saklen",78,90,"abdullah",67,"ali","saqib",90.5]
strings=[]
integers=[]
for i in list1:
    if type(i)==int:
        integers.append(i)
    elif type(i)==str:
        strings.append(i)
print(integers)
print(strings)
#Qs4
list1=[12,13,14,15,16,17,18,11,20,21]
multiple_of3=[]
non_multiple_of3=[]
for i in list1:
    if i%3==0:
        multiple_of3.append(i)
    else:
        non_multiple_of3.append(i)
print("multiple of 3 :",multiple_of3)
print("non multiple of 3 :",non_multiple_of3)
#Qs5
list1=["saklen","abdullah","ali","saqib","falak","aarif"]
even_length=[]
odd_length=[]
for i in list1:
    if len(i)%2==0:
        even_length.append(i)
    else:
        odd_length.append(i)
print("even",even_length)
print("odd",odd_length)

#ForLoop
for i in "Hello World":
    print(i)

str1=input("Enter any word :")
for i in str1:
    if i in["a","e","i","o","u","A","E","I","O","U"]:
        print(i)

factorial=1
for i in range(1,6):
    factorial*=i
print(factorial)
Sum=0
for i in range(1,11):
    Sum+=i
print(Sum)
sum_of=0
list1=[12,10,13,25,13,7,20,4,6]
for i in list1:
    sum_of+=i
print(sum_of)
#For loop
for i in range(6):
    print(i)
else:
    print("loop terminated")

for i in range(1,50):
    print(i)
    if i==20:
        break
else:
    print("loop is terminated")
for i in range(1,50):
    if i%2==0:
        continue
    print(i)
else:
    print("loop is terminated")
num=14
for i in range(2,num):
    if num%i==0:
        print("not prime")
        break
else:
    print("prime")
    
list1=[12,13,14,15,16,17,18,19,20,21,22,23]
prime=[]
for i in list1:
    for a in range(2,i):
        if i%a==0:
            break
    else:
        prime.append(i)
print(prime)

def primes(a,b):
    primes_no=0
    for i in range(a,b):
        for a in range(2,i):
            if i%a==0:
                break
        else:
            primes_no+=1
    return primes_no
print(primes(10,30))
for i in range(1,11):
    print(2*i)
name=input("enter your name :")
COUNT_OF=0
for i in name:
    if i in ["a","e","i","o","u","A","E","O","I","U"]:
        COUNT_OF+=1
print(COUNT_OF)
#loop3
num=143
s=0
for i in range(len(str(num))):
    mod=num%10
    s+=mod
    num//=num
print(s)

dict1={"num1":12,"num2":34}
print(dict1["num1"])
dict1["num3"]=90
print(dict1)
for i,e in dict1.items():
    print(i)
    print(e)

list1=["saklen",67,90.5,True]
for i in range(0,len(list1)):
    print(i,list1[i])

list1=[789,798,675,765]
dict1={}
print(dict(enumerate(list1)))
for i,e in enumerate(list1):
    dict1[i]=e
print(dict1)

len_of=[]
list1=["abdullah","aarif","saklen","ali"]
for i in list1:
    len_of.append(len(i))
print(len_of)
print(list(zip(list1,len_of)))
len_of={i:len(i) for i in list1}
print(len_of)
list1=[2,4,6,8,10]
square={i:i**2 for i in list1}
print(square)
new_list=[]
l2=["Samit","Kane","Joe"]
for i in l2:
    new_list.append(i[0])
print(new_list)

list1=[2,4,6,8,10]
dict1={}
for i in list1:
    dict1[i]=i**2
print(dict1)
l1=["abdullah","saklen","aarif","salman"]
l2=[]
for i in l1:
    l2.append(i[0])
print(l2)

d1={"apple":13,"banana":15,"charry":45}
d2={}
for k,v in d1.items():
    d2[v]=k
print(d2)
s=0
for i in d1.values():
    s+=i
print(s)
list1=["abdullah","aarif","saklen","ali"]
e_i=[]
for i,e in enumerate(list1):
    if i%2==0:
    
        e_i.append(i)
print(e_i)

dic={"num1":20,"num2":90,"num3":40,"num4":30}
print({k:v for k,v in dic.items() if v>30})

def s(a,b):
    return a+b
print(s(78,2))
def check(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
print(check(25))
def Sum(num):
    sum_of=0
    for u in range(1,num+1):
        sum_of+=u
    return sum_of
print(Sum(5))
m=100
list1=[90,67,56,54,23,41,100]
for i in list1:
    if m>i:
        m=i
print(m)

l1=[78,97,45,43,44]
l2=[12,78,45,44,90]
for i in l1:
    if i in l2:
        print(i)
    


import random
print(random.randrange(1,10))
numbers=[]
for i in range(20):
    numbers.append((random.randint(1,90)))
print(len(numbers))
num="kjhgfhfjk"
print(random.choice(num))
print(random.choices(num,k=3))
'''

def ss(*num):
    s=0
    for i in num:
        s+=i
    return s
        
print(ss(87,897,76,23))

def sk(**nums):
    for k,v in nums.items():
        print(f"{k} is {v}")
    return nums
    
print(sk(name="ali",age=8))
square=lambda a:a**2
print(square(4))
list1=[8,9,7,6,8,7,8,8,7,6,5]
list2=[]
for i,e in enumerate(list1):
    if e%2==0:
        list2.append(i)
print(list2)
for i in list1:
    if i%2==0:
        list2.append(list1.index(i))
print(i)




       





    







        
        





















##print("Hello")
##print("World")
##print("Hello",end=" ")
##print("World")
##print("Hello\nWorld")
##print("Hello\tWorld")
##print("Hello\\nWorld")
##print("Hello\World")
###Qs WAP To print " 'He"1\"'lo
##print('"\'He"1\\"\'lo')
##print("\"'He\"1\\\"'lo")
##print(r"C:\Users\hp\OneDrive\Pictures\New folder\RGPV- Smart Card View_files")






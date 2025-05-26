#Data Types
'''
A datatype is a classification that specifies
the kind of data a variable can hold
'''
#in python built in types include:
#Numeric Types: int (integers)
num1=20
print(num1,type(num1))#20 class 'int'
#float (floating-point numbers)
num2=3.5
print(num2,type(num2))# 3.5 class 'float'
#complex
num3=3j
print(num3,type(num3))#3j class 'complex'
#Text Type: str(string of characters)
str="saklen"
print(str) #saklen
print(type(str))#'str'
str1="123a[]"
print(str1,type(str)) #123a[] class 'str'
#Sequence/collection Type: list(mutable)
#tuple(immutable),rang (sequential number)
list=[12,13,100,"hello",2.9,1j,True]
print(list,type(list)) # [12, 13, 100, 'hello', 2.9, 1j, True] class 'list'
#tuple
tup1=(22,89,"saklen",False,2.9)
print(tup1,type(tup1))#(22, 89, 'saklen', False, 2.9) class 'tuple'
#range
ran=range(1,90)
print(ran,type(ran))# range(1, 90) class 'range'
#Mapping Type: dict (key-value pairs)
dic1={"day":"wednesday","Month":"october","year":2024}
print(dic1,type(dic1))#{'day': 'wednesday', 'Month': 'october', 'year': 2024} class 'dic'
#set (unique items)
set={20,21,80}
print("set" ,set) #set {80, 20, 21}
print("type of",type(set)) # type of 'set'
#boolean Type: bool(True/False)
bool1=True
bool2=False
print(bool1)#True
print(bool2)#False
print(type(bool1))# class 'bool'



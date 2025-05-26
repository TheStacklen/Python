#procedural
'''
a=10
b=30
Sum=a+b
print(Sum)
diff=a-b
print(diff)
mul=a*b
print(mul)
#use for function
def sums(a,b):
    return a+b
print(sums(20,80))#redendancy decrease and reusability inccrease
'''
'''
Object Oriented Programming
Class And Object
class is a blueprint for creating objects.
'''
##class Student:# creating class
##    name="varisha"
##s1=Student()#creating object(instance)
##print(s1.name)
##s2=Student()
##print(s2.name)
##class Car:
##    color="black"
##    brand="mercedes"
##c1=Car()
##print(c1.color)
##print(c1.brand)

default constructor
class Student:
    def __init__(self):
        print("this is default constructor")
Student()
paramerized constructor
class Student:
    def __init__(self,name):
        print("adding new student in python")
        self.name=name 
s1=Student("maneer")
print(s1.name)
s2=Student("saklen")
print(s2.name)

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
s1=Student("saklen",98)
print(s1.name,s1.marks)
s2=Student("TABREJ",56)
print(s2.name,end=" ")
print(s2.marks)
        
























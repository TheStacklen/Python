'''
class Student:
    school_name="ASCT"     #static method
    def __init__(self,N,C):
        self.Class=N
        self.Name=C
    def read(self):
        print(f"{self.Name} is reading")
    def __str__(self):#function that is added to a class to control what shows up when we print an
        #object or turn it into a string
        return self.Name
s1=Student(10,"ali")
print(s1.read())
print(s1.Name)
print(s1.Class)
print(s1.school_name)
#Qs
class Fruit:
    def __init__(self,Color,Test,Size):
        self.color=Color
        self.test=Test
        self.size=Size
    def eat(self):
        print("fruit is eaten")
    def change_color(self,new):
        self.color=new
        
f1=Fruit("orange","sweet",10)
print(f1.eat())
print(f1.color)
print(f1.test)
print(f1.size)
f1.color="red"
print(f1.color)
f1.name="tomato"
print(f1.name)
f1.size=20
print(f1.size)
f1.change_color("green")
print(f1.color)
'''
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Inheritance<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#Single Inheritance
'''
class parent:
    a="father"
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def details(self):
        print(self.num1,self.num2)
class child(parent):
    pass
p_obj=parent(11,12)
c_obj=child(13,14)
print(p_obj.num1)
print(p_obj.num2)
print(p_obj.details())
print(c_obj.num1)
print(c_obj.num2)
print(c_obj.details())
'''
#Multiple Inheritance
'''
class parent1:
    name="parent1"
    num=50
    def method1(self):
        print("This is method 1 of parent 1")
    def method2(self):
        print("This in method 2 of parent 1")
class parent2:
    name="parent2"
    num=100
    def method1(self):
        print("This is method 1 of parent 2")
class child(parent1,parent2):
    pass
p1_obj=parent1()
p2_obj=parent2()
c1_obj=child()
print()
print(p1_obj.method1())
print(p1_obj.method2())
print(p2_obj.method1())
print(p1_obj.name)
print(p2_obj.name)
print(p1_obj.num)
print(p2_obj.num)

print(c1_obj.name)
print(c1_obj.num)
print(c1_obj.method1())
print(c1_obj.method2())
'''
#Multilevel Inheritance
'''
class Member:
    def __init__(self,Name,Contact):
        self.name=Name
        self.contact=Contact
    def show_details(self):
        print(f"Name: {self.name} Contact: {self.contact}")
class Student(Member):
    def __init__(self,name,contact,enroll,branch):
        Member.__init__(self,name,contact)
        self.enroll=enroll
        self.branch=branch
    def study(self):
        print(f"{self.name} is studying")
    def details(self):
        print(self.name,self.enroll,self.contact,self.branch)
class Teacher(Member):
    def __init__(self,name,contact,salary,subject):
        Member.__init__(self,name,contact)
        self.salary=salary
        self.subject=subject
    def teach(self):
        print(f"{self.name} is teaching {self.subject}")
        
m1=Member("saqib",999999999990)
print(m1.show_details())
print(m1.name)
print(m1.contact)
s1=Student("saklen",7943,7678788,"CSE")
print(s1.details())
t1=Teacher("shamim",23689488,29000,"Mechanical Engineering")
print(t1.name)
print(t1.contact)
print(t1.salary)
print(t1.subject)
print(t1.teach())
'''
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Polymorphism<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#Method Overriing
'''
class Member:
    def __init__(self,name,contact):
        self.name=name
        self.contact=contact
    def info(self):
        print(f"{self.name} is instance of Member class")
class Student(Member):
    def info(self):
        print(f"{self.name} is instance of Student class")
m1=Member("Abdul Samir",8986688)
print(m1.name)
print(m1.contact)
print(m1.info())
s1=Student("saklen",7878787878)
print(s1.info())
'''
#Operator Overloding
'''
class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    def __add__(obj1,obj2):
        return obj1.name+obj2.name
    def __sub__(o1,o2):
        return o1.price-o2.price
    def __mul__(ob1,ob2):
        return ob1.stock*ob2.stock
    
p1=Product("pencil",5,20)
p2=Product("pen",10,50)
print(p1+p2)
print(p1-p2)
print(p1*p2)
'''
#Encapsulation
'''
class Employee:
    def __init__(self,name,salary,job_title):
        self.name=name #public
        self._job_title=job_title#protect attribute
        self.__salary=salary#private attribute
    def get_salary(self):#getter
        return self.__salary
    def change_salary(self,new_salary):#setter
        self.__salary=new_salary
e1=Employee("Eqbal",50000,"Maneger")
print(e1.name)
e1.name="ali"
print(e1.name)
print(e1._job_title)
e1._job_title="devloper"
print(e1._job_title)
print(e1.get_salary())
e1.change_salary(100000)
print(e1.get_salary())
'''
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Abstraction<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area():
        pass
    @abstractmethod
    def perimeter():

        pass
class square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2
    def perimeter(self):
        return self.side*4
sq=square(12)
print(sq.area())
print(sq.perimeter())
        



    


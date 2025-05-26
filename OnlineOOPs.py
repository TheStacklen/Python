#class and object
##class Student:
##    name="ali"
##s1=Student()
##print(s1.name)
##s2=Student()
##print(s2.name)
##class Car:
##    color="blue"
##    brand="mercedes"
##c1=Car()
##print(c1.color)
##print(c1.brand)

#constructors
#default constructors
class Student:
    name="ali"
    def __init__(self):
        print("ading new student in python...")
s1=Student()
print(s1.name)
#parameteraze constructors
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("ading new student in python...")
s1=Student("ali",97)
print(s1.name,s1.marks)
s2=Student("Falak",98)
print(s2.name,s2.marks)
#class & instance(object) attributes
class Student:
    college_name="ASCT"
    name="falak"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
s1=Student("ali",99)
print(s1.name,s1.marks)
print(s1.college_name)
print(Student.name)
print(Student.college_name)
#method
class Student:
    def __init__(self,name):
        self.name=name
    def Hello(self):
        print("Hello",self.name)
s1=Student("ali")
s1.Hello()
print(s1.name)
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        Sum=0
        for val in self.marks:
            Sum+=val
        print("hi",self.name,"your avg score is ",Sum/3)
s1=Student("ali",[90,98,97])
s1.get_avg()
#staticmethod
class Student:
    @staticmethod#decorator
    def college():
        print("all saints' college of technology")
s1=Student()
s1.college()
#q
class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
    def debit(self,amount):
        self.balance-=amount
        print("Rs",amount,"was created")
        print("total balance = ",self.get_balance())
    def credit(self,amount):
        self.balance+=amount
        print("Rs",amount,"was creted")
        print("total balance = ",self.get_balance())
    def get_balance(self):
        return self.balance
acc1=Account(1000,123123123)
acc1.debit(100)
acc1.credit(100)

        


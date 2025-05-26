##list={"saklen":"ansari","age":"20"}
##print(" ".join(list),type(list))
##
##words=['1','2','3','4','5']
##print(" to ".join(words))
##l1=["saklen","chouradhari"]
##print(" ansari ".join(l1)
##x="saklen"
##def funct():
##    print(x)
##    global y
##    y="ansari"
##
##funct()
##print(y)
##num=13
##for i in range(2,num):
##    if num%i==0:
##        print(f"{num} is not prime")
##        break
##else:
##    print(f"{num} is prime")
##list1=[10,11,12,13,14,15,16,17]
##p_list=[]
##np_list=[]
##for i in list1:
##    for e in range(2,i):
##        if i%e==0:
##            np_list.append(i)
##            break
##    else:
##        p_list.append(i)
##print("prime",p_list)
##print("not prime",np_list)
        
import re
##str1="cry dry try fry Cry Dry cry danish"
##print(re.search("cry",str1))
##print(re.findall("cry",str1))
##print(re.search("[a-z]ry",str1))
##print(re.findall("[a-z]ry",str1))
##print(re.findall("c[Aa-zZ]",str1))
##print(re.findall("[^fcd]ry",str1))
##print(re.sub("ry","at",str1))
##pat1=re.compile("cry")
##print(re.search(pat1,str1))
##print(re.findall(pat1,str1))
##str1="ABC tr 23 y6 8u @!&*()+-_"
##print(re.search("\d",str1))
##print(re.findall("\d",str1))
##print(re.findall("\D",str1))
##print(re.search("\s",str1))
##print(re.findall("\s",str1))
##print(re.search("\S",str1))
##print(re.findall("\S",str1))
##print(re.search("\w",str1))
##print(re.findall("\w",str1))
##print(re.findall("\W",str1))
#range() return a sequance of number
##print(list(range(1,11)))
##print(tuple(range(1,11)))
##print(set(range(1,11)))
##print(list(range(2,11,2)))
##print(list(range(3,100,2)))
##str1="ans 90s < > , . ? / + = _ 0 9 $ # @ !"
##print(re.findall("\w",str1))
##print(re.findall("\W",str1))
##print(re.findall("[^\w]",str1))
#while
##i=2
##while i<10:
##    if i%3:
##        print(i)
##    i+=1
##num=[10,11,12,13,14,15,16,17,18,19,20]
##prime_list=[]
##not_prime_list=[]
##for i in num:
##    for  a in range(2,i):
##        if i%a==0:
##            break
##    else:
##        print(i)
##def primes(num1,num2):
##    for i in range(num1,num2):
##        for s in range(2,i):
##            if i%s==0:
##                break
##        else:
##            print(i)
##primes(10,30)

##name="eye"
##if name==name[-1::-1]:
##    print("pelendrome")
##else:
##    print("not pelendrome")
##def primes(num1,num2):
##    for i in range(num1,num2):
##        for a in range(2,i):
##            if i%a==0:
##                break
##        else:
##            print(i)
##primes(10,30)
##

##name="eye"
##
##if name==name[-1::-1]:
##    print("p")
##else:
##     print("n")
##name="saklen"
##name=name[-1::-1]
##print(name)
##rev_name=reversed(name)
##print(name)
##name="saklen nasari maneer anasari ahsan ansari eqbal ansari eqramul ansari"
##print(name.replace("k","q"))
##print(name)
##print(name.split(maxsplit=5))
##list1=[12,"helo",True,False,10.5,3j,"ali"]
##print(list1)
##name="saklen"
##print(len(name))
##print(len(list1))
##print(list1.index("ali"))
##print(list1[-1])
##print(list1[2:5:2])
##list1.append(2000)
##print(list1)
##list1.insert(1,5000)
##print(list1)
##list1[3]="khan"
##print(list1)
##list1.remove(5000)
##print(list1)
##pop=list1.pop(5)
##print(list1)
##list1.clear()
##print(list1)
##list2=[120,14,1,2,5,6,8,9]
####list2.sort(reverse=True)
####print(list2)
##sorted_list=sorted(list2)
##print(sorted_list)
##print(list2)
##i=2
##num=14
##while i<num:
##    if num%i==0:
##        print("num is not prime")
##        break
##        
##    i+=1
##else:
##    print("num is prime")
##    
##def nn(a):
##    for i in range(2,a):
##        if a%i==0:
##            print("not")
##            break
##    else:
##        print("prime")
##nn(97)
##def ss(*args):
##    s=0
##    for i in args:
##        s+=i
##    return s
##print(ss(18,20,30,40))
##square=lambda a:a**2
##print(square(4))
##
##print([i**2 for i in [1,4,5,8,9,21]])
##d1={"a":12,"b":14,"c":15,"d":80}
##for k,v in d1.items():
##    
##    d2=v**2
##print(d2)
##print({k:v**2 for k,v in d1.items()if v**2>500})
##list1=[10,50,24,15,100,58,99]
##list1.sort()
##print(list1)
##list1.sort(key=lambda a:a**2,reverse=True)
##print(list1)
##d1={"a":10,"b":20,"c":30,"d":40}
##s_list=sorted(d1.items(),key=lambda a:a[0])
##print(s_list)
##import os
##print(os.getcwd())
##print(os.listdir())
##class Student:
##    school_name="SGS"
##    def __init__(self,name,Class):
##        self.name=name
##        self.Class=Class
##    def read(self):
##        print(f"{self.name} is reading a book")
##    def __str__(self):
##        return self.name
##s1=Student("ali",1)
##print(s1.name)
##print(s1.read())
##class Fruits:
##    def __init__(self,color,tast,size):
##        self.color=color
##        self.tast=tast
##        self.size=size
##    def change_color(self,new):
##        self.color=new
##        
##f1=Fruits("red","sweet",10)
##print(f1.color)
##print(f1.size)
##f1.change_color("blue")
##print(f1.color)
##class A:
##    a="hello"
##    def __init__(self,num1,num2):
##        self.num1=num1
##        self.num2=num2
##    def details(self):
##        print(self.num1,self.num2)
##
##class B(A):
##    pass
##obj_a=(10,20)
##obj_a.details()
##print(B.a)
#single inheritance
##class A:
##    a="hello"
##    def __init__(self,num1,num2):
##        self.num1=num1
##        self.num2=num2
##    def details(self):
##        print(self.num1,self.num2)
##
##class B(A):
##    pass
##obj_a=A(20,30)
##obj_a.details()
##obj_b=B(40,50)
##obj_b.details()
##print(B.a)
##print(A.a)
###multiple inheritance
##class parent1:
##    name="parent1"
##    num=50
##    def method1(self):
##        print("this is method1 of parent1")
##class parent2:
##    num=25
##    def method2(self):
##        print("this is method1 of parent2")
##class child(parent1,parent2):
##    pass
##class child2(parent2,parent1):
##    pass
##c1=child()
##c1.method1()
##c1.method2()
##c2=child2()
##c2.method1()
###multilevel inheritance
##class Member:
##    def __init__(self,name,contact):
##        self.name=name
##        self.contact=contact
##    def show_details(self):
##        print(f"name:{self.name} contact:{self.contact}")
##class Student(Member):
##    def __init__(self,name,enroll,branch):
##        super().__init__(name,contact)
##        
##        self.enroll=enroll
##        self.branch=brancc
##    def study(self):
##        print(f"{self.name} is studying")
##    def details(self):
##        print(self.name,self.enroll,self.branch)
##s1=Student("saklen",787979,78,"cse")
##s1.study()
##



##def nn(a):
##    for i in range(2,a):
##        if a%i==0:
##            print(f"{a} is not a prime no ")
##            break
##    else:
##        print(f"{a} is a prime no ")
##nn(10)

##n=int(input("enter a number"))
##i=2
##while i<n:
##    if n%i==0:
##        print("not a prime no")
##        break
##    i+=1
##else:
##    print("prime no")
##
##
#
##employees = {
##    "Emp1": {"age": 30, "skills": ["Python", "C++"]},
##    "Emp2": {"age": 25, "skills": ["JavaScript", "HTML"]}
##}
##print(employees["Emp2"]["skills"][1])
##employees["Emp2"]["skills"][1]="c#"
##print(employees["Emp2"]["skills"][1])
##
##list1=[[1,2,3] , [4,5,[10,16]] , [7,8,9]]#8
##print(list1[2][1])



i=2
num=13
while i<num:
    if i%num==0:
        print("not")
        break
    i+=1
else:
    print("prime")












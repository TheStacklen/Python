#Revision
##print("hii I am Saklen")
##print("saklen",end=" ")
##print("ansari")
##_123="saklen"
##print(_123)
##num=3j
##print(num,type(num))
##num=["saklen","ansari",898,90.98,True,False]
##num[0]="maneer"
##num.remove("ansari")
##num.pop(2)
##num.append(500)
##num.insert(3,1000)
##print(num)
##print(dir(list))
##tup=("saklen","ansari",12,20.5,True,False)
##print(tup,type(tup))
##tup.append(121)
##print(tup)
##tup[1]="tabrej"
##
##print(tup)
##r=range(1,30)
##print(r,type(r))

##sets={12,30.5,"saklen","maneer",True,False}
##print(sets,type(sets))
##sets[1]="mohammad"
##print(sets)#error
##b1=True
##b2=False
##print(b1)
##print(b2)
##print(type(b1))
##print(type(b2))
#python operator
#arithmatic operator (+,-,*,/,%,//)
##print(2+2)
##print(10-5)
##print(20*2)
##print(20/3)
##print(20%3)
##print(20//3)
#comparison operator (==,!=,>=,<=)
##num=12
##print(num==12)
##print(num!=12)
##print(num<13)
##print(num>11)
##print(num<=13)
##print(num>=10)
###assinment operator (+=,-=.*=,/=,//=,%=)
##x=3
##x+=2
##print(x)
#string
##str1="saklen"
##print(str1,type(str1))
##print(str1[0])
##print(len(str1))
##print(str1[1:len(str1):2])
##print(str1.index("k"))
##print(str1.upper())
##print(str1.lower())
##print(str1.capitalize())
##s="saklen ansari mansoori"
##print(s,type(s))
##s.replace("mansoori","khan")
##print(s.replace("mansoori","khan"))
##print(s.replace("a","q"))
#split
##s="saklen raza"
##print(s.split(" "))
##m=s.split("a",maxsplit=2)
##print(m)
##m=s.split("a",maxsplit=3)
##print(m)
#casting
##f=2.5
##print(f,type(f))
##int1=int(f)
##print(int1,type(int1))
##int1=12
##f=float(int1)
##print(f,type(f))
##str1="12"
##int1=int(str1)
##print(int1,type(int1))
##int1=12
##str1=str(int1)
##print(str1,type(str1))
##sets={"saklen","ansari","ansari",12,10,15,12}
##print(sets)
##print(sets)
###sets[1]="name" #error
##print(sets)
#format string
##num=int(input("Enter Frist Number: "))
##num1=int(input("Enter Second Number: "))
##print(f"sum is {num+num1}")
##age=int(input("Enter Your Age: "))
##if age>=18:
##    print("eligible for vote")
##elif age==0:
##    print("Enter The Valid Age: ")
##else:
##    print("not eligible for vote")
##try:
##    
##    num=int(input("Enter Any Number: "))
##    if num%2==0 and num%3==0:
##        print(f"{num} divisible by both")
##    elif num%2==0:
##        print(f"{num} is divisible by 2")
##    elif num%3==0:
##        print(f"{num} is divisible by 3")
##except ValueError:
##    print("enter the valid number")
###WAP to determine if a triangle is equilateral,isoscales and scalen
###based on its side lengths
##num1=int(input("Enter the frist lenght: "))
##num2=int(input("Enter the second lenght: "))
##num3=int(input("Enter the third lenght: "))
##if num1!=num2 and num2!=num3:
##    print("Scalen Triangle")
##elif (num1==num2 and num3!=num1)or(num2==num3 and num1!=num2)or(num1==num3 and num2!=num3):
##    print("Isoscale Triangle")
##elif num1==num2 and num2==num3:
##    print("Equilateral Triangle")

##list1=["saklen","maneer","eqbal",12,20.5,True,False]
##print(list1)
##print(len(list1))
##print(list1.index("eqbal"))
##print(list1[2])
##print(list1[0:len(list1):2])
####s="hello"
####print(s[1:len(s):2])
##list1.append(100)
##print(list1)
##list1.insert(0,100)
##print(list1)
##list1[2]="reshma"
##print(list1)
##list1.remove("reshma")
##print(list1)
##pops=list1.pop()
##print(list1)
##print(pops)
##pops=list1.pop(3)
##print(pops)
##print(list1)
##list2=["saniya","soniya",20,50.5,True,False]
##print(list1+list2)
##list1.extend(("reshma","muskan","khushi"))
##print(list1)
##list1=[12,154,6,14,18,1,3,5,2]
##print(list1)
####list1.reverse()
####print(list1)
####list1.sort( reverse=False)
####print(list1)
##sorted_list=sorted(list1)
##print(sorted_list)
##sorted_list=sorted(list1,reverse=True)
##print(sorted_list)
##print(list1)
##list1=[12,154,6,14,18,1,3,5,2]
##rev_list=reversed(list1)
##print(list(rev_list))
##rev_list=reversed(list1)
##print(rev_list)
##tup=(12,20,50,3,"saklen","hello","varisha",False,20,51,20,"varisha")
##print(tup)
##print(tup.count(20))
##print(tup.count("varisha"))
####print(tup)
####print(tup)
##set1={10,20,30,40,50,50}
##print(set1)
####print(sets)
####print(sets)
##set2={10,100,200,50,500}
##print(set2)
##print(set1.intersection(set2))
##print(set1.union(set2))
##print(set1|set2)
##print(set1&set2)
#dictionary
##student={"name":"saklen","semester":3,"age":19}
##print(student)
##print(student["age"])
##student["name"]="aarif"
##print(student)
##student["enrollment"]=116
##print(student)
##print("age" in student)
##age=student.pop("age")
##print(age)
##print(student)
##print(student.keys())
##print(student.values())
##print(student.items())
##list1=[10,20,30,40]
##print(tuple(enumerate(list1)))
##print(list(enumerate(list1)))
##print(dict(enumerate(list1)))
##list1=[10,20,30,40]
##list2=["saklen","maneer","eqbal","ahsan","ekramul"]
##print(list(zip(list1,list2)))
####print(tuple(zip(list1,list2)))
####print(dict(zip(list1,list2)))
##list3=["allsaint","chouradhari","patna","up","up"]
##print(list(zip(list1,list2,list3)))
##print(tuple(zip(list1,list2,list3)))

#missing quastions
#range
##print(list(range(1,10,2)))
##print(list(range(10,0,-1)))
##print(list(range(1,50,2)))
##import time
##for i in range(10):
##    print(i,"hello sir")
##    time.sleep(0.5)
##odd_list=[]
##even_list=[]
##for i in range(1,51):
##    if i%2==0:
##        even_list.append(i)
##    else:
##        odd_list.append(i)
##print("even num=",even_list)
##print("odd num=",odd_list)
#for else
##import time
##for i in range(1,10):
##    print(i)
##    time.sleep(1)
##else:
##    print("loop terminated")
##for i in range(1,10):
##    print(i)
##    if i==5:
##        break
##else:
##    print("terminated the loop")
##for i in range(1,10):
##    if i==5:
##        continue
##    print(i)
##else:
##    print("for else block")
#while loop
##i=1
##while i<11:
##    print(i,"hello sir")
##    i+=1
##i=1
##divisible_by11=0
##while i<100:
##    if i%11==0:
##        divisible_by11+=1
##    i+=1
##print(divisible_by11)
##num=int(input("Enter Any Number: "))
##i=2
##while i<num:
##    if num%i==0:
##        print("not")
##        break
##    i+=1
##else:
##    print("prime")
    
#nested list
#a nested list is simply a list that contain other lists as its elements
#its like having a list inside another list.
##list1=[[1,2,3],4,5,[10,11],6,7,8]
##print(list1)
##print(list1[0][2])
##print(list1[1],list1[2])
##print(list1[3][0])
##print(list1.index(8))
#nested dictionary
#a nested dictionary is a dictionary that contains other dictionries as values
##dict1={"product1":{"name":"abcd","price":30,"color":{"red","blue"}},
##       "product2":{"name":"xyz","price":100,"color":{"black","green"}}}
####print(dict1)
##print(dict1["product1"]["name"])
##print(dict1["product2"]["price"])
##print(dict1["product1"]["color"][0])
#randam
#python module is a file that contains buil-in function classes its and variables


import random

##rand_rang=random.randrange(1,5)
##print(rand_rang)
##print(random.randrange(1,5))
##list1=[]
##for i in range(8):
##    list1.append(random.randint(1,20))
##print(list1)
##    print(random.randint(1,20))
##l1=10
##l2=20
##for i in range(1,5):
##    print(random.randint(l1,l2))
##s="saklen"
##print(s)
##print(random.choices(s,k=6))
#Function
#a function is a block of organized reusable code that performs
#a specifie task functions make that code easir to understand.
##def s():
##    print("it is inside the function block")
##s()
##def a():
##    print("it is inside the function block")
##    return "this is returned by function "
##print(a())
##def add(a,b):
##    return a+b
##def check(num):
##    if num%2==0:
##        return "even"
##    else:
##        return "odd"
##print(check(51))
##for i in range(1,20):
##    print(i,check(i))
##def sums(num):
##    s=0
##    for i in range(0,num+1):
##        s+=i
##    return s
##  
##num=5
##print(sums(num))
##def mul(num):
##    m=1
##    for i in range(1,num+1):
##        m*=i
##    return m
##print(mul(4))

#missing two topics
#argument and


#listcomprehensions.py
##print([i for i in "saklen"])
##list1=[10,20,21,31]
##print([i+2 for i in list1])
##print([i**2 for i in list1])
#dictionarycomprehesion
##print({i:len(i) for i in ["saklen","nameer","tabrej","irfan","zulfekar"] })

##d1={"abc":10,"xyz":20}
##print({k:v*2 for k,v in d1.items() if v**2>100})

#key sorting
##l1=[10,201,20,30,50,840,14,5,8]
##l1.sort(reverse=True)
##print(l1)
##l2=[2,5,4,3,1]
##l2.sort(key= lambda a:a**2,reverse=True)
##print(l2)
d1={"a":50,"b":20,"c":30}
print(d1)
sorted_d=sorted(d1.items(),key=lambda a:a[1])
print()
print(sorted_d)













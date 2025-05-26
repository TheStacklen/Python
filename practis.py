#####reaplace
####str="sad"
####print(str.replace("s","d"))#dad
#####or
####str1=str.replace("s","d")
####print(str1)#dad
##str1="hello world good evening"
####print(str1)#hello world good evening
#####split
####sep1=str1.split(" ")
####print(sep1)#['hello', 'world', 'good', 'evening']
####sep2=str1.split("o")
####print(sep2)#['hell', ' w', 'rld g', '', 'd evening']
####sep3=str1.split(" ")
####print(sep3)#['hello', 'world', 'good', 'evening']
##sep4=str1.split(maxsplit=2)
##print(sep4)#['hello', 'world', 'good evening']
###casting
##f1=3.5
##int1=int(f1)
##print(int1,type(int1))#3 <class 'int'>
##str1="12",
##int2=int(str1)
##print(int2,type(int1))#12 <class 'int'>
##int4=1234
##str2=str(int4)
##print(str2,type(str2))#1234 <class 'str'>
##num1=10
##num2=8
##print("sum of {} and {} is {}".format(num1,num2,num1+num2))#sum of 10 and 8 is 18
##print(f"sum of {num1} and {num2} is {num1+num2}")#sum of 10 and 8 is 18
###ifelse
##a=4
##if a==4:
##    print("we are in if block")#we are in if block
##
##if True:
##    print("if block")#it will run
##elif False:
##    print("elif block")
##
##if False:
####    print("if block")
####elif True:
####    print("elif block")#it will run
####
####print("out of condition")
#####list
####l1=["saklen",34,67,90,9.3,True]
####print(l1)
####print(len(l1))
####l2=list((23,78,90,"ansari"))
####print(l1)
####print(l2)
#####indexing
####l1=["saklen",34,67,90,9.3,True]
####print(l1[-1])
####print(l1[4])
#####slicing
####l1=["saklen",34,67,90,9.3,True]
####print(l1[0:3])#['saklen', 34, 67]
####print(l1[2:])#[67, 90, 9.3, True]
####print(l1[:4])#['saklen', 34, 67, 90]
####print(l1[-1::-1])#[True, 9.3, 90, 67, 34, 'saklen']
####print(l1[-1::-2])
#####index
####list1=["python",12,13,False,12]
####print(list1)
####list1[2]="saklen"
####print(list1)
#####changing the value
##student1={"name":"Saklen","semester":3}
##print(student1["semester"])
##student1["semester"]=2
##print(student1)
##student1["branch"]="CS"
##student1["college"]="ASCT"
##print(student1)
##college=student1.pop("college")
##print(college)
##print(student1)
##
###data types
##num1=90
##print(num1,type(num1))
##num2=90.5
##print(num2,type(num2))
##num3=3j
##print(num3,type(num3))
##str1="saklen"
##print(str1,type(str1))
##str2="123a[]"
##print(str2,type(str2))
###list
##list1=[10,20,30,"saklen",False,True,1j]
##print(list1,type(list1))
###tuple
##tuple1=("saklen",12,10,True,False,1j)
##print(tuple1,type(tuple1))
###range
##range1=(1,20)
##print(range1,type(range1))
###dictionary
##dict1={"name":"saklen","age":19,"enroll":97,}
##print(dict1,type(dict1))
###sets(unique itens)
##set1={22,10,80}
##print(set1)
###boolean type: bool (True/False)
##bool1=True
##bool2=False
##print(bool1)
##print(bool2,type(bool2))
###length
##a="saklen"
##print(len(a),type(a))
###index
##print(a[0])
##print(a[3])
##print(a.index("n"))
##print(a.index("k"))
###slicing
##print(a.upper())
###replace
##s="cat"
##s1=s.replace("c","b")
##print(s)
##str3="python programing"
##print(str3.replace("p","s"))
###split
##str1="hello world good morning sir"
##print(str1)
##print(str1.split(" "))
##print(str1.split(maxsplit=3))
##list1=["python",12,13,False,12]
##print(list1)
##list1[2]="hello"
##print(list1)
##list1.append(101)
##print(list1)
##list1.insert(3,"saklen")
##print(list1)
###change elements
##list1[2]=14
##print(list1)
##num1=float(input("Enter first number :"))
##num2=float(input("Enter second number :"))
##print(f"sum of {num1} and {num2} is ",num1+num2)
#length
##name=["saklen","ansari",786]
##print(name,len(name))
##l1=["saklen","python",100,50,50.5,True]
####print(l1.index(50))
####print(l1[0:4])
##l1.append(10)
##l1.insert(1,"ansari")
##print(l1)
###change elements
##l1[1]="khan"
##print(l1)
###remove
##l1.remove(50)
##print(l1)
##list2=['saklen', 'khan', 'python' 100, 50.5,]
##pop=list2.pop()
##print(list2)
##print(pop)
##list2.clear()
##print(list2)
##list2.extend(("saklen",12,30))
##print(list2)
##l3=[12,51,62,9,53,1,8,11,9,12,10,3,5,7,6,4,1]
##l3.sort(reverse=True)
##print(l3)
##print("original list",l3)
##sorted_list=sorted(l3,reverse=True)
##print("sorted list",sorted_list)
##print(sorted(l3))
##print(l3)
##l4=reversed(l3)
##print(list(l4))
##print(l3.count(1))
##l4={12,51,62,9,53,1,8,11,9,12,10,3,5,7,6,4,1}
##l5={1,12,5,51,6,7,8,9,2,5,6,3,1,5,8,4,2,54,}
##set_union=l4.union(l5)
##print(set_union)
##print(l4.intersection(l5))
##l5=input("Enter your name :")
##even_lengths=[]
##odd_lengths=[]
##for s in l5:
##    if len(s)%2==0:
##        even_lengths.append(s)
##    else:
##        odd_lengths.append(s)
##print("even_lengths",even_lengths)
##print("odd_lengths",odd_lengths)
##list1=[100,200,2,4,4,500]
##sum_of=0
##for i in list1:
##    sum_of+=i
##print(sum_of)
##num=1
##while num<100:
##    if num%11==0:
##        print(num)
##        num+=1
##print(r"C:/Users/hp/OneDrive/Documents/unit 1 \nquestions and answer for mid sem.pdf")
##a="saklen"
##print(a.replace("s","a"))
##name=int("enter the number")
##print(name)
##lis=[78,89,56,45,54,46,90,13,17,23]
###lis=[]
###pri=[]
##for num in lis:
##    for i in range(2,num):
##        if num%i==0:
##            print("not")
##            break
##    
##    else:
##        print("yes")

##i=1
##div_by11=[]
##while i<100:
##    if i%11==0:
##        div_by11.append(i)
##        #print(i)
##    i+=1
##print(div_by11)
##num=13
##i=2
##while i<num:
##    if num%i==0:
##        print("not")
##        break
##    i+=1
##    
##else:
##    print("prime")

##s=143
##rev=0
##for i in range(len(str(s))):
##    mod=s%10
##    rev=rev*10+mod
##    s=s//10
##print(rev)
##student1={"name":"ibrahim","semester":3}
##print("semester" not in student1 )

##l3=[12,51,62,9,53,1,8,11,9,12,10,3,12,5,7,6,4,1,12]
##print(l3[2])
##def check(num):
##    for i in range(2,num):
##        if num%i==0:
##            return "not prime"
##    else:
##        return "prime"
##num=int(input("enter any number :"))
##print(check(num))

##i=1
##div_by_7=[]7
##while i<1000:
##    if i%7==0:
##        div_by_7.append(i)
##    i+=1
##print(div_by_7)


###Nested
##list1=["hello","python","cat","world"]
##for e in list1:
##    for i in e:
##        print(i)

##l1=[[1,2,3],[4,5,[10,16]],[7,8,9]]#O/P is 3 5 16 8
##print(l1[0][2],l1[1][1],l1[1][2][1],l1[2][1])
##name="saklen ansari chauradhari"
##print(name,end=(""))
##print(name.upper())
##print(name.lower())
##print(name.capitalize())
##print(name[2])
##print(name.index("n"))
##print(name[:len(name):2])
##print(name.replace("s","a"))
##print(name.replace("chauradhari","sono"))
##print(name.split(" "))
##print(name.split(maxsplit=4))
##num=range(1,50)
##print(num,type(num))
##num="12"
##i=int(num)
##print(i,type(i))
##f=2.12
##i=int(f)
##print(i,type(i))

##tup=(12,13,14,15,16,17,18,True,False)
##print(tup)
###tup[6]="maneer" #tuple is not changeble so this line in error
##print(tup)
###print(tup.replace("True","zulfekar"))


##list1=[12,13,14,15,16,17,18,True,False]
##print(list1[-1::-1])
##print(list1.index(18))
##list1[6]="saklen"
##print(list1)
##list1.append(50)
##list1.insert(2,"saklen")
##print(list1)
###change values
##list1[3]="saqib"
##print(list1)
##po=list1.pop(2)
##print(list1)
##list1.remove(17)
##print(list1)
##list1.clear()
##print(list1)
##list1=[12,13,14,20,50]
###list2=[50,60,70,82,50]
####del list1[4]
####print(list1)
####list1.sort(reverse=False)
####print(list1)
####sorted_my_list=sorted(list1)
####print(sorted_my_list)
####list1.reverse()
##s=list(reversed(list1))
##print(s)
####print(list1)
####print(len(list1))
####print(list1.count(20))
####add_lists=list1+list2
####print(add_lists)
##list1.extend((20,30,79,63,))
##print(list1)
##set1={12,10,30,60,50}
##print(set1,type(set1))
##set2=set((20,30,40,50,60))
##print(set2,type(set2))
##set2.add(3)
##print(set2)
###ssets
##set1={10,20,30,40,50,10}
##set2={80,90,20,30,50,40}
###set1[2]=30
###set_union=set1.union(set2)
##set_union=set1|(set2)
##print(set_union)
##print(set1.union(set2))#{40, 10, 80, 50, 20, 90, 30}
###set_intersection=set1.intersection(set2)
##set_intersection=set1&(set2)
##print(set_intersection)#{40, 50, 20, 30}
#dictionary
##name=["apple","banana","mango"]
##price=[100,30,50]
###print(price)
##pairs=list(enumerate(price))
##print(pairs)
##name_zip=list(zip(name,price))
##print(name_zip)
##prd1={"name":"apple","price":100,"stock":20,}
##print(prd1,type(prd1))
##prd1["name"]="saklen"
##prd1["quantity"]=10
##print(prd1)
##name=["apple","banana","mango"]
##frt_index=name.index("apple")
##print(frt_index)
##info={"name":"saklen","department":"CSE","semester":3,"enrollment":116}
####print("name" not in info)
####info["age"]=19
####print(info)
####info["semester"]=4
####print(info)
####info.pop("age")
####print(info)
####print(info.keys())
####print(info.values())
####print(info.items())
##a=info.items()
##print(a)
##list1=[10,20,30,40,50,60,]
##list2=[100,200,300,400,500,600,700]
##list3=["sakeln","aarif","abdullah","rahmatullah","arman"]
##print(list(zip(list1,list2,list3)))
###list1.sort()
##
##print(tuple(enumerate(list1)))
##list1.append(90)
##print(list1)
##print(list1.index(50))
##list1.insert(5,55)
##print(list1)
##list1=["saklen","abbas","tahir"]
##print("join".join(list1))
#print(list(range(2,50,2)))
##for i in range(1,10):
##    print(i,"Hello Saklen")

##even_num=[]
##odd_num=[]
##for i in range(1,51):
##
##    if i%2==0:
##        even_num.append(i)
##    else:
##        odd_num.append(i)
##print(even_num)
##print(odd_num)

##nums=[]
##strs=[]
##list1=[10,"a","b","c",20,30,40,50,"d","e"]
##for s in list1:
##    if type(s)==int:
##        nums.append(s)
##    elif type(s)==str:
##        strs.append(s)
##print(nums)
##print(strs)
##list4=["saklen","ali","zulfekar","abdullah","abdulhafiz","aftab"]
##even_length=[]
##odd_length=[]
##for i in list4:
##    if len(i)%2==0:
##        even_length.append(i)
##    else:
##        odd_length.append(i)
##print("even_length :",even_length)
##print("odd_length :",odd_length)
##name=input("Enter Any World :")
##for i in name:
##    if i in ["a","e","i","o","u","A","E","O","I","U"]:
##        print(f"{name} is vowels")
##    else:
##        print(f"{name} is not vowels")
##Sum=0
##for i in range(1,11):
##    Sum+=i
##print(Sum)
##fact=1
##for i in range(1,5):
##
##    fact*=i
##print(fact)
##list1=[100,200,300,400,500,600]
##sub=0
##for i in list1:
##    sub+=i
##print(sub)
##for i in range(1,6):
##    
##    print(i)
##else:
##    print("for loop terminated")
##for n in range(50):
##    print(n)
##    if n ==20:
##        break
##else:
##    print("loop terminated")
##for i in range(50):
##    if i%2==0:
##        continue
##    print(i)
##else:
##    print("for else block")
##num=int(input("Enter Any Number :"))
##for i in range(1,11):
##    print(f"{num}*{i}= {i*num}")

##
##
##QUESTIONS from class room file (loop3)
###Q given a list l1[250,500,650,700]
###make dictionary with keys as indeces of l1 and values as elements of l1
##l1=[250,500,650,700]
##dict1={}
##for index,element in enumerate(l1):
##    dict1[index]=element
##    
##print(dict1)
 
###Q Given a list of strings["abc","hello","friday","saklen"]
###make a dictionary with keys as elements of list and values are their lengths.
##list1=["abc","hello","friday","saklen"]
##list2=[]
##for i in list1:
##    list2.append(len(i))
##    
##print(list(zip(list1,list2)))

###Q Given a list of numbers[5,12,8,3] create
###a new list where each number is multiplied by 2.
##list2=[5,12,8,3]
##multiplied_by2=[]
##for i in list2:
##    multiplied_by2.append(i*2)
##print(multiplied_by2)

###Q1 Given a list of numbers[2,4,6,8,10],
###creat a new dectionary with the keys are the number
###and values are their squares
##list1=[2,4,6,8,10]
##list2=[]
##for i in list1:
##    list2.append(i**2)
##print(dict(zip(list1,list2)))

###Q2 Given a list of names["smith","kane","joe","khan"]
###creat a list of the first latrers of each name
##list1=["Smith","Kane","Joe","Khan"]
##list2=[]
##for i in list1:
##    list2.append(i[0])
##print(list2)


##i=0
##while i<11:
##    if i%2==0:
##        print(f"{i} is even")
##    else:
##        print(f"{i} is odd")
##    i+=1

##i=1
##divisible_by11=[]
##while i<100:
##    if i%11==0:
##        divisible_by11.append(i)
##    i+=1
##print(divisible_by11)

##while True:
##    print("hello")
##    break
##num=10
##while num>0:
##    print(num)
##    num-=1
##else:
##    print("while else block")

##list1=["hello","python","cat","world"]
##for i in list1:
##    #print(i)
##    for e in i:
##        print(e)

##num=72
##for i in range(2,num):
##    if num%i==0:
##        print("this num is not prime")
##        break
##else:
##    print("this num is prime")
##num=13
##i=2
##while i<num:
##    if num%i==0:
##        print(f"{num} is not prime")
##        break
##    i=i+1
##else:
##    print(f"{num} is prime")
###nested 
##list1=[[1,2,3],[4,5,[10,16]],[7,8,9]]#o/p 3,5,16,7
##print(list1[0][2],list1[1][1],list1[1][2][1],list1[2][0])
###Random
##import random
##ran_num=random.randrange(1,10)
##print(ran_num)
##import random
##lis=[]
##for i in range(20):
##    lis.append(random.randint(1,50))
##print(lis)
##import random
##str1="saklen"
##print(random.choice(str1))
##list1=[10,20,30,True,40]
##print(random.choice(list1))
##import random
##list1=[10,40,50,60,80,90,True]
##print(random.choices(list1,k=7))
##str2="saklen ansari"
##print(random.choices(str2,k=10))
###Function
##def sa():
##    print("I`m saklen")
##    return "this is return by function"

##print(sa())
##def add(a,b):
##    return a+b
####a=int(input("enter 1st number :"))
####b=int(input("enter 2nd number :"))
####print(add(a,b))
###or
##s=add(2,3)
##print(s)
##    
##def check(num):
##    if num%2==0:
##        return "even num"
##    else:
##        return "odd num"
##num=int(input("enter any number :"))
##print(check(num))
##for i in range(20):
##    print(i,check(num))

##def add(num):
##    s=0
##    for i in range(0,num+1):
##        s+=i
##    return s
##print(add(5))
##l1=[10,20,30,40,50,20]
##l2=[90,40,20,30,50,20,100]
##comman=[]
##for i in l2:
##    if i in l2 and i not in comman:
##        comman.append(i)
##print(comman)

##def calculate(a,b,c):
##    if "+"or"-"or "*":
##        if b=="+":
##            return a+c
##        elif b=="-":
##            return a-c
##        elif b=="*":
##            return a*c
##        else:
##            return "please vailid operator"
##a=int(input("enter 1st num :"))
##b=input("enter operator :")
##c=int(input("enter 2nd num :"))
##print(calculate(a,b,c))
##list1=[10,500,30,600,900]
##m=900
##for i in list1:
##    if m>i:
##        m=i
##print(m)

##def function(*args):
##    return args
##print(function(1,2,3,5,4,6))
##names=["saklen","varish","sahbaj","farhan","abdullah","abdulhafiz"]
##def len_names(list):
##     return len(list)
##print(len_names(names))
##names=["saklen","varish","sahbaj","farhan","abdullah","abdulhafiz"]
##def saklen(list):
##    for elements in list:
##        
##        print(elements,end=" ")
##saklen(names)
##num=5
##factorial=1
##for i in range(1,num+1):
##    factorial*=i
##    
##print(factorial)
##def fac(name):
##    fac=1
##    for i in range(1,num+1):
##        fac*=i
##    print(f"{num} of factorial ",fac)
##        
##num=int(input("Enter Any Number :"))
##fac(num)
#WAF to convert INR to USD
##def convert(USD):
##    INR=USD*83
##    return (f"{USD} USD TO {INR} INR")
##rupees=float(input("Enter the USD :"))
##print(convert(rupees))
###WAF to convert USD to INR
##def convert(USD):
##    INR=USD/83
##    return (f"{USD} INR TO {INR} USD")
##rupees=float(input("Enter the INR :"))
##print(convert(rupees))
###chack prime numbers
##def check(num1,num2):
##    counts=0
##    for i in range(num1,num2):
##        for s in range(2,i):
##            if i%s==0:
##                break
##        else:
##            counts+=1
##    return counts
##
##print(check(10,30))
##def mul(*num):
##    all_mul=1
##    for i in num:
##        all_mul*=i
##    return all_mul
##print(mul(12,2,2))
##
#one line fanction
##square=lambda a:a**2
##s=int(input("enter any number :"))
##print(square(s))
##num=lambda a:"even" if a%2==0 else "odd"
##print(num(5))
##up=lambda s:s.upper()
##a=input("enter your name :")
##print(up(a))
##rev=lambda a: f"{s} is palidrom" if a==a[-1::-1] else f"{s} is not palidrom"
##s="saklen"
##print(rev(s))
##
##def lens(n):
##    return len(n)
##list1=["ansari","aftab"]
##le_list=list(map(lens,list1))
##print(le_list)
##list2=[10,20,14,50]
##sq_list=list(map(lambda a:a**2,list2))
##print(sq_list)
##list1=[20,30,50,60]
##list2=[10,20,14,50]        
##def add(a,b):
##    return a+b
##print(list(map(add,list1,list2)))

##list1=[20,30,50,60]
##list2=[10,20,14,50]
##print(list(map(lambda a,b:a+b,list1,list2)))
##f=["md","mr","mrs"]
##l=["saklen","aarif","samikchha"]
##def add(a,b):
##    return a+" "+b
##print(list(map(add,f,l)))
##def check(x):
##    if x%2==0:
##        return True
##    else:
##        return False
##list1=[1,2,3,4,5,6,7,8,9,10]
##even_list=list(filter(check,list1))
##print(even_list)
##list1=[1,2,3,4,5,6,7,8,9,10]
##even_list=list(filter(lambda a:a%2!=0,list1))
##print(even_list)
###Map
###WAP to convert a list of temperatures in celsius to fahrenheit
##def convert(celcius):
##    fahrenheit=celcius*(9/5)+32
##    return f"{celcius} celcius is equal to {fahrenheit} fahrenheit "
##print(convert(2))

###WAP to extract the first latter of each word in a list of strings
##def latter(n):
##    return n[0]
##list1=["sohail","tabrej","warish"]
##print(list(map(latter,list1)))
###using lambda
##list1=["sohail","tabrej","warish"]
##print(list(map(lambda n:n[0],list1)))

###WAP to combine corresponding elements of two lists into tuples.
##def tuples(n):
##    return tuple(zip(list1,list2))
##list1=["a","b","c","d"]
##list2=[10,20,30,40,50]
##print(list(map(tuples,(list1,list2))))

#WAP to replace all vowels in a list of strings with string 'v'

###WAP to filter a list of strings to keep only element those length is 4.
##list1=["name","abdullah","yusuf","farhan","tabrej"]
##print(list(filter(len,list1)))        

##list1=[-5,-9,-4,-6,-2,3,4]
##print(list1)
##list1.sort(reverse=True)
##print(list1)
##list1.sort(key=lambda a:a**2,reverse=False)
##print(list1)

##dict1={"a":12,"c":10,"d":30,"b":50}
##print(dict1)
###sorting on the basis of keys of dictionary
##sorted_dict=sorted(dict1.items())
##print(sorted_dict)
###sorting on the basis of values of dictionary
##sorted_dict=sorted(dict1.items(),key=lambda a:a[1])
##print(sorted_dict)
##sorted_list=sorted(dict1.items(),key=lambda a:a[1],reverse=True)
##print(sorted_list)

##import calendar
##year=int(input("enter year :"))
##month=int(input("enter month :"))
##date=int(input("enter date :"))
##print(calendar.month(year,month,date))


###map()
##def s(a):
##    return a**2
##list1=[10,20,30]
##print(list(map(s,list1)))
##print(list(map(lambda a:a**2,list1)))

##list1=[120,201,305,5004,900]
##def dis(a):
##    return a-(a*10)/100
##print(list(map(dis,list1)))
##print(list(map(lambda a:a-(a*10)/100,list1)))
##l1=[2,4,6]
##l2=[6,2,8]
##print(list(map(lambda a,b:a+b,l1,l2)))

#filter

##list1=[10,11,20,30,45,69,80]
##def check(a):
##    if a%2!=0:
##        return True
##print(list(filter(check,list1)))
##print(list(filter(lambda a:a%2==0,list1)))

#reduce

#l2=[100,200,300,400]
##def s(a,b):
##    return a*b
##from functools import reduce
##l1=[10,20,30,50]
##print(reduce(lambda a,b:a*b , l1))
##print(reduce(lambda a,b:a*b,range(1,5)))

##str="hello"
##for i in str:
##    print(i.upper())
##print([i.upper() for i in "hello"])
##print(8/4/2,8/(4/2))
##print("abc.DEF".capitalize())
#map
##def square(n):
##    return n**2
##list1=[2,4,5]
##print(list(map(square,list1)))
##print(list(map(lambda a:a**2,list1)))
##import re
##str1="cry dry fry sry ary a n Cry"
##print(list(re.finditer("cry",str1)))
##print(list(re.findall("cry",str1)))
##print(re.search("cry",str1))
##def add(a,b):
##    return a+b
##s=20
##k=35
##print(add(30,20))
##print(add(s,k))
#regex
##import re
##str1="saken cry fry dry sry nry Cry Dry cry Fry chouradhary"
####print(re.search("cry",str1))
####print(re.findall("cry",str1))
####print(re.search("[a-z]ary",str1))
####print(re.findall("[aA-zZ]ry",str1))
####print(re.sub("c","z",str1))
####print(re.)
##for i in re.finditer("cry",str1):
##    print(i.span())
##    print(i.start())
##    print(i.end())
##    print(i.group())
##    print("\n")
##import re
##str2="regex is a smart way 090@."
##print(re.findall("\b",str2))
##s1='''regex is a smart way to search and
##organize text easily and efficiently'''
##print(re.findall("\w{3}",s1))
##print(re.findall("\s(\w{3})\s",s1))
##print(re.findall("\s(\w{2,6})\s",s1))
##n="1245155 45124 551525121 41528552385 48125856 9695307794 "
##print(re.findall("\s(\d{10})\s",n))

##emails="aklen221@gmail.com hdaskhd124@gamil.com qwer.@egmail.com"
##print(re.findall("[\w.@*+_]{1,20}@\w{1,8}\.\w{1,5}",emails))

##s1={"saklen","ansari",True,False,12,20.5,12}
##print(s1,type(s1))
##t1=("saklen","ansari",True,False,12,20.5,12)
##print(t1,type(t1))
##d1={"name":"ali","age":5,"mothername":"tamanna","fathername":"iqbal"}
##print(d1,type(d1))
##print(d1["name"])
##d1["name"]="saqib"
##print(d1["fathername"])
##print("name" in d1)
##print("age" in d1)
##print("roll" in d1)
##
####list1=[10,11,15,16,18,98]
####print(list1[2])
####print(list1.index(15))

##class Student:
##    school_name="SGS"
##    def __init__(self,Name,Class):
##        self.Name=Name
##        self.Class=Class
##    def read(self):
##        print(f"{self.Name} is reading")
##    def __str__(self):
##        return self.name
##a=Student("mujahid",10)  
##s1=Student("maneer",11)
##s2=Student("zubair",12)
##print("Name:",s1.Name,"And Class ",s1.Class)
##print("Name:",s2.Name,"And Class ",s2.Class)
##print(s1.school_name)
##s1.Name="arbaj"
##print(s1.Name)
##s2.read()   
##s1.read()
##class Number:
##    def __init__(self,length,width):
##        self.length=length
##        self.width=width
##    def Squre(self):
##        print(self.length*self.width)
##a=Number(12,10)
##a.Squre()
##class Fruit:
##    def __init__(self,name,color,size,price):
##        self.name=name
##        self.color=color
##        self.size=size
##        self.price=price
##    def change_color(self,new):
##        self.color=new
##f1=Fruit("apple","red",5,150)
##print(f1.color)
##print(f1.name)
##print(f1.color)
##print(f1.size)
##print(f1.price)
##f1.name="banana"
##print(f1.name)
##    
##f1.change_color("blue")
##print(f1.color)
##class Student:
##    school_name="SGS"
##    def __init__(self,n,c):
##        self.name=n
##        self.Class=c
##    def read(self):
##        print(f"{self.name} is reading")
##s1=Student("abs",5)
##print(s1.name)
##print(s1.Class)
##s1.name="ali"
##print(s1.name)
##
##falak=Student("falak",4)
##sadaf=Student("sadaf",2)
##print(falak.name)
##print(falak.Class)
##falak.read()
##print(sadaf.name)
##print(sadaf.Class)
##sadaf.read()
##print(s1,falak,sadaf)
##class Fruit:
##    def __init__(self,name,Color,taste,size):
##        self.name=name
##        self.Color=Color
##        self.taste=taste
##        self.size=size
##
##    def __init__(self,new):
##        self.color=new     
####    @staticmethod
####    def eat():
####        print("fruit is eaten")
##
##f1=Fruit("apple","red","sweet",10)
##f1.color="orenge"
##print(f1.name)
##print(f1.color)
##class A:
##    a="hello"
##    def __init__(self,num1,num2):
##        self.num1=num1
##        self.num2=num2
##    def details(self):
##        print(self.num1,self.num2)
##class B(A):
##    pass
##obj_a=A(12,20)
##obj_a.details()
##print(B.a)
##obj_b=B(25,50)
##obj_b.details()
##class R:
##    def __init__(self,length,width):
##        self.length=length
##        self.width=width
##    def area(self):
##        print(self.length*self.width)
##n=R(12,10)
##n.area()
#regular expression
##import re
##str1="saklen Cry fry dry try Dry cry maneer vasisha"
##print(re.search("cry",str1))
##print(re.findall("cry",str1))
##print(re.findall("[Aa-zZ]ry",str1))
##replace/edit
##str1="saklen Cry fry dry try Dry cry maneer varisha"
##print(re.sub("r","9",str1))
##compile method create a regex pattern object
##str1="saklen Cry fry dry try Dry cry varisha"
##pat1=re.compile("cry")
##print(re.search(pat1,str1))
###\
###\d only digits (number from 1-9)
##str2="98 lk _ - = + % ^ & * $ @ # ! ~ ` / |"
##print(re.findall("\d",str2))
##print("        ")
###\D or [^\d]
##print(re.findall("\D",str2))
##print("    ")
##print(re.findall("\w",str2))
##print(" ")
##print(re.findall("\W",str2))
##finditer
##str1="Saklen Cry fry dry try Dry cry varisha cry try cry"
##print("finditer",list(re.finditer("cry",str1)))
##print("search",re.search("cry",str1))
##print("findall",re.findall("cry",str1))
###dot(.)
##import re
##str3="regex is a smart way 09@"
##print(re.findall(".",str3))
##print(re.search(".",str3))
##print(re.findall(".t",str3))
##print(re.findall("\s\w{2}\s",str3))
##print(re.findall("\w{2,6}",str3))
##nums="9695307794 09478095478 34208979004 7879794548 4709 ;kdl 987 765"
##print(re.findall("\d{10}",nums))
##import re
##num="7550-7666-989769"
##print(re.findall(r"\d{4}-\d{4}-\d{6}",num))
##
##emails="saklen660@gmail.com sajkfll@9978@gmail.com sdkj.as9489@gamil.com"
##print(re.findall(r"[\w.@*&+=-_]{1,20}@\w{1,8}\.\w{1,5}",emails))
#\b
##import re
##str1="try app tapp capp appss appsss"
##print(re.findall(r"\bapp\b",str1))
###quantifier
###(?) zero or one
##print(re.findall(r"apps?",str1))
###one or many (+)
##print(re.findall(r"apps+",str1))
###(*)zero or many
##print(re.findall(r"apps*",str1))
##import copy
##list1=[1,2,3,[4,5]]
##copy_list=copy.copy(list1)
##print(copy_list)
##print(list1)
##copy_list[3][0]=40
##print(list1)
##print(copy_list)
##list1=[1,2,3,[4,5]]
##deep_list=copy.deepcopy(list1)
##deep_list[3][1]=100
##print(list1)
##print(deep_list)
##
##dict1={"a":10,"b":20,"c":{"d":30,"e":40}}
##shallow=copy.copy(dict1)
##deep=copy.deepcopy(dict1)
##dict1["c"]["d"]=300
##dict1["a"]=10
##print("oiginal",dict1)
##print("shallow",shallow)
##print("deep",deep)
# str1="saklen"
# str2="ansari"
# print(str1+str2)
# con=" ".join([str1,str2])
# print(con)

# numm=int(input("Enter Any Number :"))
# if numm==0:
#     print("number is zero")
# elif(numm<0):
#     print("number is negative")
# elif(numm>0):
#     print("number is positive")

#---------------------------------------------------------------------------------------------
#python`s map() built-in function that allows you to process and transform all the items in an
# iterable without using an expicit for loop a technique commonly known as mapping.
#map() is useful when you need to apply a transformation and transform them into a new iterable.
#map function return a map object.
# It takes two arguments a function and an iterable .
##MAP
##WAP to convert a list of temperatures in Celsius to Fahrenheit.
##WAP to extract the first letter of each word in a list of strings.
##WAP to combine corresponding elements of two lists into tuples.
##WAP to replace all vowels in a list of strings with string "v".
'''
list1=[2,4,6,7,8,9,9]
def s(a):
    return a**3
print(list(map(s,list1)))
list2=[3,4,5,6,7,9,70]
print(list(map(lambda a,b:a+b,list1,list2)))

##FILTER

##WAP to Filter a list of strings to keep only those whose length is 4.
##WAP to keep only those elements from a list that are perfect squares.
def check(a):
    if a%2!=0:
        return True
    else:
        False
print(list(filter(check,list1)))
def add(a,b):
    return a+" "+b
f_name=["Md","Mohd","Er","Hafiz"]
l_name=["Saklen","Ibrahim","Mustakim","Iqramul"]
print(list(map(add,f_name,l_name)))
#WAP to convert amount of Transaction to Dollars.
#1 dollar=84 Rs
#1 Rs =1/84 dollar
transaction = [{"type":"debit","amount":1200},
               {"type":"credit","amount":1600},
               {"type":"debit","amount":17500},
               {"type":"credit","amount":19800}]
def dollar(a):
    a["amount"]=a["amount"]/84
    return a
print(list(map(dollar,transaction)))

# Reduce
from functools import reduce
list4=[2,3,4,5]
print(reduce(lambda a,b: a*b,list4))
print(24*5)
print(reduce(lambda a,b:a+b,list4))
#WAP to print factorial of 6 using reduce
print(reduce(lambda a,b:a*b,range(1,6)))
'''
#list Comperehenssion
#Python
'''
list1=[]
for i in "Python":
    list1.append(i)
print(list1)
print([i for i in "python"])
print([i.upper() for i in "python"])
list2=["Saklen","Ayesha","Aarif"]
print([s.upper()for s in list2])
print([len(s)for s in list2])
list3=[1,3,5,6,8,9,23,24,26]
print([i for i in list3 if i%2==0])
print([i for i in list3 if i%2!=0])
#dictinary Comprehenssion
print({i:len(i) for i in list2})
print({len(i):i for i in list2})
dict1={"num1":10,"num2":20,"num3":30}
d1={}
for k,v in dict1.items():
    d1[k]=v*2
print(d1)
print({k:v for k,v in dict1.items()})
print({k:v**2 for k,v in dict1.items()})
'''
#Questions
#1. WPA to convert a list of tempreturesinn celsius to fahrenheit.
def Tempreturs(c):
   return(c * 9/5) + 32
list1=[10,11,13,14,15,17]
##user=int(input("Enter Temperature in Celsius :"))
print(list(map(Tempreturs,list1)))
#2. WAP to extract the first letter of each word in list of strings.
list1=["Saklen","Ayesha","Zulfekar","ayan","Tabrej","Sohel"]
new_list=[]
for i in list1:
    new_list.append(i[0])
print(new_list)
#2.WAP to combine correponding elements of two lists into tuples.
list4=["a","b","c","d","e"]
list5=[10,20,30,40]
print(list(zip(list4,list5)))
#4.WAP to replace all vowels in list of strings with string "k".
vowels="aeiouAEIOU"
for i in range(len(list1)):
    for o in vowels:
        list1[i]=list1[i].replace(o,"k")
print(list1)
#Filter
#question 1.
#WAP to Extract all prime numbers from a list.
##list9=[12,13,14,15,16,171,18,19,10,20]
##num=13
##for i in range(2,num):
##    if num%i==0:
##        print("Not")
##        break
##else:
##    print("Prime")
list10=[12,13,14,15,16,17,18,19,20,21]
n_prime=[]
prime_no=[]
for i in list10:
    for a in range(2,i):
        if i%a==0:
            n_prime.append(i)
            break
    else:
        prime_no.append(i)
            
print("prime no ",prime_no)
print("Not Prime no ",n_prime)

#2 WAP to filter a list of strings to keeps only those whose length is 4.
print(list(filter(lambda a:len(a)==4,list1)))
print("nothing")
list17= [1, 2, 3, 4, 5, 9, 16, 18, 25, 30]
#WAP to keep only those elements from a list that are perfect squares.
print(list(filter(lambda a: any(i*i == a for i in range(1,a+1)),list17)))
#Reduce
#WAP to Calculate the product of all elements in a list.
from functools import reduce
print(reduce(lambda a,b:a*b,list10))
#WAP to Combine a list of strings into a single sentence with spaces.
print(reduce(lambda a,b:a+" "+b,list4))
#list comtehension
#WAP to print a list of the first 10 multiples of 7 using list comprehension.
print([a*7 for a in range(1,11)])
#WAP to print a list of the lengths of each word in a list of strings.
print([len(s) for s in list1])
#WAP to print a list of the squares of all even numbers from 1 to 20 using list comprehension.
print([a**2 for a in range(1,21) if a%2==0])
#Given a list of words ["apple", "banana", "cherry"], create a list with each word reversed.
words=["apple", "banana", "cherry"]
print([a[-1::-1] for a in words])
#WAP to print a dictionary to filter out all key-value pairs of any given dict
#where the value is less than 10 using dictionary comprehension.
dict1={"num1":15,"num2":8,"num3":9,"num4":12,"num5":5}
print({k:v for k,v in dict1.items() if v<10})

#WAP to print a dictionary where the keys are the names of fruits and the values are their lengths
#Using dictionary comprehension.
words=["apple", "banana", "cherry","mango"]
print({k:len(k) for k in words})
#WAP to print a dictionary from any given list whose keys will be the elements and values will be
#the indices of elements.
print({v:k for k,v in enumerate(words)})

#WAP to print a dictionary from two given lists whose keys will be the elements of first list
#and values will be the  elements of second list.
list1=["a","b","c","d"]
list2=[10,20,30,40]
print({a:b for a,b in zip(list1,list2)})





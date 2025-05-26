#Loop
#while loop
##
##while True:
##    print("saklen")
#print number from 1 to 100
##i=1
##while i<=100:
##    print(i)
##    i+=1
##i=100
##while i>=1:
##    print(i)
##    i-=1
##i=1    
##num=int(input("enter any number: "))
##while i<=10:
##    print(i*num)
##    i+=1
##l1=["saklen","zulfekar","tabrej","sohail","saklen"]
##i=0
###s="saklen"
##while i<len(l1):
##    if l1[i]=="saklen":
##        print("foud at index",i)
##    else:
##        print("finding....")
##    i+=1
##i=1
##l1=["saklen","sahbaj","saddam","sarfaraj","meraj"]
##while i<len(l1):
##    if l1[i]=="meraj":
##        print(i)
##        break
##    else:
##        print("finding...")
##    i+=1
##i=1
##while i<=20:
##    if i%2==0:
##        i+=1
##        continue
##    print(i)
##    i+=1    
###FOR LOOP
##nums=[12,13,14,15,16,17]
##ind=0
##x=14
##for el in nums:
##    
##    if el==x:
##        print(ind)
##        break
##    ind+=1
##for o in range(1,5,2):
##    print(o)
##num=4
##i=1
##ad=1
##while i<=num:
##    
##    ad*=i
##    i+=1
##print(ad)
###function
##def Sum(a=3,b=3):
##    add=a+b
##    return add
##print(Sum(6))


##list1=["saklen","manir","ahsan","zubair","sahbaj"]
##def list_len(list1):
##    return len(list1)
##print(list_len(list1))

##list1=["saklen","manir","ahsan","zubair","sahbaj"]
##def s(list):
##    for i in list:
##        print(i,end=" ")
##print(s(list1))
##print()
#num=5
#Function
##def Sum(a,b):
##    return a+b
##print(Sum(10,23))

##def fact_num(num):
##    factorial=1
##    for i in range(1,num+1):
##        factorial*=i
##    return(factorial)
##print(fact_num(5))
##rupees=float(input("Enter The USD "))
##def convert(USD):
##    INR=USD*84
##    return f"{USD} USD is equal to {INR} INR"
##print(convert(rupees))

#Recursion
##def s(n):
##    if (n==0):
##        return
##    print(n)
##    s(n-1)
##s(6)
# write a recursive function frist n natural numbers
##def fact(n):
##    if (n==1 or n==0):
##        return 1
##    return fact(n-1) * n
##print(fact(5))
# write a recursive function to calculate the sum of fist n natural numbers

def s(n):
    if (n==0):
        return 0
    return s(n-1)+n
su=s(5)
print(su)
#write a recursive function to print all elements in a list
def list1(list,idx=0):
    if (idx==len(list)):
        return
    print(list[idx])
    list1(list,idx+1)
names=["python","aarif","hasim","maneer","ekramul"]
list1(names)







    




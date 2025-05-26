''' Interaction is the repeated execution of a process in
loops. Each pass through a loop is called an interation,

it allows automatic handing of multiple items without manual retition.'''
'''Iterables in python are objects that can be looped over or iterated through.Example are list,
tuple,set,range,string etc'''

#ForLoop
''' A for loop allows to repeat a block of code for each items in a collection, such as a list
or string.'''
###print 1 to 10
##for i in range(1,11):
##    print(i)
###print 10 times hello world
##for i in range(1,11):
##    print(i,"hello world")
###print 1,50 even numbers
##for num in range(1,51):
##        if num%2==0:
##            print(num)
###print 50,100 odd numbers
##for num in range(50,100):
##    if num%2!=0:
##        print(num)

###Q1
##''' WAP to seperate even and odd numbers from 0 to 50
##into two lists:even_nums and odd_nums,and then print both listes'''
##even_nums=[]
##odd_nums=[]
##for num in range(0,50):
##    if num%2==0:
##        even_nums.append(num)
##    else:
##        odd_nums.append(num)
##print("even_nums",even_nums)
##print("even_nums",odd_nums)
#Q2
#Q3
'''WAP to seperate integers and strings from a mixed list into two lists:
numbers for integers and strings for strings for strings then print both lists'''
list1=["a",1,"b",2,"c",3,"d",4]
numbers=[]
strings=[]
for i in list1:
    if type(i)==int:
        numbers.append(i)
    elif type(i)==str:
        strings.append(i)
print("numbers",numbers)
print("strings",strings)

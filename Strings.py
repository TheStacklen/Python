#Strings
a="saklen"
b="123"
#length
#The len() function returns the number of elements
#in the string (or list, tuple etc)
print(len(a)) # 6
'''
Indexing:
Indexing refers to accessing
individual elements in a sequence(str,tuple,list)
indexing starts from 0
'''
print("0th index",a[0]) #0th index s
print("1st index",a[1]) #1st index a
print("2nd index",a[2]) #2nd index k
print("5th index",a[5]) #5th index n
str1="wednesday"
#negetive indexing : it starts from -1
print(str1[-1]) # y
print(str1[-2]) #a
print(str1[-9]) #w
'''
slicing:
slicing is used to obtain a portion of a
sequence
syntax:[start_index:end_index]
end_index is exclued
'''
str="hello"
print(str[0:5])#hello
print(str[:5])#hello
print(str[2:])#llo
print(str[0:4])#hell
#[start index:endIndex: step_sise]
print(str[0:len(str)])#hello
print(str[0:len(str):2])#hlo
#we can return a range of characters by using the slice syntax
print(str[0:3])# 'hel' we give range in sq. brackets [start index:end index] end endex is excluded
print(str[:4])#hell. if start index is not given it will start from 0th index
print(str[2:])#llo. if start index is not given it will go upto last character of string
print(str[0:5:2])#hlo.here third number is step size in range
print(str[-4:-2])#el.print character from -4 to -2(i,e from 3 to 5)
#to slice string in reverse order we give -1 as stepsize
print(str[-1:-4:-1])#oll. start from -1, end index is -4
print(str[5:1:-1])# oll. start from 5 , print in reverse order upto 1st index
#"Tuesday" yadseuT
a="Tuesday"
print(a[-1:-8:-1])#yadseuT
print(a[7::-1])#yadseuY
print(a[4:])# day
print(a[-3:])#day
print(a[-3:len(a)])#day
print(a[0:3])#tue
print(a[1:4])#ues
#common string methods
#upper(): converts string to uppercase
s="saklen"
print(s.upper())#SAKLEN
#lower():converts string to lowercase
k="SAKLEN"
print(k.lower())#saklen





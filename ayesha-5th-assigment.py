##1. (2 Marks)
####Write a Python program that extracts all dates in the format "dd-mm-yyyy" (e.g., 12-08-2023) from a given text
####and prints only the day and month, excluding the year.
##import re
##text = "my birth date is 14-09-2005 and today is 12-07-2024 python full stack batch statrts from 25-09-2024"
##print(re.findall("(\d{1,2})-(\d{1,2})-(\d{1,2})", text))
##for i in re.finditer("(\d{1,2})-(\d{1,2})-(\d{1,2})", text):
##    print("day",i.group(1))
##    print("month",i.group(2))


##2. (2 Marks)
##Write a Python program that searches for the first occurrence of the phrase "Python is fun" in a given
##text and prints the start and end indices of the match.
import re
text2 = " belive me python is fun learn python because python is fun and code in python is easy "
matchh = re.search("python is fun", text2)
print(matchh.start())
print(matchh.end())


##3. (2 Marks)
##Write a Python program that takes an input from the user and checks if the input is a valid employee ID.
##The employee ID format is "EMP" followed by 2 to 5 digits (e.g., EMP23, EMP12345).
empid = input("enter employee id:")
if re.search("EMP\d{2,5}", empid):
    print("it is valid employee ID")
else:
    print("invalid employee ID")


##4. (3 Marks)
##a) Write a Python program that searches for the word "student" in both its singular and plural forms
##(student/students) and prints the number of matches. The search should NOT be case-sensitive.
text3 = "student students teacher teach studentss STUDENTS and STUDENT Student"
matchh = re.findall("(students?)",text3.lower())
print(len(matchh))
##b) Write the above program for a case-sensitive search.
re.findall("(students?)",text3)

##5. (3 Marks)
##Write a Python program that searches in a text file for all occurrences of a user-provided word and prints
##the start indices of all matches.
text_file = open("textfile.txt","r")
word = input("enter a word for search")
for i in re.finditer(word,text_file.read()):
    print(i.start())

text_file.close()
print(text_file.closed)

##6. (4 Marks)
##Write a Python program that:
##Prints "Starts with a letter" if the given text starts with a letter.
##Prints "Ends with a letter" if the given text ends with a letter.
##Prints both messages if both cases are true.
##Prints "Neither starts nor ends with a letter" if neither case is true.
text4 = input("enter a text here:")
if re.search("[a-zA-z]", text4[0])  and re.search("[a-zA-z]",text4[-1]) :
    print("Starts with a letter and Ends with a letter")
elif re.search("[a-zA-z]", text4[0]):
    print("Starts with a letter")
elif re.search("[a-zA-z]",text4[-1]):
    print("Ends with a letter")
else:
    print("Neither starts nor ends with a letter")
    
##7
##(4 Marks)
##Write a Python program which reads a text file and makes the following changes:  
##a) Removes all the special characters from the text.
text_file = open("textfile.txt","r")
print(text_file.read())
text_file.close()
text_file =  open("textfile.txt","r")         
clean = re.sub("[^A-Za-z0-9\s]","", text_file.read())
print(clean)
text_file.close()
write_file = open("textfile.txt", "w")
write_file.write(clean)
write_file.close()



####b) Removes all the new line characters from the text
text_file = open("textfile.txt", "r")
clean2 = re.sub("\n","", text_file.read())
print(clean2)
text_file.close()
text = open("textfile.txt", "w")
text.write(clean2)
text.close()

##c) Removes all the words which have length two or less
text_file = open("textfile.txt","r")
remove = re.sub("\w{1,2}\s"," ", text_file.read())
print(remove)
text_file.close()
chnge = open("textfile.txt","w")
chnge.write(remove)
chnge.close()


##d) Replaces all the email Ids in the text with string -'EmailID'
text_file = open("textfile.txt","r")
emails = re.sub("[\w.@*&+-]{1,20}@gmail\.com","EmailID", text_file.read())
print(emails)
text_file.close()
replace = open("textfile.txt","w")
replace.write(emails)
replace.close()


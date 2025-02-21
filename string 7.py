 # strings - collection of characters enclosed with doble codes
str1="vishnu"
print(str1)
print(type(str1))

new="im a  python developer"
print(new[5])
print(new[4])
print(new[-5])

#slicing
print(new[3:10])
print(new[-4:-1])
 


name1="vishnu"
name2="vardhan"
con=name1+ " " +name2
print(con)
print(con*5)

# string methods
# 1.len() -used to find the length of string
student="maheshreddy"
print(len(student))

# 2.upper()- converts the string to upper case
student_name="chatrapathi shivaji"
print(student_name.upper())

# 3. lower()- converts the string to lower case
print(student_name.lower())

# 4.count()- count how many times the word is repeated
print(student_name.count("i"))

#5 strip()- it will remove the white spaces in string at the starting and ending 
employee=" technicaldepartment    "
strp=employee.strip()
print(strp)


#split() -used to split the string into list
id="we are students who is the future of the country"
print(id.split())

#join()- converts the list into string
id=['we', 'are', 'students', 'who', 'is', 'the', 'future', 'of', 'the', 'country']
print(" ".join(id))
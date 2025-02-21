#string is a collection of characters enclosed with single quodes, double quodes or triple quodes

#len() _ used to find the length of a string
name="vishnu"
print(name)
print(len(name))

#upper()- to convert the string to upper case
userelement="this is vishnu vardhan"
print(userelement.upper())

#lower() - converts the string to lower case
id="vishnu vardhan reddy"
print(userelement.lower())

# count() - used to find how many times a word is going to repeat
stu="kumarvarma"
name=stu.count("a")
print(name)

#split()- used to split the string into list
id ="we are students from teks academy"
print(id.split())

#strip()- removes all the white spaces from starting and ending
userid="    computerscience and engineering      "
print(userid.strip())

#join() - converts the list into string
user_element=["we","are ","good","at","programming"]
print(" ".join(user_element))
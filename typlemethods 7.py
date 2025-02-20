names=["sai","manish","mahesh","madhu","manu"]
names2=["vinod","vishnu","vamsi","vaibhav"]


#append- adds an element at the end of the list
names.append("vishnu")
print(names)

# extend - merges to elements
names.extend(names2)
print(names)

#pop - deletes an element at the end of the lists
names.pop()
print(names)

#count- used to count how many times the  string in the list is repeated
print(names.count("sai"))
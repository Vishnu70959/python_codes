# lists in python are mainly used to store multiple items in a data.
# list are used with square braces and operations are performed in it
# we can assign any data type in lists
# the data between words inside lists are seperated by comma(,)


number=[1,2,3,4,5,7,6,9,8]
print(type(number))


names=["vishnu","charan","durga","naresh","prasadh"]
print(names)
print(type(names))


university=["srm","kl","jntuh","ou","au"]
print(university)
print(university[4])

# indexing in python are mainly used to represent the index position of lists 
# in python indexing is mainly from positive side and negative side
# positive index starts from 0 to ♾️ and negative index starts from -1 to -♾️

# index 1 example
names=["vishnu","charan","durga","naresh","prasadh"]
print(names[2])
print(names[2]==5)

print(names[1:3])
print(names[-3:-1])


#index 2 example
nums=[2,4,56,67,45,777,88,18]
print(nums[5])
print(nums[2]==6767) #here == means "exactly equal it assigns the value"
print(nums[2:5])
print(nums[2:4:5])
print(nums[-5:-4])
print(nums[-3])

#for updating values in list this is used
nums[2]=67676
print(nums)


#index example 3
roles=["developer","tester","telecaller","nonvoiceprocess","salesagent"]
roles[3]="fresher"
print(roles)

print(roles[-1])
print(roles[-3:-2])

#list example 4
fruits=["apple","grapes","mango","orange","banana"]
for fruit in fruits:
    print(fruit)

fruits[1]="apple"  # for replacing elements in lists
print(fruits)
print(fruits[1:4])
print(fruits[-4:-5])
print(fruits[-3:-2])
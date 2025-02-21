
#concat for adding two strings
#example1
name="vishnu"
name2="vardhan"
fullname=name+ " " +name2
print(fullname)


#example 2
numbers=[1,2,3,4,5]
numbers2=[9,8,7,6]
result=numbers+numbers2
print(result)
print(result[-2])


#new example 3
company1=["tcs","wipro","hexaware","mindtree"]
company2=["fastpix","arena","amazon","google"]
newcompany=company1+company2
print(newcompany)
print(type(company1))


#repacing elements in the list
company1[2]="google"
print(company1)

#new example 4
vishnu=["kumarsai","manisharma","hariprasad","surendra"]
vishnu[2]="harsha"
print(vishnu)
vishnu2=["saikrishna","harish","maniprasad","sathya"]

new=vishnu+vishnu2
print(new)
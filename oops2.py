from oops1 import employee

#create attribte outside the class
emp1 = employee()
emp1.name = "sam"
print(emp1.name)
#print(emp1.__topsecret) ## return error if we want to access private attributes

#emp1.get_key()
#emp1.set_key(112)
#emp1.get_key()

print(emp1.emp_id)
emp2 = employee()
print(emp2.emp_id)
emp3 = employee()
print(emp3.emp_id)
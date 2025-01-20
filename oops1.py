# creating a first class
class employee:
    def __init__(self):
        print("this class is being executed")
        self.id = 123
        self.dept = "IT"
        self.sal = 50,000
    
    def travel(self,destination):
        print("the employer is travelling to {destination}")
        
        
#creating first object
sam = employee()
sam.travel("hyderabad")
print(type(sam))
str = "hey"
print(type(str))
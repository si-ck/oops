# creating a first class


class employee:
    
    __user_id = 0   #  "static"  hidden value
    
    def __init__(self):
        print("this class is being executed")
        self.__topsecret = "confidentila ifo like private key"
        self.emp_id = employee.__user_id
        employee.__user_id +=1
        self.dept = "IT"
        self.sal = 50,000
    
    
    #getter
    def get_key(self):
        return self.__topsecret
    #setter
    def set_key(self,key):
        self.__topsecret = key
    
    def travel(self,destination):
        print("the employer is travelling to {destination}")
        
    
        
#creating first object
#sam = employee()
#sam.travel("hyderabad")
#print(type(sam))
#str = "hey"
#print(type(str))
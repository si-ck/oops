class blogdiary :
    def __init__(self):
        self.username = ""
        self.password = ""
        self.login = False  
        self.menu()
    def menu(self):
        user_input=input("""Welcome to blogdiary
            press 1 to signup
            press 2 to login
            press 3 to write a post
            press 4 to msg a friends
            anyother to exit
            
            
            ->""")
        
        if user_input == "1":
            self.signup()
        if user_input == "2":
            self.signin()
        if user_input == "3":
            self.post()
        if user_input == "4":
            self.convo()
        else :
            pass
        
       
        
    def signup(self):
        userN=input("create a username -> ")
        userP=input("create a password -> ") 
        self.username = userN
        self.password = userP
        print("you have successfullu signed up\n please login to blogdiary\n")
        self.menu() 
        
        
    def signin(self):
        uName = input("enter username -> ")
        upass = input("enter the password -> ")   
        if uName == self.username and upass == self.password:
            self.login = True
            print("uve successfully logged into blogdiary\n")
            self.menu()
        else :
            print("unmatched credentials")
  
    def post (self):
        if self.login == True:
            post = input("write a post\n-> ")
            print(f"your following post has been successfully registered-> {post}\n")
            self.menu()
        else:
            print("make sure ur succesfully logged into blogdiary\n")
            self.menu()
            
            
    def convo (self):
        if self.login == True:
            txt = input("enter the message-> ") 
            frnd = input("to whom is this mesge written for-> ") 
            print(f"your message has been sent to-> {frnd}")      
        else:
            print("make sure ur succesfully logged into blogdiary\n")    
user1 = blogdiary()            
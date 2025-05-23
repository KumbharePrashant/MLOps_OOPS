class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()
    
    def menu(self):
        user_input = int(input(""" Welcome to Chatbook | How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to Signin
                           3. Press 3 to send a Post
                           4. Press 4 to send a Message
                           5. Press any key to Exit\n"""))
        
        if user_input == 1:
            self.sign_up()
        elif user_input ==2:
            self.sign_in()
        elif user_input == 3:
            self.send_post()
        elif user_input ==4:
            self.send_message()
        else:
            exit()
    
    def sign_up(self):
        email = input("Enter your email here --> ")
        pwd= input("Enter your password here --> ")
        self.username = email
        self.password = pwd
        print("You have signed up successfully!")
        print("\n")
        self.menu()
    
    def sign_in(self):
        if self.username == "" and self.password == "":
            print("Please sign up  first by pressing 1 in the main menu")
        else:
            uname = input("Enter yout username here --> ")
            pwd = input("Enter your password here --> ")
            if self.username == uname and self.password == pwd:
                print("You have signed in successfully!")
                self.loggedin = True
            else:
                print("Enter the correct creditials!")
        print("\n")
        self.menu()

    def send_post(self):
        if self.loggedin == True:
            txt = input("Enter your post here --> ")
            print(f"Your following post is now live - {txt}")
        else:
            print("You need to sign in first to post something")
            
        print("\n")
        self.menu()
    
    def send_message(self):
        if self.loggedin == True:
            txt = input("Enter your message here --> ")
            whom = input("Enter username to whom you want to send message -->")
            print(f"Your message {txt} is successfully send to {whom}")
        else:
            print("You need to sign in first to message someone")
            
        print("\n")
        self.menu()
    

user1 = chatbook()

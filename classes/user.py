class User:
    def __init__(self, user_id, user_name, user_email):
        self.user_id = user_id
        self.user_name = user_name
        self.user_email = user_email
    
    def register(self):
        print("\n===== USER REGISTRATION =====")
        print(f"User ID   : {self.user_id}")
        print(f"Name      : {self.user_name}")
        print(f"Email     : {self.user_email}")
        print("Status    : Registration Successful")
        print("==================================")

    def login(self):
        print("User logged in.")

    def logout(self):
        print("User logged out.")

    def view_profile(self):
        print("\n===== USER PROFILE =====")
        print("User ID :", self.user_id)
        print("Name    :", self.user_name)
        print("Email   :", self.user_email)
        print("========================")
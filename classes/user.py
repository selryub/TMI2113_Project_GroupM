class User:
    def __init__(self, user_id, user_name, user_email):
        self.user_id = user_id
        self.user_name = user_name
        self.user_email = user_email

    def login(self):
        print("User logged in.")

    def logout(self):
        print("User logged out.")

    def view_profile(self):
        print("User Profile")
        print("Name:", self.user_name)
        print("Email:", self.user_email)
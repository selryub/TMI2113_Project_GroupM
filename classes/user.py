class User:
    def __init__(self, user_id, user_name, user_email, password):
        self.user_id = user_id
        self.user_name = user_name
        self.user_email = user_email
        self.password = password
        self.is_verified = False

    def register(self):
        print("User registered successfully.")

    def verify_email(self):
        self.is_verified = True
        print("Email verified.")

    def reset_password(self, new_password):
        self.password = new_password
        print("Password reset successful.")

    def logout(self):
        print("User logged out.")

    def view_profile(self):
        print("User Profile")
        print("Name:", self.user_name)
        print("Email:", self.user_email)
class User:
    def __init__(self, user_id, user_name, user_email, user_password):
        self.userID = user_id
        self.userName = user_name
        self.userEmail = user_email
        self.userPassword = user_password
        self.userVerificationStatus = False

    def register(self):
        print("User registered successfully.")

    def login(self):
        print("User logged in.")

    def logout(self):
        print("User logged out.")

    def viewProfile(self):
        print("User Profile")
        print("Name:", self.userName)
        print("Email:", self.userEmail)

    def verifyEmail(self):
        self.userVerificationStatus = True
        print("Email verified.")

    def resetPassword(self, new_password):
        self.userPassword = new_password
        print("Password reset successful.")
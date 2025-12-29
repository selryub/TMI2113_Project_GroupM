from classes.user import User


# store a temporary test user (simulated database)
current_user = None


def userMenu():
    global current_user

    while True:
        print("\n========== USER MENU ==========")
        print("1. Register")
        print("2. Login")
        print("3. View Profile")
        print("4. Verify Email")
        print("5. Reset Password")
        print("6. Logout")
        print("7. Back to Main Menu")
        print("================================")

        choice = input("Select option: ")

        # ---------------- REGISTER ----------------
        if choice == "1":
            print("\n--- Register New User ---")
            user_id = input("Enter User ID: ")
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            password = input("Enter Password: ")

            current_user = User(user_id, name, email, password)
            current_user.register()

        # ---------------- LOGIN ----------------
        elif choice == "2":
            if current_user is None:
                print("\nNo user registered yet. Please register first.")
            else:
                current_user.login()

        # ---------------- VIEW PROFILE ----------------
        elif choice == "3":
            if current_user is None:
                print("\nNo user found. Please register first.")
            else:
                current_user.view_profile()

        # -------- VERIFY EMAIL --------
        elif choice == "4":
            if current_user is None:
                print("\nNo user found.")
            else:
                current_user.verifyEmail()

        # -------- RESET PASSWORD --------
        elif choice == "5":
            if current_user is None:
                print("\nNo user found.")
            else:
                new_password = input("Enter new password: ")
                current_user.resetPassword(new_password)

        # ---------------- LOGOUT ----------------
        elif choice == "6":
            if current_user is None:
                print("\nNo user logged in.")
            else:
                current_user.logout()
                current_user = None

        # ---------------- EXIT TO MAIN ----------------
        elif choice == "7":
            print("\nReturning to Main Menu...")
            break

        else:
            print("Invalid option. Try again.")

        input("\nPress Enter to continue...")
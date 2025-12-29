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
        print("4. Logout")
        print("5. Back to Main Menu")
        print("================================")

        choice = input("Select option: ")

        # ---------------- REGISTER ----------------
        if choice == "1":
            print("\n--- Register New User ---")
            user_id = input("Enter User ID: ")
            name = input("Enter Name: ")
            email = input("Enter Email: ")

            current_user = User(user_id, name, email)
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

        # ---------------- LOGOUT ----------------
        elif choice == "4":
            if current_user is None:
                print("\nNo user logged in.")
            else:
                current_user.logout()
                current_user = None

        # ---------------- EXIT TO MAIN ----------------
        elif choice == "5":
            print("\nReturning to Main Menu...")
            break

        else:
            print("Invalid option. Try again.")

        input("\nPress Enter to continue...")

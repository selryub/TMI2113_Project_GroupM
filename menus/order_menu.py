def userMenu():
    while True:
        print("\n===== USER MENU =====")
        print("1. Login")
        print("2. Register")
        print("3. Back to Main Menu")

        choice = input("Select option: ")

        if choice == "1":
            print("Login selected (stub)")
        elif choice == "2":
            print("Register selected (stub)")
        elif choice == "3":
            break
        else:
            print("Invalid option.")

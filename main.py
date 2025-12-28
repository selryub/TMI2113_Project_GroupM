from menus.user_menu import userMenu
from menus.buyer_menu import buyerMenu
from menus.coordinator_menu import coordinatorMenu
from menus.farmer_menu import farmerMenu
from menus.order_menu import orderMenu
from menus.delivery_menu import deliveryMenu

def mainMenu():
    while True:
        print("\n===== SYSTEM MAIN MENU =====")
        print("1. User Menu")
        print("2. Buyer Menu")
        print("3. Coordinator Menu")
        print("4. Farmer Menu")
        print("5. Order Menu")
        print("6. Delivery Menu")
        print("7. Exit System")

        choice = input("Select option: ")

        if choice == "1":
            userMenu()
        elif choice == "2":
            buyerMenu()
        elif choice == "3":
            coordinatorMenu()
        elif choice == "4":
            farmerMenu()
        elif choice == "5":
            orderMenu()
        elif choice == "6":
            deliveryMenu()
        elif choice == "7":
            print("Exiting system...")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    mainMenu()


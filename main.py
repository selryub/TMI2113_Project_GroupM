from menus.user_menu import userMenu
from menus.buyer_menu import buyerMenu
from menus.village_coordinator_menu import villageCoordinatorMenu 
from menus.farmer_menu import farmerMenu
from menus.produce_menu import produceMenu
from menus.order_menu import orderMenu
from menus.delivery_trip_menu import deliveryTripMenu
from menus.community_driver_menu import communityDriverMenu

def mainMenu():
    while True:
        print("\n===== SYSTEM MAIN MENU =====")
        print("1. User Menu")
        print("2. Buyer Menu")
        print("3. Coordinator Menu")
        print("4. Farmer Menu")
        print("5. Produce Menu")
        print("6. Order Menu")
        print("7. Delivery Trip Menu")
        print("8. Community Driver Menu")
        print("9. Exit")

        choice = input("Select option: ")

        if choice == "1":
            userMenu()
        elif choice == "2":
            buyerMenu()
        elif choice == "3":
            villageCoordinatorMenu()
        elif choice == "4":
            farmerMenu()
        elif choice == "5":
            produceMenu()
        elif choice == "6":
            orderMenu()
        elif choice == "7":
            deliveryTripMenu()
        elif choice == "8":
            communityDriverMenu()
        elif choice == "9":
            print("Exiting system...")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    mainMenu()


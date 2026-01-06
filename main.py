from classes.community_driver import communityDriver
from classes.delivery_trip import deliveryTrip
from classes.village_coordinator import VillageCoordinator

from menus.user_menu import userMenu
from menus.buyer_menu import buyer_menu
from menus.village_coordinator_menu import villageCoordinatorMenu 
from menus.farmer_menu import farmerMenu
from menus.produce_menu import produceMenu
from menus.order_menu import orderMenu
from menus.community_driver_menu import communityDriverMenu
from menus.delivery_trip_menu import deliveryTripMenu


drivers = {
    "D01": communityDriver("D01", "Aiman", "Motorcycle", "0123456789"),
    "D02": communityDriver("D02", "Liang", "Van", "0132188576")
}

trips = {
    "T01": deliveryTrip("T01", 12),
    "T02": deliveryTrip("T02", 20)
}

orders = {
    "O01": "Order#01",
    "O02": "Order#02"
}

produce_list = []

def mainMenu():
    while True:
        print("\n===== SYSTEM MAIN MENU =====")
        print("1. User Menu")
        print("2. Buyer Menu")
        print("3. Farmer Menu")
        print("4. Produce Menu")
        print("5. Order Menu")
        print("6. Village Coordinator Menu")
        print("7. Community Driver Menu")
        print("8. Delivery Trip Menu")
        print("9. Exit")

        choice = input("Select option: ")

        if choice == "1":
            userMenu()
        elif choice == "2":
            buyer_menu()
        elif choice == "3":
            farmerMenu()
        elif choice == "4":
            produceMenu(produce_list)
        elif choice == "5":
            orderMenu()
        elif choice == "6":
            villageCoordinatorMenu()
        elif choice == "7":
            communityDriverMenu(drivers, trips)
        elif choice == "8":
            deliveryTripMenu(trips, drivers, orders)
        elif choice == "9":
            print("Exiting system...")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    mainMenu()
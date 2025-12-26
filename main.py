from menus.user_menu import userMenu
from menus.delivery_menu import deliveryMenu
from menus.coordinator_menu import coordinatorMenu
from menus.buyer_menu import buyerMenu
from menus.farmer_menu import farmerMenu

def main():

    while True:
        role = userMenu()

        if role == "Community Driver":
            deliveryMenu()

        elif role == "Village Coordinator":
            coordinatorMenu()
        
        elif role == "Buyer":
            buyerMenu()
        
        elif role == "Farmer":
            farmerMenu()
        
        else:
            print("\nExiting the system...")
            break

if __name__ == "__main__":
    main()
    
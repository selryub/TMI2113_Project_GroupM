from classes.buyer import Buyer

def show_buyer_menu():
    print("\n==============================")
    print("        BUYER MENU            ")
    print("==============================")
    print("1. Browse Produce Catalog")
    print("2. Place Order")
    print("3. View Orders")
    print("0. Logout")


def buyerMenu():
    buyer = Buyer(
        user_id=1,
        user_name="Ashley",
        user_email="ashley88@email.com",
        delivery_address="Kuching",
        payment_method="Cash"
    )

    buyer.login()

    while True:
        show_buyer_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            buyer.browse_produce()
        elif choice == "2":
            buyer.place_order()
        elif choice == "3":
            buyer.view_orders()
        elif choice == "0":
            buyer.logout()
            break
        else:
            print("Invalid choice. Please try again.")
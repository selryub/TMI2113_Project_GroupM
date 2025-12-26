from classes.buyer import Buyer


def show_buyer_menu():
    print("\n==============================")
    print("        BUYER MENU            ")
    print("==============================")
    print("1. Browse Produce Catalog")
    print("2. Place Order")
    print("3. View Orders")
    print("0. Logout")


def buyer_menu():
    """
    Buyer menu flow 
    """

    # Demo buyer (temporary)
    buyer = Buyer(
        user_id=1,
        user_name="Ali",
        user_email="ali@email.com",
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

from menus.buyer_menu import buyer_menu


def main():
    buyer_menu()


if __name__ == "__main__":
    main()
def deliveryMenu():

    while True:
        print("\n===== Delivery Menu =====")
        print("1. Assign Delivery Trip")
        print("2. Update Delivery Status")
        print("3. View Trip Details")
        print("4. View Delivery Logs")
        print("5. Add Order to Trip")
        print("6. Calculate Cost")
        print("7. Exit menu")

        choice = input("Choose option: ")

        if choice == "7":
            print("Returning to User Menu...")
            break

    
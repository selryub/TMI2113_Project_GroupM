from classes.farmer import Farmer
from classes.produce import Produce

def farmer_menu():
    # Create a sample farmer object
    farmer = Farmer(1, "John Doe", "john@email.com", "password123", "Sunny Farm", "Kuching")

    while True:
        print("\n===== FARMER MENU =====")
        print("1. Supply Produce")
        print("2. Update Produce Details")
        print("3. View Settlement Statement")
        print("4. Review Delivery Records")
        print("5. View Profile")
        print("0. Back to Main Menu")

        choice = input("Select option: ")

        if choice == "1":
            pid = input("Produce ID: ")
            pname = input("Produce Name: ")
            category = input("Category: ")
            grade = input("Grade: ")
            weight = float(input("Weight (kg): "))
            price = float(input("Price per kg: "))
            produce = Produce(pid, pname, category, grade, weight, price)
            farmer.supply_produce(produce)

        elif choice == "2":
            pid = input("Enter Produce ID to update: ")
            weight = input("Enter new weight (leave blank to skip): ")
            grade = input("Enter new grade (leave blank to skip): ")
            farmer.update_produce_details(
                pid,
                weight=float(weight) if weight else None,
                grade=grade if grade else None
            )

        elif choice == "3":
            farmer.view_settlement_statement()

        elif choice == "4":
            farmer.review_delivery_records()

        elif choice == "5":
            farmer.view_profile()  # Polymorphism - Override

        elif choice == "0":
            break

        else:
            print("Invalid option.")

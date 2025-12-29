from classes.farmer import Farmer
from classes.produce import Produce

def farmerMenu():
    farmer = Farmer(1, "John Doe", "john@email.com", "Sunny Farm", "Kuching")

    while True:
        print("\n===== FARMER MENU =====")
        print("1. Supply Produce")
        print("2. Update Produce Details")
        print("3. View Settlement Statement")
        print("4. Review Delivery Records")
        print("5. Back to Main Menu")

        choice = input("Select option: ")

        if choice == "1":
            pid = input("Produce ID: ")
            pname = input("Produce Name: ")
            category = input("Category: ")
            grade = input("Grade: ")
            weight = float(input("Weight (kg): "))
            price = float(input("Price per kg: "))
            produce = Produce(pid, pname, category, grade, weight, price)
            farmer.supplyProduce(produce)

        elif choice == "2":
            pid = input("Enter Produce ID to update: ")
            weight = input("Enter new weight (leave blank to skip): ")
            grade = input("Enter new grade (leave blank to skip): ")
            farmer.updateProduceDetails(
                pid,
                weight=float(weight) if weight else None,
                grade=grade if grade else None
            )

        elif choice == "3":
            farmer.viewSettlementStatement()

        elif choice == "4":
            farmer.reviewDeliveryRecords()

        elif choice == "5":
            break

        else:
            print("Invalid option.")
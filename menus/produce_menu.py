from classes.produce import Produce

def produceMenu():
    produce_list = []

    while True:
        print("\n===== PRODUCE MENU =====")
        print("1. Add Produce")
        print("2. Update Produce Weight")
        print("3. Update Produce Grade")
        print("4. Update Produce Price")
        print("5. View Produce Details")
        print("0. Back to Main Menu")

        choice = input("Select option: ")

        if choice == "1":
            pid = input("Enter Produce ID: ")
            pname = input("Enter Produce Name: ")
            category = input("Enter Category: ")
            grade = input("Enter Grade: ")
            weight = float(input("Enter Weight (kg): "))
            price = float(input("Enter Price per kg: "))
            produce = Produce(pid, pname, category, grade, weight, price)
            produce_list.append(produce)
            print(f"✔ Produce {pname} added.")

        elif choice == "2":
            pid = input("Enter Produce ID to update weight: ")
            new_weight = float(input("Enter new weight: "))
            for p in produce_list:
                if p.getProduceDetails()["id"] == pid:
                    p.updateWeight(new_weight)
                    break
            else:
                print("Produce not found.")

        elif choice == "3":
            pid = input("Enter Produce ID to update grade: ")
            new_grade = input("Enter new grade: ")
            for p in produce_list:
                if p.getProduceDetails()["id"] == pid:
                    p.updateGrade(new_grade)
                    break
            else:
                print("Produce not found.")

        elif choice == "4":
            pid = input("Enter Produce ID to update price: ")
            new_price = float(input("Enter new price per kg: "))
            for p in produce_list:
                if p.getProduceDetails()["id"] == pid:
                    p.updatePrice(new_price)
                    break
            else:
                print("Produce not found.")

        elif choice == "5":
            for p in produce_list:
                print(p.getProduceDetails())

        elif choice == "0":
            break
        else:
            print("Invalid option.")
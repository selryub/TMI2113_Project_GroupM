from classes.produce import Produce

def produceMenu(produce_list):
    while True:
        print("\n===== PRODUCE MENU =====")
        print("1. Add Produce")
        print("2. Update Produce Weight")
        print("3. Update Produce Grade")
        print("4. Update Produce Price")
        print("5. Check Availability")
        print("6. View Produce Details")
        print("0. Back to Main Menu")

        choice = input("Select option: ")

        if choice == "1":  
            print("\n--- Add New Produce ---")
            pid = input("Enter Produce ID: ")
            pname = input("Enter Produce Name: ")
            category = input("Enter Category: ")
            grade = input("Enter Grade: ")
            weight = float(input("Enter Weight (kg): "))
            price = float(input("Enter Price per kg: "))
            
            produce = Produce(pid, pname, category, grade, weight, price)
            produce_list.append(produce)
            print(f"Produce '{pname}' added successfully.")

        elif choice == "2":  
            pid = input("Enter Produce ID to update weight: ")
            new_weight = float(input("Enter new weight (kg): "))
            found = False
            for p in produce_list:
                if p.getProduceDetails()["id"] == pid:
                    p.updateWeight(new_weight)
                    found = True
                    break
            if not found:
                print("Produce not found.")

        elif choice == "3":  
            pid = input("Enter Produce ID to update grade: ")
            new_grade = input("Enter new grade: ")
            found = False
            for p in produce_list:
                if p.getProduceDetails()["id"] == pid:
                    p.updateGrade(new_grade)
                    found = True
                    break
            if not found:
                print("Produce not found.")

        elif choice == "4":  
            pid = input("Enter Produce ID to update price: ")
            new_price = float(input("Enter new price per kg: "))
            found = False
            for p in produce_list:
                if p.getProduceDetails()["id"] == pid:
                    p.updatePrice(new_price)
                    found = True
                    break
            if not found:
                print("Produce not found.")

        elif choice == "5":  
            pid = input("Enter Produce ID to check availability: ")
            found = False
            for p in produce_list:
                if p.getProduceDetails()["id"] == pid:
                    availability_status = "Available" if p.checkAvailability() else "Not Available"
                    print(f"Produce availability: {availability_status}")
                    found = True
                    break
            if not found:
                print("Produce not found.")

        elif choice == "6":  
            pid = input("Enter Produce ID to view details: ")
            found = False
            for p in produce_list:
                if p.getProduceDetails()["id"] == pid:
                    print(p.viewProduceDetails())  
                    found = True
                    break
            if not found:
                print("Produce not found.")

        elif choice == "0":  
            break

        else:
            print("Invalid option. Please try again.")




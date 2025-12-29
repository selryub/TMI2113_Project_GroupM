def deliveryLogMenu(trips):
    while True:
        print("\n===== DeliveryLog Sub-Menu =====")
        print("1. Add Entry")
        print("2. Display Log")
        print("3. Format Log")
        print("4. Summarize Action")
        print("5. View Logs")
        print("6. Back to Main Menu")
        
        choice = input("Select: ").strip()
        tripID = input("Enter Trip ID: ").strip()
        if tripID not in trips:
            print("Trip not found.")
            continue
        log = trips[tripID]._DeliveryTrip__logs  # Assuming log is an attribute
        
        if choice == "1":
            action = input("Enter action: ").strip()
            userID = input("Enter User ID: ").strip()
            log.addEntry(action, userID)
        elif choice == "2":
            log.displayLog()
        elif choice == "3":
            log.formatLog()
        elif choice == "4":
            log.summarizeAction()
        elif choice == "5":
            log.viewLogs()
        elif choice == "6":
            break
        else:
            print("Invalid.")
        
        input("Press Enter...")
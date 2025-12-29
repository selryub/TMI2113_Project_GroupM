from classes.order import Order

def orderMenu():
    orders = []
    
    while True:
        print("\n===== ORDER MENU =====")
        print("1. Create New Order")
        print("2. Calculate Order Total")
        print("3. Calculate Total with Discount")
        print("4. Update Order Status")
        print("5. View Order Details")
        print("6. View All Orders")
        print("7. Back to Main Menu")
        
        choice = input("Select option: ")
        
        if choice == "1":
            orderID = input("Enter Order ID: ")
            buyerID = input("Enter Buyer ID: ")
            produceID = input("Enter Produce ID: ")
            
            order = Order(orderID, buyerID, produceID)
            
            quantity = int(input("Enter Quantity: "))
            order.setQuantity(quantity)
            
            orders.append(order)
            print(f"Order {orderID} created successfully")
        
        elif choice == "2":
            if not orders:
                print("No orders available.")
                continue
            
            orderID = input("Enter Order ID: ")
            found = False
            
            for order in orders:
                if order.getOrderID() == orderID:
                    price = float(input("Enter price per unit: "))
                    order.calculateTotal(price)
                    found = True
                    break
            
            if not found:
                print("Order not found.")
        
        elif choice == "3":
            if not orders:
                print("No orders available.")
                continue
            
            orderID = input("Enter Order ID: ")
            found = False
            
            for order in orders:
                if order.getOrderID() == orderID:
                    price = float(input("Enter price per unit: "))
                    quantity = int(input("Enter quantity: "))
                    discount = float(input("Enter discount percentage: "))
                    order.calculateTotalWithDiscount(price, quantity, discount)
                    found = True
                    break
            
            if not found:
                print("Order not found.")
        
        elif choice == "4":
            if not orders:
                print("No orders available.")
                continue
            
            orderID = input("Enter Order ID: ")
            found = False
            
            for order in orders:
                if order.getOrderID() == orderID:
                    newStatus = input("Enter new status (Pending/Verified/Approved/Delivered): ")
                    notes = input("Enter notes (optional): ")
                    order.updateStatus(newStatus, notes)
                    found = True
                    break
            
            if not found:
                print("Order not found.")
        
        elif choice == "5":
            if not orders:
                print("No orders available.")
                continue
            
            orderID = input("Enter Order ID: ")
            found = False
            
            for order in orders:
                if order.getOrderID() == orderID:
                    order.viewOrderDetails()
                    found = True
                    break
            
            if not found:
                print("Order not found.")
        
        elif choice == "6":
            if not orders:
                print("No orders available.")
            else:
                print("\n===== All Orders =====")
                for order in orders:
                    print(f"Order ID: {order.getOrderID()} | Status: {order.getStatus()} | Total: RM{order.getTotalPrice():.2f}")
        
        elif choice == "7":
            break
        
        else:
            print("Invalid option.")
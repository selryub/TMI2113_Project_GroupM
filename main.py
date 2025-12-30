"""
DirectFarm Samarahan System - Main Program
Group M - TMI2113 Object-Oriented Software Development
"""

from classes.user import User
from classes.buyer import Buyer
from classes.farmer import Farmer
from classes.village_coordinator import VillageCoordinator
from classes.community_driver import communityDriver
from classes.produce import Produce
from classes.order import Order
from classes.delivery_trip import deliveryTrip

from menus.user_menu import userMenu
from menus.buyer_menu import buyer_menu
from menus.village_coordinator_menu import villageCoordinatorMenu 
from menus.farmer_menu import farmerMenu
from menus.produce_menu import produceMenu
from menus.order_menu import orderMenu
from menus.delivery_trip_menu import deliveryTripMenu
from menus.community_driver_menu import communityDriverMenu


# ============== GLOBAL DATA STORAGE ==============
# Simulates a database for demonstration purposes

class SystemData:
    """Central data storage for all system entities"""
    def __init__(self):
        # Users
        self.users = {}
        self.buyers = {}
        self.farmers = {}
        self.coordinators = {}
        
        # Business entities
        self.produces = {}
        self.orders = {}
        self.trips = {}
        self.drivers = {}
        
        # Initialize with sample data
        self._initialize_sample_data()
    
    def _initialize_sample_data(self):
        """Create sample data for testing"""
        
        # Sample Buyers
        buyer1 = Buyer("B001", "Ashley Tan", "ashley@email.com", "pass123", 
                       "Kuching", "Online Banking")
        buyer2 = Buyer("B002", "Michael Wong", "michael@email.com", "pass456",
                       "Kota Samarahan", "Cash")
        self.buyers = {"B001": buyer1, "B002": buyer2}
        
        # Sample Farmers
        farmer1 = Farmer("F001", "John Lee", "john@email.com", "pass789",
                        "Sunrise Farm", "Samarahan")
        farmer2 = Farmer("F002", "Sarah Chai", "sarah@email.com", "pass321",
                        "Green Valley Farm", "Serian")
        self.farmers = {"F001": farmer1, "F002": farmer2}
        
        # Sample Coordinator
        coordinator = VillageCoordinator("VC001", "Alice Lim", "alice@email.com", 
                                        "pass999", "Happy Village", "012-3456789")
        self.coordinators = {"VC001": coordinator}
        
        # Sample Produces (supplied by farmers)
        produce1 = Produce("P001", "Tomato", "Vegetable", "A", 50, 3.50)
        produce2 = Produce("P002", "Spinach", "Vegetable", "B", 30, 2.80)
        produce3 = Produce("P003", "Corn", "Vegetable", "A", 40, 1.50)
        produce4 = Produce("P004", "Cucumber", "Vegetable", "A", 25, 2.00)
        
        self.produces = {
            "P001": produce1,
            "P002": produce2,
            "P003": produce3,
            "P004": produce4
        }
        
        # Link produces to farmers
        farmer1.supplyProduce(produce1)
        farmer1.supplyProduce(produce2)
        farmer2.supplyProduce(produce3)
        farmer2.supplyProduce(produce4)
        
        # Sample Orders
        order1 = Order("O001", "B001", "P001")
        order1.setQuantity(10)
        order1.calculateTotal(3.50)
        order1.updateStatus("Pending")
        
        order2 = Order("O002", "B002", "P003")
        order2.setQuantity(20)
        order2.calculateTotal(1.50)
        order2.updateStatus("Verified")
        
        self.orders = {"O001": order1, "O002": order2}
        
        # Sample Drivers
        driver1 = communityDriver("D001", "Ahmad", "Van", "011-2345678")
        driver2 = communityDriver("D002", "Liang", "Motorcycle", "013-9876543")
        driver1.set_availability(True)
        driver2.set_availability(False)
        
        self.drivers = {"D001": driver1, "D002": driver2}
        
        # Sample Delivery Trips
        trip1 = deliveryTrip("T001", 15)
        trip2 = deliveryTrip("T002", 25)
        
        self.trips = {"T001": trip1, "T002": trip2}
        
        print("\n[SYSTEM] Sample data initialized successfully")


# Global system data instance
system_data = SystemData()


def display_welcome_banner():
    """Display system welcome banner"""
    print("\n" + "="*60)
    print("          DIRECTFARM SAMARAHAN SYSTEM")
    print("     Object-Oriented Software Development Project")
    print("                    Group M - TMI2113")
    print("="*60)
    print("\n[INFO] Connecting farmers and buyers directly")
    print("[INFO] Reducing carbon footprint through efficient delivery")
    print()


def display_system_overview():
    """Display current system statistics"""
    print("\n===== SYSTEM OVERVIEW =====")
    print(f"Total Buyers       : {len(system_data.buyers)}")
    print(f"Total Farmers      : {len(system_data.farmers)}")
    print(f"Total Produces     : {len(system_data.produces)}")
    print(f"Total Orders       : {len(system_data.orders)}")
    print(f"Available Drivers  : {sum(1 for d in system_data.drivers.values() if d.isAvailable() == 'Available')}")
    print(f"Active Trips       : {len(system_data.trips)}")
    print("===========================")


def main_menu():
    """Main system menu with integrated functionality"""
    
    display_welcome_banner()
    
    while True:
        print("\n" + "="*40)
        print("       MAIN MENU")
        print("="*40)
        print("1.  User Management")
        print("2.  Buyer Operations")
        print("3.  Farmer Operations")
        print("4.  Village Coordinator Operations")
        print("5.  Produce Management")
        print("6.  Order Management")
        print("7.  Delivery Trip Management")
        print("8.  Community Driver Management")
        print("9.  System Overview")
        print("10. Quick Demo (Test All Features)")
        print("0.  Exit System")
        print("="*40)
        
        choice = input("Select option: ").strip()
        
        if choice == "1":
            userMenu()
            
        elif choice == "2":
            # Pass system data to buyer menu
            buyer_menu_enhanced()
            
        elif choice == "3":
            farmerMenu()
            
        elif choice == "4":
            villageCoordinatorMenu()
            
        elif choice == "5":
            # Pass produce list to menu
            produceMenu(list(system_data.produces.values()))
            
        elif choice == "6":
            # Pass orders to menu
            orderMenu_enhanced()
            
        elif choice == "7":
            deliveryTripMenu(system_data.trips, system_data.drivers, system_data.orders)
            
        elif choice == "8":
            communityDriverMenu(system_data.drivers, system_data.trips)
            
        elif choice == "9":
            display_system_overview()
            input("\nPress Enter to continue...")
            
        elif choice == "10":
            run_quick_demo()
            
        elif choice == "0":
            print("\n" + "="*60)
            print("Thank you for using DirectFarm Samarahan System!")
            print("Connecting Communities, Reducing Carbon Footprint")
            print("="*60 + "\n")
            break
            
        else:
            print("[ERROR] Invalid option. Please try again.")


def buyer_menu_enhanced():
    """Enhanced buyer menu with access to system data"""
    print("\n--- Select Buyer ---")
    for buyer_id, buyer in system_data.buyers.items():
        print(f"{buyer_id}: {buyer.userName}")
    
    buyer_id = input("Enter Buyer ID (or 'back' to return): ").strip()
    
    if buyer_id.lower() == 'back':
        return
    
    if buyer_id not in system_data.buyers:
        print("[ERROR] Buyer not found.")
        return
    
    buyer = system_data.buyers[buyer_id]
    buyer.login()
    
    while True:
        print("\n===== BUYER MENU =====")
        print(f"Logged in as: {buyer.userName}")
        print("="*30)
        print("1. Browse Available Produce")
        print("2. Place New Order")
        print("3. View My Orders")
        print("4. View Profile")
        print("0. Logout")
        
        choice = input("Select: ").strip()
        
        if choice == "1":
            browse_produce_catalog()
            
        elif choice == "2":
            place_order_enhanced(buyer)
            
        elif choice == "3":
            view_buyer_orders(buyer)
            
        elif choice == "4":
            buyer.viewProfile()
            
        elif choice == "0":
            buyer.logout()
            break
        else:
            print("[ERROR] Invalid option.")
        
        input("\nPress Enter to continue...")


def browse_produce_catalog():
    """Display all available produces"""
    print("\n===== AVAILABLE PRODUCE CATALOG =====")
    if not system_data.produces:
        print("No produce available.")
        return
    
    for produce_id, produce in system_data.produces.items():
        details = produce.getProduceDetails()
        status = "Available" if produce.checkAvailability() else "Out of Stock"
        print(f"\n{produce_id}: {details['name']}")
        print(f"  Category : {details['category']}")
        print(f"  Grade    : {details['grade']}")
        print(f"  Weight   : {details['weight']} kg")
        print(f"  Price    : RM{details['price']}/kg")
        print(f"  Status   : {status}")


def place_order_enhanced(buyer):
    """Place order with real produce data"""
    print("\n--- Place New Order ---")
    browse_produce_catalog()
    
    produce_id = input("\nEnter Produce ID: ").strip()
    
    if produce_id not in system_data.produces:
        print("[ERROR] Produce not found.")
        return
    
    produce = system_data.produces[produce_id]
    
    if not produce.checkAvailability():
        print("[ERROR] This produce is currently unavailable.")
        return
    
    try:
        quantity = int(input("Enter quantity (kg): "))
        if quantity <= 0:
            print("[ERROR] Quantity must be positive.")
            return
        
        # Create new order
        order_id = f"O{len(system_data.orders) + 1:03d}"
        new_order = Order(order_id, buyer.userID, produce_id)
        new_order.setQuantity(quantity)
        
        details = produce.getProduceDetails()
        new_order.calculateTotal(details['price'])
        
        # Ask about discount
        has_discount = input("Apply discount? (y/n): ").strip().lower()
        if has_discount == 'y':
            discount = float(input("Enter discount percentage: "))
            new_order.calculateTotalWithDiscount(details['price'], quantity, discount)
        
        # Store order
        system_data.orders[order_id] = new_order
        buyer.order_history.append({
            "orderID": order_id,
            "item": details['name'],
            "quantity": quantity,
            "total": new_order.getTotalPrice()
        })
        
        print(f"\n[SUCCESS] Order {order_id} created!")
        print(f"Total: RM{new_order.getTotalPrice():.2f}")
        print("Status: Pending Verification")
        
    except ValueError:
        print("[ERROR] Invalid input.")


def view_buyer_orders(buyer):
    """View all orders for a specific buyer"""
    print("\n===== MY ORDERS =====")
    buyer_orders = {oid: order for oid, order in system_data.orders.items() 
                    if order.getBuyerID() == buyer.userID}
    
    if not buyer_orders:
        print("No orders found.")
        return
    
    for order_id, order in buyer_orders.items():
        produce = system_data.produces.get(order.getProduceID())
        produce_name = produce.getProduceDetails()['name'] if produce else "Unknown"
        
        print(f"\nOrder ID   : {order_id}")
        print(f"Produce    : {produce_name}")
        print(f"Quantity   : {order.getQuantity()} kg")
        print(f"Total      : RM{order.getTotalPrice():.2f}")
        print(f"Status     : {order.getStatus()}")


def orderMenu_enhanced():
    """Enhanced order menu with system integration"""
    while True:
        print("\n===== ORDER MANAGEMENT =====")
        print("1. View All Orders")
        print("2. View Order Details")
        print("3. Update Order Status")
        print("4. Calculate Order Statistics")
        print("0. Back to Main Menu")
        
        choice = input("Select: ").strip()
        
        if choice == "1":
            view_all_orders()
        elif choice == "2":
            view_order_details()
        elif choice == "3":
            update_order_status()
        elif choice == "4":
            calculate_order_statistics()
        elif choice == "0":
            break
        else:
            print("[ERROR] Invalid option.")
        
        input("\nPress Enter to continue...")


def view_all_orders():
    """Display all orders in the system"""
    print("\n===== ALL ORDERS =====")
    if not system_data.orders:
        print("No orders in system.")
        return
    
    for order_id, order in system_data.orders.items():
        buyer = system_data.buyers.get(order.getBuyerID())
        produce = system_data.produces.get(order.getProduceID())
        
        buyer_name = buyer.userName if buyer else "Unknown"
        produce_name = produce.getProduceDetails()['name'] if produce else "Unknown"
        
        print(f"\n{order_id}: {buyer_name} → {produce_name}")
        print(f"  Quantity: {order.getQuantity()} kg | Total: RM{order.getTotalPrice():.2f} | Status: {order.getStatus()}")


def view_order_details():
    """View detailed information about an order"""
    order_id = input("Enter Order ID: ").strip()
    
    if order_id not in system_data.orders:
        print("[ERROR] Order not found.")
        return
    
    order = system_data.orders[order_id]
    order.viewOrderDetails()


def update_order_status():
    """Update order status (Coordinator function)"""
    order_id = input("Enter Order ID: ").strip()
    
    if order_id not in system_data.orders:
        print("[ERROR] Order not found.")
        return
    
    order = system_data.orders[order_id]
    
    print("\nCurrent Status:", order.getStatus())
    print("\nAvailable Statuses:")
    print("1. Pending")
    print("2. Verified")
    print("3. Approved")
    print("4. Preparing")
    print("5. Out for Delivery")
    print("6. Delivered")
    print("7. Cancelled")
    
    status_choice = input("Select status: ").strip()
    status_map = {
        "1": "Pending",
        "2": "Verified",
        "3": "Approved",
        "4": "Preparing",
        "5": "Out for Delivery",
        "6": "Delivered",
        "7": "Cancelled"
    }
    
    if status_choice in status_map:
        new_status = status_map[status_choice]
        notes = input("Enter notes (optional): ").strip()
        order.updateStatus(new_status, notes)
        print(f"[SUCCESS] Order {order_id} updated to {new_status}")
    else:
        print("[ERROR] Invalid status selection.")


def calculate_order_statistics():
    """Display order statistics"""
    print("\n===== ORDER STATISTICS =====")
    
    total_orders = len(system_data.orders)
    total_revenue = sum(order.getTotalPrice() for order in system_data.orders.values())
    
    status_count = {}
    for order in system_data.orders.values():
        status = order.getStatus()
        status_count[status] = status_count.get(status, 0) + 1
    
    print(f"Total Orders     : {total_orders}")
    print(f"Total Revenue    : RM{total_revenue:.2f}")
    print("\nOrders by Status:")
    for status, count in status_count.items():
        print(f"  {status:15s}: {count}")


def run_quick_demo():
    """Run a quick demonstration of all system features"""
    print("\n" + "="*60)
    print("           QUICK DEMO - TESTING ALL FEATURES")
    print("="*60)
    
    input("\n[1/7] Press Enter to test Inheritance (User → Buyer/Farmer/Coordinator)...")
    print("\n--- Testing Polymorphism: viewProfile() Override ---")
    print("\n1. Base User Profile:")
    user = User("U999", "Test User", "test@email.com", "pass")
    user.viewProfile()
    
    print("\n2. Buyer Profile (Overridden):")
    system_data.buyers["B001"].viewProfile()
    
    print("\n3. Farmer Profile (Overridden):")
    system_data.farmers["F001"].viewProfile()
    
    print("\n4. Coordinator Profile (Overridden):")
    system_data.coordinators["VC001"].viewProfile()
    
    input("\n[2/7] Press Enter to test Encapsulation (Private Attributes)...")
    print("\n--- Testing Encapsulation ---")
    order = system_data.orders["O001"]
    print("Accessing private attributes through getters:")
    print(f"  Order ID (via getter)    : {order.getOrderID()}")
    print(f"  Buyer ID (via getter)    : {order.getBuyerID()}")
    print(f"  Total Price (via getter) : RM{order.getTotalPrice():.2f}")
    
    input("\n[3/7] Press Enter to test Polymorphism - Method Overloading...")
    print("\n--- Testing Method Overloading ---")
    test_order = Order("DEMO01", "B001", "P001")
    test_order.setQuantity(5)
    print("\n1. calculateTotal(price):")
    test_order.calculateTotal(10.00)
    
    print("\n2. calculateTotalWithDiscount(price, quantity, discount):")
    test_order.calculateTotalWithDiscount(10.00, 5, 15)
    
    print("\n3. updateStatus(status) - without notes:")
    test_order.updateStatus("Verified")
    
    print("\n4. updateStatus(status, notes) - with notes:")
    test_order.updateStatus("Approved", "Verified by coordinator")
    
    input("\n[4/7] Press Enter to test Association (Buyer → Order → Produce)...")
    print("\n--- Testing Association ---")
    order = system_data.orders["O001"]
    buyer = system_data.buyers[order.getBuyerID()]
    produce = system_data.produces[order.getProduceID()]
    
    print(f"Order {order.getOrderID()} connects:")
    print(f"  Buyer   : {buyer.userName}")
    print(f"  Produce : {produce.getProduceDetails()['name']}")
    print(f"  Amount  : RM{order.getTotalPrice():.2f}")
    
    input("\n[5/7] Press Enter to test Aggregation (Trip → Orders → Logs)...")
    print("\n--- Testing Aggregation ---")
    trip = system_data.trips["T001"]
    print(f"Trip {trip.trip_id} aggregates:")
    trip.add_order("O001")
    trip.add_order("O002")
    print(f"  Total Orders: {len(trip.orders)}")
    trip.view_logs()
    
    input("\n[6/7] Press Enter to test Delivery Workflow...")
    print("\n--- Testing Complete Delivery Workflow ---")
    trip = system_data.trips["T002"]
    driver = system_data.drivers["D001"]
    
    print("Step 1: Assign driver to trip")
    trip.assign_driver(driver)
    
    print("\nStep 2: Update delivery status")
    driver.update_delivery_status(trip, "On the Way", "Driver")
    
    print("\nStep 3: View trip details")
    trip.view_trip_details()
    
    input("\n[7/7] Press Enter to see final system statistics...")
    display_system_overview()
    
    print("\n" + "="*60)
    print("              DEMO COMPLETED SUCCESSFULLY")
    print("     All OO Concepts Demonstrated:")
    print("     ✓ Inheritance    ✓ Encapsulation    ✓ Polymorphism")
    print("     ✓ Association    ✓ Aggregation")
    print("="*60)
    
    input("\nPress Enter to return to main menu...")


if __name__ == "__main__":
    main_menu()
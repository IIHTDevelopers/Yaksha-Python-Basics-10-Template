# Warehouse Management System
# Topics: Control Flow, Tuples, Dictionaries, If-Else

def initialize_inventory():
    """
    Initializes warehouse inventory with tuples (Item Name, Quantity, Price per Unit).
    """
    return {
        "W101": ("Laptops", 50, 800),
        "W102": ("Smartphones", 100, 500),
        "W103": ("Headphones", 200, 50),
        "W104": ("Keyboards", 150, 30),
        "W105": ("Monitors", 75, 200)
    }


def most_expensive_item(inventory):
    """
    Finds the most expensive item in inventory.
    """
    pass  # TODO: Implement logic to find the item with the highest price per unit


def monitor_stock(inventory):
    """
    Gets the stock and price details of Monitors.
    """
    pass  # TODO: Implement logic to check if 'W105' exists and return its stock details


def total_items_in_warehouse(inventory):
    """
    Calculates total stock in warehouse.
    """
    pass  # TODO: Implement logic to sum up quantities of all items


# Main Execution
def main():
    """
    Main execution function.
    """
    inventory = initialize_inventory()

    print("Most Expensive Item:", most_expensive_item(inventory))  # TODO: Implement function call
    print("Monitor Stock:", monitor_stock(inventory))  # TODO: Implement function call
    print("Total Items in Warehouse:", total_items_in_warehouse(inventory))  # TODO: Implement function call


if __name__ == "__main__":
    main()

menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}

def calculate_subtotal(order):
    total = 0
    for item in order:
        itemPrice = item["price"]
        total+=itemPrice
    total = float(total)
    return round(total,2)
    # raise NotImplementedError()

def calculate_tax(subtotal):
    tax = round(subtotal * 0.15,2)
    return  tax
    # raise NotImplementedError()

def summarize_order(order):
    total =0
    summary=[]
    for item in order:
        total+=item['price']
        summary.append(item["name"])
    tax = calculate_tax(total)
    grandTotal = round(tax + total,2)
    return summary,grandTotal
    # raise NotImplementedError()

# This function is provided for you, and will print out the items in an order
def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order

# This function is provided for you, and will display the menu
def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

# This function is provided for you, and will create an order by prompting the user to select menu items
def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order

def main():
    order = take_order()
    print_order(order)
    calculate_subtotal(order)
    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str(subtotal))
    tax = calculate_tax(subtotal)
    print("Tax for the order is: " + str(tax))
    x=summarize_order(order)
    items, subtotal = summarize_order(order)

if __name__ == "__main__":
    main()

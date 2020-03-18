
from datetime import datetime
import os


#Goal 1: simplify USD formatting
#Goal 2: simplify receipt printing / file writing
#Goal 2: simplify receipt printing / file writing


checkout_at = datetime.now().strftime("%M/%d/%Y %I:%m %p")

selected_products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
] # FYI: for the purposes of this exercise, you won't need to modify this list at all

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}"



now = datetime.now()

subtotal = sum([p["price"] for p in selected_products])

# PRINT RECEIPT

print("---------")
print("CHECKOUT AT: " + str(now.strftime("%Y-%M-%d %H:%m:%S")))
print("---------")
for p in selected_products:
    print("SELECTED PRODUCT: " + p["name"] + "   " + to_usd(p["price"]))
print("---------")
print(f"SUBTOTAL: {to_usd(subtotal)}")
print(f"TAX: {to_usd(subtotal * 0.0875)}")
print(f"TOTAL: {to_usd((subtotal * 0.0875) + subtotal)}")
print("---------")
print("THANK YOU! PLEASE COME AGAIN SOON!")
print("---------")

# WRITE RECEIPT TO FILE

file_name = os.path.join(os.path.dirname(__file__), "..", "receipts", f"{now.strftime('%Y-%M-%d-%H-%m-%S')}.txt")
with open(file_name, 'w') as f:
    f.write("------------------------------------------")
    for p in selected_products:
        f.write("\nSELECTED PRODUCT: " + p["name"] + "   " + '${:.0f}'.format(p["price"]))

    f.write("---------")
    f.write(f"SUBTOTAL: {subtotal:,.2f}")
    f.write(f"TAX: {(subtotal * 0.1):.2f}")
    f.write(f"TOTAL: {((subtotal * 0.1) + subtotal):.2f}")
    f.write("---------")
    f.write("THANK YOU! PLEASE COME AGAIN SOON!")
    f.write("---------")

# TODO: SEND RECEIPT VIA EMAIL

items = {
    1: ("Milk",55,5),
    2: ("Bread",50,0),
    3: ("Eggs(12)",100,4),
    4: ("Rice 5 kg", 350,5),
    5: ("Oil 1L", 120,5)
}

def calculate_items(price,qty,gst):
    subtotal = price * qty
    gst_amount = (subtotal * gst) /100
    return subtotal,gst_amount

def apply_discount(amount, discount_percentage):
    return amount - (amount * discount_percentage / 100)

    


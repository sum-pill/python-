import groc as gm

cart = []

def show_items():
    print("----------------Seven 11-----------------")
    print("---------------Item  Menu-----------------")
    print(f"{"Item":<20}{"price":<12}{"gst":<6}")

    for item in gm.items:
        price,gst = gm.items[item]
        print(f"{item.title():<20}RS{price:<10.2f}{gst:<6.2f}")
        

show_items()         
    
def show_bill(cart,discount):
    print("-"*40)
    print(f"{'item':<20}{'qty':<6}{'price':<8}{'gst':<6}{'total_amount':<6}")
    subtotal = 0
    total_gst = 0
    for choice,qty in cart:
        price,gst = gm.items[choice]
        total_amount,gst_amount = gm.calculate_items(price,qty,gst)
        print(f"{choice.title():<20}{qty:<6}{price:<8.2f}{gst:<7.2f}{total_amount:<6.2f}")
    # subtotal +=total_amount
    # total_gst+=gst_amount   

    # print(f"{choice.title():<20}{qty:<6}{price:<8}{gst:<6}{total_amount:<6}")
        subtotal +=total_amount
        total_gst +=gst_amount   
    #    print(f"{choice.title():<20}{qty:<6}{price:<8.2f}{gst:<6.2f}{total_amount:<6.2f}")


    discounted_total = gm.apply_discount(subtotal,discount)
    final_amount = discounted_total - total_gst
    print("-"*40)
    print(f"{'subtotal:':<40}{subtotal:<10.2f}")
    print(f"{'discount %:':<40}{discount:<10.2f}")
    print(f"{"dicounted_total:":<40}{discounted_total:<10.2f}")
    print(f"{'gst:':<40}{total_gst:<10.2f}")
    print("-"*40)
    print(f"{'final amount:':<40}{final_amount}")
    print("-------------------Thank You---------------------")

while True:
    show_items()

    choice = input("\nEnter the item name or 'q' to exit  : ")
    if choice == 'q':
        break
    if not choice in gm.items:
        print("item not availible")
        continue
    qty = input("Enter the quantity : ")
    if not qty.isdigit():
        print("invalid number.please enter a valid matter")
        continue
    qty = int(qty)
    cart.append((choice,qty))
    print("added to cart")

discount = input("Enter discount percentage% :")
discount = int(discount) if discount.isdigit() else 0
    
    
print("added to cart")
if len(cart) == 0:
    print("no items added")
    
show_bill(cart,discount)






        
        
             
    

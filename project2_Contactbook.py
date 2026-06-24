Contacts = {}

def add_contact(name,phone):
    Contacts [name] = phone
    print(f"Added {name}")

def view_contact():
    for name,phone in Contacts.items():
     print(f"{name} : {phone}")

while True:
    print("\n 1.add contact.\n 2.view.\n 3.Exit" )

    choice = input("Enter the number (1/2/3):")

    if choice == '1':
      name = input("Enter the name :")
      phone = input("Enter the phone number:")
      add_contact(name,phone)
       
    if choice == '2':
     view_contact()

    elif choice == '3':
     print("invalid choice...")
     break
  
       

          



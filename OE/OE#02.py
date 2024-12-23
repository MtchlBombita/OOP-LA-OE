def create_phone():
    brand = input("Enter the phone brand: ")
    model = input("Enter the phone model: ")
    price = float(input("Enter the phone price: "))
    color = input("Enter the phone color: ")
    return {"brand": brand, "model": model, "price": price, "color": color}

def modify_phone(phone):
    print("1. Modify brand")
    print("2. Modify model")
    print("3. Modify price")
    print("4. Modify color")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        phone["brand"] = input("Enter new brand: ")
    elif choice == 2:
        phone["model"] = input("Enter new model: ")
    elif choice == 3:
        phone["price"] = float(input("Enter new price: "))
    elif choice == 4:
        phone["color"] = input("Enter new color: ")
    else:
        print("Invalid choice")

def delete_phone(phones, index):
    if 0 <= index < len(phones):
        del phones[index]
    else:
        print("Invalid index")

def display_phones(phones):
    if len(phones) == 0:
        print("No phones in the list")
    else:
        for i, phone in enumerate(phones):
            print(f"Phone {i + 1}:")
            print(f"Brand: {phone['brand']}")
            print(f"Model: {phone['model']}")
            print(f"Price: {phone['price']}")
            print(f"Color: {phone['color']}")

def main_menu():
    phones = []
    while True:
        print("\n--- Main Menu ---")
        print("1. Create phone")
        print("2. Modify phone")
        print("3. Delete phone")
        print("4. Display phones")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            phones.append(create_phone())
        elif choice == 2:
            if len(phones) == 0:
                print("No phones to modify")
            else:
                display_phones(phones)
                index = int(input(f"Enter the index of the phone to modify (1 to {len(phones)}): ")) - 1
                if 0 <= index < len(phones):
                    modify_phone(phones[index])
                else:
                    print("Invalid index")
        elif choice == 3:
            if len(phones) == 0:
                print("No phones to delete")
            else:
                display_phones(phones)
                index = int(input(f"Enter the index of the phone to delete (1 to {len(phones)}): ")) - 1
                delete_phone(phones, index)
        elif choice == 4:
            display_phones(phones)
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main_menu()

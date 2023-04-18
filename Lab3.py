#An empty dictionary ro store the items
shoppingCart = {}
while True:
    print("WELCOME TO THE AMANDO SHOPPING SITE")
    print("1. Add product to the cart.")
    print("2. Search the product.")
    print("3. Delete the product from the cart.")
    print("4. Quit.")
    choice = input("Enter your choice :")

    if choice == "1":
        count = int(input("Enter the number of items to be added in the shopping cart: "))

        for i in range(count):
            if len(shoppingCart) >= 5:
                print("Cart is full")
                break
            else:
                item = input("Enter an item: ")
                brand = input("Enter the brand Name: ")
                shoppingCart[item] = brand
        
        print("You added the following items to the cart:")
        for item, brand in shoppingCart.items():
            print(f"{item}: {brand}")
        
    elif choice == "2":
        search_item = input("Enter the item to be searched: ")
        if search_item in shoppingCart:
            print(f"{search_item}: {shoppingCart[search_item]}")
        else:
            print("No product exists with this name")

    elif choice == "3":
        if len(shoppingCart) == 0:
            print("Cart is empty, no item is found")
        else:
            del_item = input("Enter the item to be deleted: ")
            if del_item in shoppingCart:
                del shoppingCart[del_item]
                print(f"{del_item} has been removed from the cart.")
            else:
                print("No product exists with this name")

    elif choice == "4":
        break

    else:
        print("Wrong Option Entered.")

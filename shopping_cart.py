cart = []

while True:
    print("-------MENU------")
    print("1. Add product to cart")
    print("2. View Cart")
    print("3. Remove product")
    print("4. Calculate Total")
    print("5. Exit")

    choice = input("Enter your choice (1-5)")

    #product

    if choice == "1":
        pid = int(input("Enter product ID: "))
        name = input("Enter Product Name: ")
        price = float(input("Enter product price: "))

        product = (pid,name,price)
        cart.append(product)

        print("product added to cart")

    #View CArt

    elif choice  == "2":
        if not cart:
            print("Cart is empty")
        else:
            print("/nYour Cart Items: ")
            for p in cart:
                print("ID: ", p[0], "| Name: ",p[1],"|Price: ", p[2])

    #Remove product
    elif choice == "3":
        remove_id= int(input("enter Product ID to remove: "))
        for p in cart:
            if p[0]==remove_id:
                cart.remove(p)
                print("product Removed")
                break

            else:
                print("Product not found")

    #Total Bill
    elif choice == "4":
        total = 0
        for p in cart:
            total += p[2]

        print("Total Bill Amount: ", total)

    #Exit
    elif choice == "5":
        print ("thank you for shopping! :D")
        break

    else:
        print("invalid choice D:. Try Again")

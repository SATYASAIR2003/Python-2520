# Diary products Ecommerce 
System_info=("Milk Diarry Farm", "Milk Products","v1")
Admin_info=("7793969951","satya@gmail.com")

products ={}
while True:
    print("Choose an opition: ")
    print("1 - Add Product")
    print("2 - Update Product")
    print("3 - Delete Product")
    print("4 - List Product")
    print("5 - Exit System")

    choice = input("Enter Choice (1-5): ")
    
    if choice == "1":
        print("Adding Product Logic")
        product_id = input("Enter ID: ")
        if product_id in products:
            print("ID Already Exist, Try with different ID")
        else:
            Name = input("Enter Name: ").title()
            Quantity = int(input("Enter Quantity of Product in kg/L: "))
            Cost = int(input("Enter Cost of Product per kg/L: RS. "))
            Description=input("Provide Description: ")
            products[product_id] = {
                "name": Name,
                "quantity": Quantity,
                "cost": Cost,
                "description": Description,
            }
            print("Student Saved")
            
            # for our confirmation
            # print(products)
            
    elif choice == "2":
        print("Updating Product Logic")
        product_id = input("Enter ID To Update: ")
        
        while True:
                print("Choose an opition: ")
                print("1 - Change Name")
                print("2 - Change quantity")
                print("3 - Change cost")
                print("4 - Exit System")
                choice = input("Enter Choice (1-4): ")
                if choice == "1":
                    print("Updating name")
                    if product_id in products:
                        new_name = input("Enter New Name: ").title()
                        products[product_id]["name"] = new_name
                        print("product Name Updated")
                    else:
                        print("ID Doesn't Exist to Update")
                elif choice == "2":
                    print("Updating quantity")
                    if product_id in products:
                        new_quantity = input("Enter New quantity: ")
                        products[product_id]["quantity"] = new_quantity
                        print("product quantity Updated")
                    else:
                        print("ID Doesn't Exist to Update")
                elif choice == "3":
                    print("updating cost")
                    if product_id in products:
                        new_cost = input("Enter New quantity: ")
                        products[product_id]["cost"] = new_cost
                        print("product cost Updated")
                    else:
                        print("ID Doesn't Exist to Update")
                elif choice == "4":
                    print("Exit System")
                    break   
                else:
                    print("Invalid Option, Only Select (1-4)")
        # for our confirmation
        # print(products)


    elif choice == "3":
        print("Deleting Student Logic")
        product_id = input("Enter ID To Delete: ")
        if product_id in products:
            remove = products.pop(product_id)
            print(remove)
        else:
            print("ID Doesn't Exist to Delete")
        # for our confirmation
        # print(products)


    elif choice == "4":
        print("Listing Product Details")
        for pid, data in products.items():
            name = data["name"]
            Quantity = data["quantity"]

            print("="*50)
            print("PRODUCT DETAILS")
            print("="*50)
            
            print(f"ID: {pid}")
            print(f"NAME: {name}")
            print(f"QUANTITY: {Quantity}")
            print(f"COST: {Cost}")
            print(f"DESCRIPTION: {Description}")
    elif choice == "5":
        print("Exit System")
        print("="*50)
        print("CONTACT ADMIN FOR MORE INFORMATION")
        print(f"ADMIN CONTACT NO: {Admin_info[0]}")
        print(f"ADMIN EMAIL ID: {Admin_info[1]}")
        print("="*50)
        break
    else:
        print("Invalid Option, Only Select (1-5)")
    print(products)

    
# customers page will open
cart ={}
while True:
    print("Choose an opition: ")
    print("1 - Add Product")
    print("2 - Update Product")
    print("3 - Delete Product")
    print("4 - List Product")
    print("5 - Exit System")  

    Buying_products = input("Enter Choice (1-5): ")
    
    if Buying_products == "1":
        print("Adding Product")  
        while True:
            product_id = input("Enter product ID (or type 'stop' to exit): ")

            if product_id.lower() == "stop":
                print("\nStopped adding products.")
            break

        if product_id in products:
            product = products[product_id]
            Quantity1 = int(input("Enter quantity: "))
            if Quantity1 <= product["quantity"]:
                # Reduce stock
                product["quantity"] -= Quantity1  

                # Add to cart (if already exists, increase quantity)
                if product_id in cart:
                    cart[product_id]["quantity"] += Quantity1
                else:
                    cart[product_id] = {
                        "name": product["name"],
                        "quantity": Quantity1,
                        "cost": product["cost"],
                        "description": product["description"],
                    }
                print("Product added to cart")
            else:
                print("Not enough stock. Available:", product["quantity"])
        else:
            print("Product ID not found")
            print("\n Cart Summary:")
        for pid, item in cart.items():
            total_price = item["quantity"] * item["cost"]
            print(f"{item['name']} (x{item['cost']}) - Rs.{total_price}")
        
        
    elif Buying_products == "2":
            print("Updating Product in cart")
            product_id = input("Enter ID To Update: ")
        
            while True:
                print("Choose an opition: ")
                print("1 - Change Name")
                print("2 - Change quantity")
                print("3 - Exit System")
                choice = input("Enter Choice (1-3): ")
                if choice == "1":
                    print("Updating name")
                    if product_id in products:
                        new_name = input("Enter New Name: ").title()
                        products[product_id]["name"] = new_name
                        print("product Name Updated")
                    else:
                        print("ID Doesn't Exist to Update")
                elif choice == "2":
                    print("Updating quantity")
                    if product_id in products:
                        new_quantity = input("Enter New quantity: ")
                        products[product_id]["quantity"] = new_quantity
                        print("product quantity Updated")
                    else:
                        print("ID Doesn't Exist to Update")
                elif choice == "3":
                    print("Exit System")
                    break   
                else:
                    print("Invalid Option, Only Select (1-3)")
            
        # for our confirmation
        # print(products)


    elif Buying_products == "3":
        print("Deleting product from cart")
        product_id = input("Enter ID To Delete: ")
        if product_id in products:
            remove = products.pop(product_id)
            print(remove)
        else:
            print("ID Doesn't Exist to Delete")
        # for our confirmation
        print(products)


    elif Buying_products == "4":
        print("Listing Product Details")
        for pid, data in cart.items():
            name = data["name"]
            Quantity1 = data["quantity"]
            price=data[sum(Cost)]
            count=data[len(cart)]

            print("="*50)
            print("PRODUCT DETAILS")
            print("="*50)
            
            print(f"ID: {pid}")
            print(f"NAME: {name}")
            print(f"QUANTITY: {Quantity1}")
            print(f"COST: {Cost}")
            print(f"DESCRIPTION: {Description}")
            print(f"PRICE: ")
    elif Buying_products == "5":
        print("Exit System")
        print("="*50)
        # print("CONTACT ADMIN FOR MORE INFORMATION")
        # print(f"ADMIN CONTACT NO: {Admin_info[0]}")
        # print(f"ADMIN EMAIL ID: {Admin_info[1]}")
        print("="*50)
        break
    else:
        print("Invalid Option, Only Select (1-5)")
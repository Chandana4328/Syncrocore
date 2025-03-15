product_name=[]
product_quality=[]
product_price=[]
while True:
    print("1.Add Product")
    print("2.update the Product stock")
    print("3.Inventory")
    print("4.Exit")
    choice=int(input("Enter ur choice->"))
    if choice==1:
        print("add new to Invnetory->")
        name=input("Enter the name of the Product->")
        quantity=int(input("Enter the quantity of the product->"))
        price=int(input("Enter the price of the product"))
        product_name.append(name)
        product_quality.append(quantity)
        product_price.append(price)
        print(f"product {name} added successfully")
    elif choice==2:
        print("Update the Product stock")
        name=input("Enter the name of product->")
        if name in product_name:
            index=product_name.index(name)
            change=int(input("Enter the change in quantity->"))
            product_quality[index]=max(0,product_quality[index]+change)
            print(f"Stock updated {product_name[index]} now has {product_quality[index]} items")
        else:
            print("Product not found")
    elif choice==3:
        print("Current Inventory")
        if not product_name:
            print("Inventory is empty")
        else:
            for i in range(len(product_name)):
                print(f"{product_name[i]},{product_quality[i]},{product_price[i]}")
    elif choice==4:
        print("Exiting the program")
        break
    else:
        print("Invalid Choice")
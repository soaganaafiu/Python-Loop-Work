name = input("Enter your name: ")

product_sum = 0;


while("YES"):


    product_name = input("Enter product name: ")

    quantity_of_product = int(input("Enter quantity of " + product_name +": "))

    price_of_product = int(input("Enter price of " + product_name + ": "))

    proceed_prompt = input("Add another product yes / no" + ": ").upper()

    product_sum = product_sum + (price_of_product * quantity_of_product)

    if proceed_prompt == "NO":
        
        print(Total Price of , product_sum)

        break

































    

#if proceed_prompt == YES:
#
#    while procced_prompt == YES:
#
#        name = input("Enter your name: ")
#
#        product_name = input("Enter product name: ")
#
#        quantity_of_product = int(input("Enter quantity of " + product_name +": "))
#
#        price_of_product = int(input("Enter price of " + product_name + ": "))
#
#        proceed_prompt = input("Add another product yes / no" + ": ").upper()
#
#
#else:
#    
#    print(quantity_of_product * price_of_product)
    



 








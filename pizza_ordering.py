
# Created by La'Ron Latin

# Pizza Ordering Program


def main():
    ###prices
    small_price = float(7.00)
    medium_price = float(10.75)
    large_price = float(14.75)
    sauce_price = float(0.50)
    sauce_count = 0

    total_price = float(0.0)

    large_toppings = float(1.50)
    medium_toppings = float(1.00)
    small_toppings = float(.50)


### qty pizza's

####exception handling integer
    validInput = False


    while not validInput:
        try:
            pizza = int(input("How many pizza's would you like? "))
            validInput = True
        except:
            print("Please type an integer")

#### pizza size loop

    expected_sizes = ["small", "medium", "large"]
    for i in range(1, pizza + 1):

#### exception handling expected sizes in string

        validInput = False
        while not validInput:
            size = (input(f"for pizza {i}, what size would you like? ")).strip().lower()


            if size in expected_sizes:
                validInput = True
            else:
                print(f"Please enter a valid size {expected_sizes}")
#### Toppings prompt

        toppings = int(input(f"How many toppings do you want for that {size} pizza?"))
#### conditionals to determine price with toppings

        if size == "small" and toppings < 1:
            price = small_price
            print(" ")
            print(f"Your total for a {size} pizza with {toppings} toppings is {price:.2f}")

        elif size == "medium" and toppings < 1:
            price = medium_price
            print(" ")
            print(f"Your total for {size} pizza with with {toppings} toppings is {price:.2f}")

        elif size == "large" and toppings < 1:
            price = large_price
            print(" ")
            print(f"Your total for {size} pizza with {toppings} toppings is {price:.2f}")

        elif size == "small" and toppings > 0:
            price = small_price + (toppings * small_toppings)
            print(" ")
            print(f"Your total for {size} pizza with {toppings} toppings is {price:.2f}")

        elif size == "medium" and toppings > 0:
            price = medium_price + (toppings * medium_toppings)
            print(" ")
            print(f"Your total for {size} pizza with {toppings} toppings is {price:.2f}")


        elif size == "large" and toppings > 0:
            print(" ")
            price = large_price + (toppings * large_toppings)
            print(f"Your total for {size} pizza with {toppings} toppings is {price:.2f}")




        print(" ")

        #### optional sauce

        sauce = input(f"would you like extra sauce on the {size} pizza {i} for $.50 extra? (y/n)").strip().lower()

        if sauce == "y":
            price += sauce_price
            sauce_count += 1
            total_price += price

        else:
            total_price += price


     ###subtotal

    print(" ")
    print(" ")
    print(f"Your subtotal for {i} pizzas with {toppings} toppings and {sauce_count} with extra sauce(s) $ {total_price:.2f}")
    print(" ")

    ###sales tax

    total_sales_tax = float(total_price * 0.04)
    print(f"Sales tax of 4% is: ${total_sales_tax:.2f}")
    print(" ")


    #### total cost with Tax
    print(f"This brings your total price to ${total_price + total_sales_tax:.2f}")

main()



def main():
    cost = 0
    k = 0
    numbersForOrder = 0
    totalCost = 0
    s = ''
    #I shall use a dictionary of dictionary object--see below.
    # These are the food items, their prices, and the numbers that represent them.
    restaurant = {
    1: {'food' : 'Chicken Strips', 'price' : 3.50},
    2 : {'food' : 'French Fries', 'price' : 2.50},
    3 : {'food' : 'Hamburger', 'price' : 4.00},
    4 : {'food' : 'Hotdog', 'price' : 3.50},
    5 : {'food' : 'Large Drink', 'price' : 1.75},
    6 : {'food' : 'Medium Drink', 'price' : 1.50},
    7 : {'food' : 'Milk Shake', 'price' : 2.25},
    8 : {'food' : 'Salad', 'price' : 3.75},
    9 : {'food' : 'Small Drink', 'price' : 1.25}}
    
    #print the menu.
    #for key in restaurant:
        #print(str(key) + ' ' + restaurant[key]['food'] + ' ' + str(restaurant[key]['price']))
        #print('\n')



    # The while loop to control the calculation of the cost of the food and to
    # help with the printing of the receipt.
    while True:
        s = s + input("Enter the numbers that represent your order: ") # string input s
        print(s) # prints s

        # userInputB ask the user/client if he wants to order some more food in addition of what he has ordered ...
        # or to simply pay for what he already ordered.
        userInputB = input("Do you wish to order more food?\n Press Y for yes\n Press N for no: \n")
        print('\n')


        # The if statement permits the user to order additional food but the else statement permits user to pay ...
        # for what he has already ordered.
        if userInputB == 'Y':
            continue # this takes us back to the while loop
        else:
            break # this breaks out of while loop

    print("****************** THIS IS A COPY OF YOUR RECEIPT *****************************")
    print('\n')

    print("{}    {}             {}    {}".format("#", "FOOD", "PRICE($)", "TOTAL COST($)"))
    print("-------------------------------------------------------------------------------")

    # The double for loop calculates the cost of all the food ordered
    for i in range(len(s)):
        for key in restaurant:
            if (key == int(s[i])):
                cost = cost + restaurant[key]['price']

                if len(restaurant[key]['food']) == 14:
                    food = restaurant[key]['food'].ljust(20, ' ')
                elif len(restaurant[key]['food']) == 12:
                    food = restaurant[key]['food'].ljust(20, ' ')
                elif len(restaurant[key]['food']) == 11:
                    food = restaurant[key]['food'].ljust(20, ' ')
                elif len(restaurant[key]['food']) == 10:
                    food = restaurant[key]['food'].ljust(20, ' ')
                elif len(restaurant[key]['food']) == 9:
                    food = restaurant[key]['food'].ljust(20, ' ')
                elif len(restaurant[key]['food']) == 6:
                    food = restaurant[key]['food'].ljust(20, ' ')
                else:
                    food = restaurant[key]['food'].ljust(20, ' ')


                # prints the "food number", "type of food", "price of food", and "total cost of the food" ordered by the user.
                print(str(key) + '   ' + food + ' ' + str(restaurant[key]['price']) + '         ' + str(cost))
                print('\n')




    # Print the total cost of the meal.
    print("Total Costs: {}".format(cost))

    print("\n")
    print("******************** I APPRECIATE YOUR BUSINESS ********************************")
    print('\n')
    
    # This ask the user if he wants to make another order or not.
    x = input("Do you wish to continue?\n Press Y for yes\n Press N for no: \n")

    # if else statement below provides mechanism through which the user the user will answer the question in x above.
    if (x == 'Y'):
        main()
    else:
        print("\n")
        print("We thank you for choosing us-please come by to see us !!!")
        exit()

# This is a call to the function "main"
main()

MENU  CALCULATOR

Imagine you have started up a small restaurant and are trying to make it easier to take and calculate orders. Since your restaurant only sells 9 different items, you assign each one to a number, as shown below:

 1  Chicken Strips - $3.50
 2  French Fries - $2.50
 3  Hamburger - $4.00
 4  Hotdog - $3.50
 5  Large Drink - $1.75
 6  Medium Drink - $1.50
 7  Milk Shake - $2.25
 8  Salad - $3.75
 9  Small Drink - $1.25
 
To quickly take orders, your program should allow the user to type in a string of numbers and then it should calculate the cost of the order. For example, if one large drink, two small drinks, two hamburgers, one hotdog, and a salad are ordered, the user should type in 5993348, and the program should say that it costs $19.50. Also, make sure that the program loops so the user can take multiple orders without having to restart the program each time.

Subgoals: 

If you decide to, print out the items and prices every time before the user types in an order.
Once the user has entered an order, print out how many of each item have been ordered, as well as the total price.
If an item was not ordered at all, then it should not show up.

A. Core ideas of the structure of the program(code):

a. The function main() was placed at the last line of the code. This makes it possible to repeat the program without
   restarting the program each time. The last if else statement at the bottom of the program makes it possible for
   the user to make some more orders after they have checked out/received a receipt or to quit(make no order).
   
b. The double for loops calculate the total cost of the meals ordered. They also print out the receipt of the user's    
   order.
   
c. A variable called userInput was used to give the user the ability to make more orders before the final check out.

   
   
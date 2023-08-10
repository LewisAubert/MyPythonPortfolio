#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

cost = float(input("Please enter the exact cost of the bill in dollars \n"))
people = int(input("Please enter the number of people you'd like to split the bill with.\n"))
tip = int(input("What percentage tip would you like to leave?\n"))

payment = (cost / people) * ((100 + (tip)) / 100) #converting the strings into integers and floats so that they can be used in calculations.

# print(payment)

split = (round(payment, 2)) #rounding the payment variable to two decimal places, like it is an actual amount of money. - changed after an error was found.

#I have noticed that for the example given in the beginning, the output displays 33.6, when I want it to display 33.60. To get around this formatting error, you need to use the function split = "{:.2f}".format(payment)

split = "{:.2f}".format(payment)

print(f"Each person should pay ${split}")

# using the f-string here so that I can combine the different variables without having to change their type in the code.

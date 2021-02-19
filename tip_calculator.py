print ("Welcome to Zak's tip calculator!")
# Requests user's name and saves it to a variable
user_name = input("What's your name?")

# Welcomes the user
print(f"Welcome, {user_name}!")

# Finds out how many more diners and converts to int
additional_diners = int(input("How many other people joined you for dinner?"))

# Determines total number of diners
total_diners = additional_diners + 1

# Finds out the total cost of the bill post-tax and converts to float
total_bill = float(input("And what was the total cost of the meal after tax?"))

# Calculates pre-tax bill, assuming 10% sales tax
pretax_bill = total_bill / 1.1

# Finds out the tip percent from user and converts to float, then divides by 100 to create a percent
tip_percent = float(input("What percent would you like to tip? (Please don't include the percentage sign)")) / 100

# Calculates total bill, assuming tip on only the pre-tax amount; rounds to two digits
total_bill = round(total_bill + (tip_percent * pretax_bill), 2)

# Calculates bill per person; rounds to two digits
bill_per_person = round(total_bill / total_diners, 2)

# Output for user
print(f"Sorry to be so nosy, {user_name}! The total bill comes to {total_bill}, and assuming you're splitting the bill evenly, each of you owes {bill_per_person}.")
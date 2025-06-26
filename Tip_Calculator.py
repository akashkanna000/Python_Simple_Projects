#Greeting the user is must
print("Welcome to the tip calculator")

#User need to input the total bill
bill = float(input("what was the total bill ?\n$"))

#Ask the user to enter the percentage of tip
tip = int(input("what percentage tip would you like to give ? 10, 12, 15\n"))

#Ask the user to enter the number of people sharing the bill
people = int(input("How many people to split the bill ?\n"))

#tip calculator formula begins.........
tip_percentage = tip / 100 #common percentage formula
total_tip = tip_percentage * bill #calculate total tip
total_bill = total_tip + bill # add tip to the total bill
per_person_bill = total_bill / people #divide by number of people to get per person amount
total_amount  = round(per_person_bill, 2)

#Now we can calculate how much each person should pay
print(f"Each person should pay: \n${total_amount}")
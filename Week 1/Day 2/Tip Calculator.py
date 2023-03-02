print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

final_amount = float(bill) * float(1 + (int(tip)/100))

each_person = final_amount/int(people)

rounded = round(each_person,2)
rounded = "{:.2f}".format(each_person)

print(f"Each person should pay: ${rounded}")
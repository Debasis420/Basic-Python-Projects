#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6

print("Welcome to the tip calculator!")
bill = float(input("what was the total bill?\n$"))
tip = int(input("How much percentage of tip would you like to give?(10,12,or15)\n"))
people = int(input("How many people to split the bill?\n"))
total_bill = tip/100 * bill + bill
bill_per_person = total_bill / people
final_amount =(round(bill_per_person, 2)) 
#or
#final_amount ="{:2f}".format(bill_per_person) 
print(f"So each one of you has to pay ${final_amount}")

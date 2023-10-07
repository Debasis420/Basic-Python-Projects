print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L\n").lower()   # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Y or N\n").lower()  # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Y or N\n").lower()   # Do you want extra cheese? Y or N

# Write your code below this line 👇

bill = 0

if size == "s":
    bill = bill + 15
elif size == "m":
    bill = bill + 20
else:
    bill = bill + 25

if add_pepperoni == "y":
    if size == "s":
        bill = bill + 2
    else:
        bill = bill + 3

if extra_cheese == "y":
    bill = bill + 1

print(f"Your final bill is: ${bill}.")

print("Welcome to Bill Splitter App")
print()

bill = float(input("Enter total bill: "))
people = int(input("Enter number of people: "))
tip = int(input("Enter tip percentage (0/5/10/15/20): "))
print()

tip_amount = bill * tip / 100
total_bill = bill + tip_amount
per_person = total_bill / people
print()

print("Tip Amount:", tip_amount)
print("Total Bill:", total_bill)
print("Each person pays:", per_person)
print()
again = input("Would you like to calculate another bill? (y/n): ")


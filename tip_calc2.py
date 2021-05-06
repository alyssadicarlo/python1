bill_amount = float(input("Total bill amount? "))
level_of_service = input("Level of service? (good, fair, bad) ")
num_of_people = int(input("Split how many ways? "))
tip_percent = 0

if level_of_service == "good":
    tip_percent = 0.2
if level_of_service == "fair":
    tip_percent = 0.15
if level_of_service == "bad":
    tip_percent = 0.1

tip_amount = bill_amount * tip_percent
print("Tip amount: $%.2f" % (tip_amount))
total = bill_amount + tip_amount
print("Total amount: $%.2f" % (total))
split_amount = total / num_of_people
print("Amount per person: $%.2f" % (split_amount))
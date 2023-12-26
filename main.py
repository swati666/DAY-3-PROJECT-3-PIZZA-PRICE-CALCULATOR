# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1


#PiZZa Challenge
print("Welcome to the Pizza Deliveries!\n")
size=input("What size of Pizza do you want? S, M, or L ")


size_price=0
if size=="S":
  size_price=15
elif size=="M":
  size_price=20
elif size=="L":
  size_price=25

pepp=input("\nDo you want pepperoni? Y or N ")
pep_price=size_price
if pepp=="N":
  pep_price=size_price
elif size=="S" and pepp=="Y":
  pep_price=size_price+2
elif size=="L" or size=="M" and pepp=="Y":
  pep_price=size_price+3

cheese=input("\nDo you want Extra Cheese? Y or N ")
final_bill=pep_price
if cheese=="Y":
  final_bill=pep_price+1

print(f"\nYour final bill is: ${final_bill}.")

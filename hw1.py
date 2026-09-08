price_of_rice = 45
price_of_sugar = 40
price_of_oil = 130
kg_rice = 3
kg_sugar = 2.5
kg_oil = 1.8
rice_total = kg_rice * price_of_rice
print("total rice:",rice_total)
sugar_total = kg_sugar * price_of_sugar
print("total sugar:",sugar_total)
oil_total = kg_oil * price_of_oil
print("total oil:",oil_total)
total = rice_total + sugar_total + oil_total
print("total bill:",total)
total_integer = int(total)
print("total bill as integer:",total_integer)
total_string = str(total)
print("total bill as string:",total_string)
rice_total = float(rice_total)
sugar_total = float(sugar_total)
oil_total = float(oil_total)
import random
delivery_charge = random.randrange(5,10)
print(delivery_charge)
final_bill = total + delivery_charge
print("final bill amount",final_bill)

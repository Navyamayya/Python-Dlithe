"""Write a program to calculate the EB Bill.

The tariff rate for all division is the same. Karnataka electricity board single slaps for the domestic LT supply such as for 0 to 30 units the per-unit cost will be ? 3.75/-, from 31 to 100 the per-unit cost will be ? 5.20, from 101 to 200, the per-unit cost will be ? 6.75 and above 201 units you have to pay ? 7.8 per unit.
Additionally, the consumer will pay fixed charges as ? 60/- and electricity tax of 5% extra. """


unit=int(input())
if unit>201:
    x=unit-200
    cost= x * 7.8 + 30 * 3.75+70 * 5.2+100 * 6.75
elif unit <= 200 and unit > 100:
    x=unit-100
    cost= x * 6.75 + 30 * 3.75 + 70 * 5.2
elif unit <= 100 and unit > 30:
    x = unit - 30
    cost = x * 5.2 + 30 * 3.75
else:
    cost = unit * 3.75
Tax=cost*5/100
totalcost = cost + 60 + Tax
print("Bill Amount      : %10.2f"%cost)
print("Tax              : %10.2f"%Tax)
print("Additional charge: %10.2f"%60)
print("                 ------------")
print("Net Amount       : %10.2f"%totalcost)
print("                 ------------")







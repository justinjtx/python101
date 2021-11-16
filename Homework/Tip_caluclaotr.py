def percentagePlus(bill_total, tip_percentage):
    if tip_percentage >1:
        tip_percentage = tip_percentage / 100
        return bill_total + tip_percentage * bill_total

bt = float(input("what is the total bill? "))
tip_percentage = float(input('What percentage would you like to tip?'))

total = percentagePlus(tip_percentage=tip_percentage, bill_total=bt)

print(f'Your total bill is ${total}')
# def tipCalculator():
#     bill_per_person = percentagePlus(bill_total, tip_percent, members)
#     print("Total bill after tip: ${: 2f}".format(members * bill_per_person))
#     print("each person should pay: $" + str(bill_per_person))

# def percentagePlus(bill_total, tip_percent, members):
#     return (bill_total * (1 + (tip_percent/100) / members))


bill_total = float(input("what is the total bill?"))
tip_percentage = float(input("what percent would you like to tip?"))
group_member = int(input("How many people are in your group?"))

def percentage_calculator_split(bill_total, tip_percentage):
    total_before_split = bill_total * tip_percentage / 100 + bill_total
    return total_before_split

def percentage_plus(total_before_split, group_members):
    total_bill_after_split = total_before_split / group_member
    return total_bill_after_split

total = percentage_calculator_split(bill_total, tip_percentage)
print("Your total bill is: " + "$" + str(total))
print("Each person should pay: " + str (total / group_member)) 

from Exhibition import Exhibition
from StageEvent import StageEvent

print("Menu\n1.Exhibition\n2.Stage Event")
n = int(input("Enter Choice\n"))
#Fill your code here
if n == 1:
    no_of_stall = int(input("Enter number of stalls\n"))
    cost_stall = float(input("Enter cost per stalls\n"))
    no_entry = int(input("Enter number of entries to exhibition\n"))
    fee = float(input("Enter the entry fee\n"))

    obj = Exhibition(no_of_stall,cost_stall,no_entry,fee)
    tot_spent = obj.cal_total_spent()
    tot_rev = obj.cal_total_revenue()
    obj.display(tot_spent, tot_rev)
    obj.profit_or_loss(tot_spent, tot_rev)

    
else:
    no_of_eve = int(input("Enter number of Events\n"))
    cost_per_eve = float(input("Enter cost per Event\n"))
    entry = []
    fee = []
    for i in range(no_of_eve):
        num_entry = int(input("Enter the number of entries for {} event\n".format(i+1)))
        entry.append(num_entry)

        fees = float(input("Enter the entry fee\n"))
        fee.append(fees)

    obj = StageEvent(no_of_eve, cost_per_eve,entry,fee)
    tot_spent = obj.cal_total_spent()
    tot_rev = obj.cal_total_revenue()
    obj.display(tot_spent, tot_rev)
    obj.profit_or_loss(tot_spent, tot_rev)

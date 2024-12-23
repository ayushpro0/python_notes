from abc import ABCMeta
from Event import Event

class StageEvent(Event):
    def __init__(self,no_of_events, cost_per_event, no_of_entries, cost_per_entry):
        self.no_of_events = no_of_events
        self.cost_per_event = cost_per_event
        self.no_of_entries = no_of_entries
        self.cost_per_entry = cost_per_entry

    def cal_total_spent(self):
        #Fill your code here
        total = self.no_of_events * self.cost_per_event
        return total
    
    def cal_total_revenue(self):
        #Fill your code here
        total = 0
        for i in range(len(self.no_of_entries)):
            val = self.no_of_entries[i] * self.cost_per_entry[i]
            total += val
        return total

    def display(self, total_spent, total_revenue):
        #Fill your code here
        print("Number of events is {}\nTotal cost spent is {}\nTotal revenue is {}".format(self.no_of_events,total_spent,total_revenue))

    def profit_or_loss(self, total_spent, total_revenue):
        #Fill your code here
        val = total_revenue-total_spent
        if val>0:
            print("Profit")
        elif val<0:
            print("Loss")
        else:
            print("No profit, No loss")


from abc import ABCMeta
from Event import Event


class Exhibition(Event):

    def __init__(self, no_of_stalls, cost_per_stall, no_of_entries, cost_per_entry):
        self.no_of_stalls = no_of_stalls
        self.cost_per_stall = cost_per_stall
        self.no_of_entries = no_of_entries
        self.cost_per_entry = cost_per_entry

    def cal_total_spent(self):
        # Fill your code here
        return self.no_of_stalls * self.cost_per_stall

    def cal_total_revenue(self):
        # Fill your code here
        return self.no_of_entries * self.cost_per_entry

    def display(self, total_spent, total_revenue):
        # Fill your code here
        print(
            "Number of stall is {}\nTotal cost spent is {}\nTotal revenue is {}".format(self.no_of_stalls, total_spent,
                                                                                        total_revenue))

    def profit_or_loss(self, total_spent, total_revenue):
        # Fill your code here
        val = total_revenue - total_spent
        if val > 0:
            print("Profit")
        elif val < 0:
            print("Loss")
        else:
            print("No profit, No loss")

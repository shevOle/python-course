class Lottery:
    def __init__(self, number, budget, ended_at, winner):
        self.number = number
        self.budget = budget
        self.ended_at = ended_at
        self.winner = winner

    def show_info(self):
        print(f'Info about lottery run #{self.number}:')
        print(f' - lottery budget is set to ${self.budget:1.2f}')
        print(f' - lottery has ended at {self.ended_at}')
        if self.winner:
            print(f' - {self.winner} has won the lottery!')

lot1 = Lottery(1, 10000, '2024-11-11', None)
type(lot1)
print()

print(lot1.budget)
print(lot1.ended_at)
print(lot1.number)
print(lot1.winner)
print(lot1.show_info)
print()

lot1.show_info()
print()

lot2 = Lottery(2, 1000, '2024-11-12', 'Mike Wazovski')
lot2.show_info()
print()

lot3 = Lottery(3, 15000, '2024-11-13', None)
lot3.show_info()
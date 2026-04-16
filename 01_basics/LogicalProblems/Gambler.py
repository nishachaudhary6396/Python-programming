import random

stake = int(input("Enter stake: "))
goal = int(input("Enter goal: "))
trials = int(input("Enter number of trials: "))

wins = 0
for t in range(trials):
    cash = stake

    while cash > 0 and cash < goal:
        if random.random() < 0.5:
            cash += 1
        else:
            cash -= 1

    if cash == goal:
        wins += 1

print("Number of Wins:", wins)
print("Win Percentage:", (wins / trials) * 100)
print("Loss Percentage:", ((trials - wins) / trials) * 100)
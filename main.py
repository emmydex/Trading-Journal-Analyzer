import csv

# creating an empty list to store our data
trades = []

# this reads the information and stores it in a list of dictionaries
with open("journal.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row['profit'] = float(row["profit"])
        trades.append(row)

# this takes count of the amount of trades taken
total_trades = len(trades)

print("total trades:", total_trades)

winning_trades = 0
losing_trades = 0
total_profit = 0

for trade in trades:
    total_profit += trade["profit"]

    if trade["profit"]> 0:
        winning_trades += 1
    else:
        losing_trades += 1

win_rate = (winning_trades / total_trades) * 100

average_profit = total_profit / total_trades


print("\n=====TRADING REPORT=====")

print(f"total trades: {total_trades}")
print(f"winning trades: {winning_trades}")
print(f"losing trades: {losing_trades}")

print(f"\nwin rate: {win_rate:.2f}%")

print(f'total profit: ${total_profit:.2f}')
print(f"average profit: ${average_profit:.2f}")
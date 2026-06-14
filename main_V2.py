import csv


trades = []
with open("journal.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row['profit']= float(row["profit"])
        trades.append(row)

total_trades = len(trades)
print("total_trades:", total_trades)

# naming variables

winning_trades = 0
losing_trades = 0
total_trades = 0
total_profit = 0
best_trade = [0]
worst_trade = [0]

# handlling a zero division error
if total_trades > 0:
    win_rate = (winning_trades / total_trades) * 100
    average_profit = total_profit / total_trades
else:
    win_rate = 0
    average_profit = 0

for trade in trades:
    total_trades += trade["profit"]

    if trade["profit"] > 0:
        winning_trades += 1
    else:
        losing_trades += 1

# added statements for best trades and worst trades
    if trade["profit"] > best_trade["profit"]:
        best_trade = trade

    if trade["profit"] < worst_trade["profit"]:
        worst_trade = trade
#  calculating win rate and average profit
win_rate = (winning_trades / total_trades) * 100
average_profit = (total_profit / total_trades)



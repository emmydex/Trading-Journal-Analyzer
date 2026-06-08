import csv

# this opens and read file inside journal.csv
with open("journal.csv" , "r") as file:
    reader = csv.DictReader(file)

# stores trade inside a list 

trades = []

# counting of total trades
total_trades = len(trades)

winning_trades = 0 
losing_trades = 0
total_profit = 0

# reading profit value in row and appending it to trades
for row in reader:
    # here i converted to float data type for calculation
    row["profit"] = float(row["profit"])
    trades.append(row)
print("total trades: " , total_trades)


# coounting winning and losing trades
for trade in trades:
    total_trades += trade["profit"]

    # for empty file error handling
    if total_trades == 0:
        print("no trades found")



    if trade["profit"] > 0:
        winning_trades += 1
    else:
        losing_trades += 1

# calculating win rate
win_rate = (winning_trades/total_trades) * 100

#calculating average profit
average_profit = (total_profit/total_trades)


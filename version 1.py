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

    if trade["profit"] > 0:
        winning_trades += 1
    else:
        losing_trades += 1


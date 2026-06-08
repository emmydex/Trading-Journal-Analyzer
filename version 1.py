import csv
# stores trade inside a list 

trades = []

# this opens and read file inside journal.csv
with open("journal.csv" , "r") as file:
    reader = csv.DictReader(file)

        # reading profit value in row and appending it to trades
    for row in reader:
        # here i converted to float data type for calculation
        row["profit"] = float(row["profit"])
        trades.append(row)
        

 # counting of total trades
total_trades = len(trades)


# for empty file error handling
if total_trades == 0:
    print("no trades found")

# naming variables
winning_trades = 0 
losing_trades = 0
total_profit = 0



    # coounting winning and losing trades
for trade in trades:
        total_profit += trade["profit"]

        
        if trade["profit"] > 0:
            winning_trades += 1
        else:
            losing_trades += 1

    # calculating win rate
win_rate = (winning_trades/total_trades) * 100

    #calculating average profit
average_profit = (total_profit/total_trades)

print("\n======================")
print("   Trading report")
print("======================\n")
print("Total trades :", total_trades)
print("Winning Trades:" , winning_trades)
print("Losing Trades:", losing_trades)
print("total profit: $" ,total_profit)
print(f"win rate: ${win_rate:.1f}%")
print(f"Average Profit: ${average_profit:.2f}")
import csv

 # This script reads a CSV file named "journal.csv" containing trade data
 
trades = []

# The CSV file is expected to have a column named "profit" which contains the profit or loss for each trade.
with open("journal.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        # to avoid python reading the pairs as diffrent keys i used the .upper() to capitalize all
        row["pair"] = row["pair"].upper()

        # converting to a floating value
        row['profit']= float(row["profit"])
        trades.append(row)

total_trades = len(trades)


# empty file handling error
if total_trades == 0:
    print("no trades found")
    exit()

# naming variables

winning_trades = 0
losing_trades = 0
total_profit = 0
best_trade = trades[0]
worst_trade = trades[0]
gross_profit = 0
gross_loss = 0
current_win_streak = 0
current_loss_streak = 0
longest_win_streak = 0
longest_loss_streak = 0

# adding variables for total winnig profit and total losing profit
total_winning_profit = 0
total_losing_profit = 0

# creating an empty dictionary for the variable
pair_counts = {}

# Loop through each trade in the list of trades and calculate the total profit
for trade in trades:
    total_profit += trade["profit"]

    if trade["profit"] > 0:
        winning_trades += 1
    else:
        losing_trades += 1

    # if profit is positive
    if trade["profit"] > 0:
        gross_profit += trade["profit"]
        # becuase the win breaks the losing streak
        current_win_streak += 1
        current_loss_streak = 0

        total_winning_profit += trade["profit"]

    # checking new record and passing it back to current win streak if it is greater than the longest win streak
    if current_win_streak > longest_win_streak:
        longest_win_streak = current_win_streak


    # if profit is negative using abs to get the absolute value instead of a negative value
    if trade["profit"] < 0:
        gross_loss += abs(trade["profit"])

        current_loss_streak += 1
        current_win_streak = 0

        total_losing_profit += abs(trade["profit"])
    # same for losing streak
    if current_loss_streak > longest_loss_streak:
        longest_loss_streak = current_loss_streak

    # added statements for best trades and worst trades
    if trade["profit"] > best_trade["profit"]:
        best_trade = trade

    if trade["profit"] < worst_trade["profit"]:
        worst_trade = trade

    # adds pair to the dictionary else if pair already exist in the dictionary it is added to the existing one
    pair = trade["pair"]
    # is pair in the dictionary variable if not add to the dictionary
    if pair not in pair_counts:
        pair_counts[pair] = 1
    else:
        # else add to existing 
        pair_counts[pair] += 1


     # getting the first pair
    most_traded_pair = list(pair_counts.keys())[0]

    #looping through the dictionary
    for pair in pair_counts:

        # comparing counts
        if pair_counts[pair] > pair_counts[most_traded_pair]:
            most_traded_pair = pair

# handling the divisible by zero error
if gross_profit > 0 :
    profit_factor = gross_profit / gross_loss
else:
    profit_factor = 0

if winning_trades > 0:
    average_win =total_winning_profit / winning_trades
else:
    average_win = 0

if losing_trades > 0:
    average_loss = total_losing_profit / losing_trades
else:
    average_loss = 0

# calculating the profit factor
profit_factor = gross_profit / gross_loss

#  calculating win rate and average profit
win_rate = (winning_trades / total_trades) * 100
average_profit = (total_profit / total_trades)


# calculating average win
average_win = total_winning_profit / winning_trades

# calculating average loss
average_loss = total_losing_profit / losing_trades



print("\n======================")
print("Trading Report")
print("======================\n")
print("total_trades:", total_trades)
print("Winning Trades:", winning_trades)
print("Losing Trades:", losing_trades)
print(f"Total profit: ${total_profit:.2f}")
print(f"win rate: {win_rate:.2f}%")
print(f"average profit: ${average_profit:.2f}")
print("\nBest Trade:")
print("pair:", best_trade['pair'])
print(f"profit: ${best_trade['profit']:.2f}")

print("\nworst trade: ")
print("pair:", worst_trade["pair"])
print(f"profit: ${worst_trade['profit']:.2f}")

print("\nMost Traded pair:", most_traded_pair)
print("Trades:", pair_counts[most_traded_pair])


print(f"\n Gross Profit: ${gross_profit:.2f}")
print(f"Gross loss: ${gross_loss:.2f}")
print(f"Profit factor: {profit_factor:.2f}")

print("\n ===Streak log===")
print(f"Longest wining Streak: {longest_win_streak}")
print(f"Longest Losing Streak: {longest_loss_streak}")
import csv

# a function for loading and reading the csv file
def load_trades(filename):

    trades = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["pair"] = row["pair"].upper()
            row["profit"] = float(row["profit"])
            trades.append(row)

    return trades

# function for calculating metrics
def calculate_metrics(trades):

    winning_trades = 0
    losing_trades = 0
    total_profit = 0
    breakeven_trades = 0
    best_trade = trades[0]
    worst_trade = trades[0]

    for trade  in trades:
        if trade["profit"] > 0:
            winning_trades +=1

        # this is better if we factor in a breakeven trade
        #this handles a losing trade and a breakeven trade (profit == 0) would not be counted
        elif trade["profit"] < 0:
            losing_trades += 1
        
        # added a variable for break even trades
        else:
            breakeven_trades += 1

        #if trade["profit"] < 0:
        #    losing_trades += 1
       # there is no way best_trade and worst_trade are the same results
        if trade["profit"] > best_trade["profit"]:
            
            best_trade["profit"] = trade["profit"]

        if trade["profit"] < worst_trade["profit"]:
    
            worst_trade["profit"] = trade["profit"]

        total_profit += trade["profit"]

    total_trades = len(trades)
    

    return {
        "total_trades": total_trades,
        "winning_trades" : winning_trades,
        "losing_trades" : losing_trades,
        "total_profit" : total_profit,
        "best_trade" : best_trade["profit"],
        "worst_trade" : worst_trade["profit"]
    }



# a function for the prints
def print_header():
    print("\n=========================")
    print("Trading Report")
    print("=========================\n")


def main():

    print("calculating metrics...")

    trades = load_trades("journal.csv")

    metrics = calculate_metrics(trades)

    print_header()

    # ths looks cleaner
    print(f"Loaded {len(trades)} trades")

    print(metrics)

main()
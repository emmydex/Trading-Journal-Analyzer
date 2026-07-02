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
    gross_profit = 0
    gross_loss = 0
    current_win_streak = 0
    current_loss_streak = 0
    longest_win_streak =0
    longest_loss_streak = 0
    total_winning_profit = 0
    total_losing_profit = 0


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

        # NOTE:best_trade = trade makes the variable point to a diffrent dictionary.
        # while best_trade["profit"] = trade["profit"] changes the contents of the current dictionary

        if trade["profit"] > best_trade["profit"]:
            
            best_trade = trade

        if trade["profit"] < worst_trade["profit"]:
    
            worst_trade = trade

        if trade["profit"] > 0:
            gross_profit += trade["profit"]

            current_win_streak += 1
            current_loss_streak = 0

            total_winning_profit += trade["profit"]
            
        if current_win_streak > longest_win_streak:
            longest_win_streak = current_win_streak
            
        elif trade["profit"] < 0 :
            current_loss_streak += 1
            current_win_streak = 0
            gross_loss += abs(trade["profit"])
            total_losing_profit += trade["profit"]

        if current_loss_streak > longest_loss_streak:
            longest_loss_streak = current_loss_streak
        

        total_profit += trade["profit"]

    total_trades = len(trades)
    
    win_rate = (winning_trades / total_trades)* 100
    average_profit = (total_profit / total_trades)
    profit_factor = gross_profit/gross_loss
    average_win = total_winning_profit/winning_trades
    average_loss = total_losing_profit/losing_trades

    return {
        "total_trades": total_trades,
        "winning_trades" : winning_trades,
        "losing_trades" : losing_trades,
        "total_profit" : total_profit,
        "best_trade" : best_trade,
        "worst_trade" : worst_trade,
        'gross_loss' : gross_loss,
        "gross_profit" : gross_profit,
        "current_win_streak" : current_win_streak,
        "current_loss_streak": current_loss_streak,
        "longest_win_streak" : longest_win_streak,
        "longest_loss_streak" : longest_loss_streak,
        "total_winning_profit" : total_winning_profit,
        "total_losing_profit" : total_losing_profit,
        "breakeven_trades" : breakeven_trades,
        "win_rate" : win_rate,
        "average_profit" : average_profit,
        "profit_factor" : profit_factor,
        "average_win" : average_win,
        "average_loss" : average_loss
    }


def pair_performance(trades):
    pair_metrics = {}
    pair_counts = {}
    pair_profit = {}
    
    #for every trade
    for trade in trades:

        pair = trade["pair"]

        # update counter
        if pair not in pair_counts :
            pair_counts[pair] = 1
        else:
            pair_counts[pair] += 1

        profit = trade["pair"]

        #update accumulator
        if profit not in pair_profit :
            pair_profit[pair] = trade["profit"]
        else:
            pair_profit[pair] += trade["profit"]
       
    most_traded_pair = list(pair_counts.keys())[0]

    for pair in pair_counts :

        if pair_counts[pair] > pair_counts[most_traded_pair]:
            most_traded_pair = pair

        
    return {
        "most_traded_pair" : most_traded_pair,
        "pair_count" : pair_counts,
        "pair_profit" : pair_profit
    }
    
# a function for the prints
def print_header():
    print("\n=========================")
    print("Trading Report")
    print("=========================\n")


# a function for printing reports
def print_report(metrics,pair_metrics):
    best_trade = metrics["best_trade"]
    worst_trade = metrics["worst_trade"]
    print_header()
    print(" Trading Summary")
    print("___________________\n")
    print(f"Total trades : {metrics['total_trades']}")
    print(f'Winning Trades : {metrics["winning_trades"]}')
    print(f'Losing Trades : {metrics["losing_trades"]}')
    print(f"Breakeven Trades : {metrics['breakeven_trades']}")
    print("___________________\n")
    print("\n   Performance")
    print("___________________\n")
    print(f"Total Profit : ${metrics['total_profit']:.2f}")
    print(f"Win Rate : {metrics['win_rate']}%")
    print(f"Average Profit : ${metrics['average_profit']:.2f}")
    print("____________________")
    print("\n   Best Trade")
    print("____________________")
    print(f"Date : {best_trade['date']}")
    print(f"Pair: {best_trade['pair']}")
    print(f"Direction : {best_trade['direction']}")
    print(f"Entry : {best_trade['entry']}")
    print(f"Exit : {best_trade['exit']}")
    print(f"Profit : ${best_trade['profit']:.2f}")
    print("___________________\n")
    print("   Worst Trade")
    print("___________________")
    print(f"Date : {worst_trade['date']}")
    print(f"Pair: {worst_trade['pair']}")
    print(f"Direction: {worst_trade['direction']}")
    print(f"Entry : {worst_trade['entry']}")
    print(f'Exit : {worst_trade["exit"]}')
    print(f"Profit : ${worst_trade['profit']:.2f}")
    print("___________________\n")
    print("   Risk Metrics    ")
    print("___________________")
    print(f"Gross Profit : ${metrics['gross_profit']:.2f}")
    print(f"Gross Loss : ${metrics['gross_loss']:.2f}")
    print(f"Average Win : ${metrics['average_win']:.2f}")
    print(f"Average Loss : ${metrics['average_loss']:.2f}")
    print(f"Profit Factor : {metrics['profit_factor']}")
    print("___________________\n")
    print("   Streak Metrics    ")
    print("___________________")
    print(f"Current Win Streak : {metrics['current_win_streak']}")
    print(f"Current Loss Streak : {metrics['current_loss_streak']}")
    print(f"Longest Win Streak : {metrics['longest_win_streak']}")
    print(f"Longest loss Streak : {metrics['longest_loss_streak']}")
    print("_____________________\n")
    print("   Pair Performance   ")
    print("_____________________")
    print(f"Most Traded Pair : {pair_metrics['most_traded_pair']}")
    print(f"Pair Count :{pair_metrics['pair_count']}")
    print(f"Pair Profit : {pair_metrics['pair_profit']}")



def main():

    print("calculating metrics...")

    trades = load_trades("journal.csv")

    metrics = calculate_metrics(trades)
    pair_metrics = pair_performance(trades)


    # print_header()
    print_report(metrics,pair_metrics) 



    



    
    

main()
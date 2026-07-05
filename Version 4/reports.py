# a function for the prints
def print_header():
    print("\n=========================")
    print("Trading Report")
    print("=========================\n")


# a function for printing reports
def print_report(metrics,pair_metrics):
    pair_count = metrics["best_trade"]
    pair_profit = metrics["worst_trade"]
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
    print(f"Average Loss : ${abs(metrics['average_loss']):.2f}")
    print(f"Profit Factor : {metrics['profit_factor']:.2f}")
    print("___________________\n")
    print("   Streak Metrics    ")
    print("___________________")
    print(f"Current Win Streak : {metrics['current_win_streak']}")
    print(f"Current Loss Streak : {metrics['current_loss_streak']}")
    print(f"Longest Win Streak : {metrics['longest_win_streak']}")
    print(f"Longest loss Streak : {metrics['longest_loss_streak']}")
    print("_____________________\n")
    print("   Pair Performance   ")
    print("_____________________\n")
    print(f"Most Traded Pair : {pair_metrics['most_traded_pair']}\n")

    pair_count = pair_metrics["pair_count"]
    pair_profit = pair_metrics["pair_profit"]

    for pair in pair_count:
        print(pair)
        print("-------------")
        print(f"Trades : {pair_count[pair]}")
        print(f"Profit : ${pair_profit[pair]}")
        print("________________\n")
        
import csv

trades = []
with open("journal.csv", "r") as file:
    reader = csv.DicctReader(file)

    for row in reader:
        row['profit'] = float(row["profit"])
        trades.append(row)

total_trades = len(trades)
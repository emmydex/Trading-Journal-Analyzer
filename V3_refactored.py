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



# a function for the prints
def print_header():
    print("\n=========================")
    print("Trading Report")
    print("=========================\n")


def main():
    trades = load_trades("journal.csv")

    print_header()

    print(trades)

main()
#wooooow
from csv_loader import load_trades

from calculations import calculate_metrics
from calculations import pair_performance
from reports import print_header
from reports import print_report
    

def main():
    # changed the csv file
    # there is an error
    # the .csv file is empty
    trades = load_trades("3_month_data.csv")
    metrics = calculate_metrics(trades)
    pair_metrics = pair_performance(trades)
    # print_header()
    print_report(metrics,pair_metrics) 

if __name__ == "__main__":
    main()
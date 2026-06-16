# Trading Journal Analyzer
a program that helps traders analyze their trading performance by reading trade records from a CSV file and generating useful statistics.

---

## Problem statement

Many traders like me take trades every day but do not track their performance properly.

Without data, it is difficult to answer questions like:

- Am I profitable?
- What is my win rate?
- where are my loosing streaks
- How many trades have I taken?
- Am I improving over time?

This project solves that problem by automatically analyzing a trading journal.

---

## Features

✅ Read trade data from a CSV file

✅ Count total trades

✅ Count winning trades

✅ Count losing trades

✅ Calculate win rate

✅ Calculate total profit/loss

✅ Calculate average profit per trade

---

## Technologies Used

- Python
- CSV File Handling
- Loops
- Functions
- Conditional Statements

---

## Project Structure

```text
trading-journal-analyzer/
│
├── main.py
├── journal.csv
├── reports/
└── README.md
```

## Sample Trade Data

```csv
date,pair,direction,entry,exit,profit
2026-06-01,EURUSD,BUY,1.0800,1.0850,50
2026-06-02,GBPUSD,SELL,1.2700,1.2650,40
2026-06-03,XAUUSD,BUY,3350,3340,-100
```

## Example Output

```text
===== TRADING REPORT =====

Total Trades: 3

Winning Trades: 2

Losing Trades: 1

Win Rate: 66.67%

Total Profit: -10

Average Profit: -3.33
```

## How To Run

Clone the repository:

```bash
git clone https://github.com/emmydex/Trading-Journal-Analyzer.git
```

Navigate into the project folder:

```bash
cd trading-journal-analyzer
```

Run the program:

```bash
python main.py
```

---


## VERSION RELEASED

# Trading Journal Analyzer V1

- CSV trade loading
- Win/loss tracking
- Profit calculations
- Average profit
- Win rate
- Empty file handling


# Trading Journal Analyzer V2

- Best trade analysis
- Worst trade analysis
- Trade detail reporting
- Pair normalization
- Most traded pair analysis
- Improved reporting




## Future Improvements

### Versions
- Monthly performance reports
- Best trade analysis
- Worst trade analysis
- Profit factor calculation
- Performance charts using Matplotlib
- Equity curve visualization
- GUI using Tkinter
- AI-powered trading insights

---

## Skills Demonstrated

- Python Programming
- Data Analysis
- File Handling
- Problem Solving
- Financial Data Processing
- data quality
---

## Author

olúwáfẹ́mi🍀

LinkedIn:
https://www.linkedin.com/in/oluwafemi69
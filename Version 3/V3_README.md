# 📊 Trading Journal Analyzer (Version 3)

## Overview

The Trading Journal Analyzer is a Python project that analyzes trading history stored in a CSV file and generates useful trading statistics.

The goal of this project is to transform raw trading data into meaningful insights that help traders evaluate their performance and improve their decision-making.

Version 3 focuses on **refactoring, cleaner architecture, and improved analytics**, making the project easier to maintain and prepare for a future graphical user interface (GUI).


---

## Features

### 📂 CSV Journal Loading

* Reads trading data from a CSV file
* Automatically converts profit values to numbers
* Standardizes currency pair names (uppercase)

---



### 📈 Trading Summary

* Total Trades
* Winning Trades
* Losing Trades
* Breakeven Trades

### 💰 Performance Metrics

* Total Profit
* Win Rate
* Average Profit per Trade

### 🏆 Trade Analysis

* Best Trade
* Worst Trade

### ⚠️ Risk Metrics

* Gross Profit
* Gross Loss
* Average Winning Trade
* Average Losing Trade
* Profit Factor

### 🔥 Streak Metrics

* Current Winning Streak
* Current Losing Streak
* Longest Winning Streak
* Longest Losing Streak

### 💹 Pair Performance

* Most Traded Pair
* Trades per Currency Pair
* Total Profit per Currency Pair

---

# 🏗️ Refactoring Improvements

Version 3 introduces a cleaner software design by separating responsibilities into dedicated functions.

Example project flow:

```
main()
│
├── load_trades()
├── calculate_metrics()
├── pair_performance()
└── print_report()
```

Each function performs a single responsibility, making the project easier to maintain, debug, and expand.

---

# 🧠 Python Concepts Practiced

This version reinforces many core Python concepts:

* Functions
* Lists
* Dictionaries
* Nested Dictionaries
* For Loops
* Conditional Statements
* Counters
* Accumulators
* Returning Dictionaries
* Refactoring
* Function Parameters
* Clean Code Principles

---

# 📋 Sample Report

```
Trading Summary
-----------------------

Total Trades : 4
Winning Trades : 3
Losing Trades : 1
Breakeven Trades : 0

Performance
-----------------------

Total Profit : $-7.49
Win Rate : 75.00%
Average Profit : $-1.87

Risk Metrics
-----------------------

Gross Profit : $92.51
Gross Loss : $100.00
Profit Factor : 0.93

Pair Performance
-----------------------

Most Traded Pair : GBPUSD

EURUSD
Trades : 1
Profit : $50.00

GBPUSD
Trades : 2
Profit : $42.51

XAUUSD
Trades : 1
Profit : $-100.00
```

---

# 🎯 What I Learned

Building Version 3 helped me understand:

* How to break a large program into smaller functions.
* The importance of separating calculations from presentation.
* How counters and accumulators solve different problems.
* How nested dictionaries organize related information.
* Why dynamic loops are better than hardcoded values.
* How to debug Python using error messages and variable inspection.
* How refactoring improves readability and maintainability.

---

# 🚀 Next Version

Version 4 will transform the console application into a graphical desktop application with:

* Interactive GUI
* Buttons
* Tables
* Better report visualization
* Improved user experience
* Future support for charts and data visualization

---

## 🛠️ Technologies

* Python
* Dictionaries
* Functions
* Git
* GitHub

---

## 👨‍💻 Author

Built by **Oluwafemi 🍀**

Learning Python through real-world software projects.

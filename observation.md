# Trading Journal Analyzer

## Project Overview

This is a Python project that reads trading data from a CSV file and generates useful trading statistics such as total trades, winning trades, losing trades, total profit, average profit, win rate, best trade, and worst trade.

The goal of the project was to practice core Python programming concepts while building a practical data analysis tool.

---

## Key Observations

### 1. CSV Data is Read as Strings

One of the first observations made during development was that all values loaded from a CSV file are stored as strings by default.

Example:

```python
row["profit"]
```

returns:

```python
"50"
```

instead of:

```python
50
```

This required converting profit values to floats before performing calculations.

```python
row["profit"] = float(row["profit"])
```

---

### 2. Dictionaries are Useful for Structured Data

Each trade was stored as a dictionary.

Example:

```python
{
    "pair": "EURUSD",
    "profit": 50.0
}
```

This made it easy to access specific trade information using keys such as:

```python
trade["profit"]
trade["pair"]
```

---

### 3. Counters and Accumulators are Common Programming Patterns

The project introduced two important programming concepts:

#### Counter

Used for counting events.

```python
winning_trades += 1
```

#### Accumulator

Used for building a running total.

```python
total_profit += trade["profit"]
```

These patterns are widely used in data analysis and software development.

---

### 4. Defensive Programming Prevents Crashes

A division-by-zero error occurred when calculating win rate and average profit on an empty dataset.

Example:

```python
win_rate = winning_trades / total_trades
```

If:

```python
total_trades = 0
```

Python raises:

```text
ZeroDivisionError
```

Adding validation checks improved the reliability of the application.

---

### 5. Variable Reassignment Can Cause Bugs

During development, the variable:

```python
total_trades
```

was accidentally reset to:

```python
total_trades = 0
```

after already being assigned the correct value.

This caused incorrect calculations and division-by-zero errors.

This reinforced the importance of tracking variable state throughout a program.

---

### 6. Best and Worst Trade Analysis Requires Comparisons

To identify the best and worst trades, the program compared each trade's profit against the current best and worst values.

Example:

```python
if trade["profit"] > best_trade["profit"]:
    best_trade = trade
```

This introduced the concept of maintaining a current "best" and "worst" record while iterating through data.

---

### 7. Data Normalization Improves Accuracy

An issue was discovered when trading pairs used different capitalization.

Example:

```text
GBPUSD
gbpusd
```

Although they represent the same currency pair, Python treated them as different strings.

Converting all pair names to uppercase solved this problem.

```python
row["pair"] = row["pair"].upper()
```

This process is known as data normalization.

---

### 8. A High Win Rate Does Not Guarantee Profitability

A notable result from testing was:

```text
Winning Trades: 3
Losing Trades: 1
Win Rate: 75%
Total Profit: -7.49
```

This demonstrated an important trading principle:

A trader can win most trades but still lose money if losses are significantly larger than wins.

---

## Skills Practiced

* Python fundamentals
* Lists
* Dictionaries
* Loops
* Conditional statements
* File handling
* CSV processing
* Data cleaning/quality
* Error handling
* Basic trading analytics
* Debugging and problem solving

---

## Future Improvements

Future versions of the project may include:

* Most traded pair analysis
* Profit factor calculation
* Monthly performance reports
* Trade filtering
* Data visualization and charts
* Exporting reports
* Graphical user interface (GUI)

---

## Conclusion

This project provided practical experience with Python data processing and analytics. It demonstrated how raw trading data can be transformed into meaningful statistics while reinforcing core software development concepts such as loops, dictionaries, error handling, debugging, and data normalization.


## Author

olúwáfẹ́mi🍀

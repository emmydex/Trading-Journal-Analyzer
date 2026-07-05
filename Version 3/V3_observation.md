# Observations (Version 3)

## Overview

Version 3 marked a major shift from simply writing Python code to designing maintainable software.

The focus was no longer just on producing the correct output, but also on organizing code into reusable functions with clear responsibilities.

---

## Key Learning Points

### 1. Counters vs Accumulators

One of the most important concepts learned during Version 3 was understanding the difference between counters and accumulators.

Counter examples:

* Winning trades
* Losing trades
* Pair counts

Accumulator examples:

* Total profit
* Gross profit
* Gross loss
* Pair profit

This distinction made metric calculations much easier to design.

---

### 2. Dictionary Design

A major breakthrough came from understanding that dictionary keys should represent what we want to look up.

Example:

```python
pair_profit = {
    "EURUSD": 50,
    "GBPUSD": 42.51
}
```

The currency pair serves as the key, while the accumulated profit becomes the value.

---

### 3. Refactoring

Large blocks of code were separated into dedicated functions including:

* load_trades()
* calculate_metrics()
* pair_performance()
* print_header()

This significantly improved readability and maintainability.

---

### 4. Software Engineering

Instead of asking only "Does the code work?", the project began asking questions like:

* Should this logic belong in another function?
* What should this function return?
* What responsibility should this function have?

This represents an important step toward software engineering practices.

---

### 5. Debugging Skills

Several bugs were solved through reasoning rather than trial and error.

Examples included:

* TypeError
* ZeroDivisionError
* Dictionary reference mistakes
* Variable scope issues
* Incorrect accumulator logic

---

## Biggest Takeaway

The biggest lesson from Version 3 was that understanding the data is more important than memorizing Python syntax.

Once the data model became clear, implementing the code became much easier.

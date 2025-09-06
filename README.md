# Debugging & Documentation — Python, HTML/JS

Hands-on exercises to practice using ChatGPT to **identify**, **explain**, and **fix** bugs across small Python programs and a simple HTML/JavaScript page. Each task includes the original issue, the root cause, and a corrected implementation with run instructions.

> Repository: `holbertonschool-chatgpt-introduction`  
> Directory: `debugging/`

---

## Table of Contents

1. [Task 0 — Python Factorial (Iterative)](#task-0--python-factorial-iterative)
2. [Task 1 — Python Arguments Printing](#task-1--python-arguments-printing)
3. [Task 2 — HTML/JavaScript Background Color](#task-2--htmljavascript-background-color)
4. [Task 3 — Python Minesweeper (Win Detection)](#task-3--python-minesweeper-win-detection)
5. [Task 4 — Python Factorial (Recursive, Docs)](#task-4--python-factorial-recursive-docs)
6. [Task 5 — Python Checkbook (Error Handling)](#task-5--python-checkbook-error-handling)
7. [Task 6 — Python Tic-Tac-Toe (Robust I/O)](#task-6--python-tic-tac-toe-robust-io)
8. [How to Run](#how-to-run)
9. [Testing Tips](#testing-tips)
10. [License](#license)

---

## Task 0 — Python Factorial (Iterative)

**Original issue:** Infinite loop; `n` never changes inside the `while` loop.  
**Fix:** Use a `for` loop (or decrement `n`) and validate input.

**File:** `factorial.py`
```python
#!/usr/bin/python3
import sys


def factorial(n):
    """Return n! for n >= 0 (iterative)."""
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <non-negative-integer>")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Error: argument must be an integer")
        sys.exit(1)

    print(factorial(n))

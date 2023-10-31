# Fibonacci Calculator

This repository contains a Python script, `fibonacci.py`, that allows you to calculate the Fibonacci sequence and retrieve a list of Fibonacci numbers within a specified range.

## Usage

### Calculate the Nth Fibonacci Number
To calculate the Nth Fibonacci number, use the `fibonacci(n)` function. It takes a positive integer `n` as input and returns the Fibonacci number at the Nth position. For example:
```python
from fibonacci import fibonacci

n = 10
result = fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")
```

### Calculate a Range of Fibonacci Numbers
You can also calculate a range of Fibonacci numbers between a starting and ending position using the `fibonacci_array(start, end)` function. It takes two positive integers, `start` and `end`, as input and returns a list of Fibonacci numbers within that range. For example:
```python
from fibonacci import fibonacci_array

start = 5
end = 15
result = fibonacci_array(start, end)
print(f"Fibonacci numbers from {start} to {end}: {result}")
```

### Command Line Usage
The script can be executed from the command line, providing the `start` and `end` values as arguments. For example:
```bash
python fibonacci.py 5 15
```

## Error Handling
The script includes error handling to ensure that the input is valid. It will raise a `TypeError` if the input is not an integer, a `ValueError` if the input is not a positive integer, or if the `start` value is greater than the `end` value when calculating a range.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it according to the terms of the license.

If you encounter any issues or have questions, please open an issue in this repository. We welcome contributions and improvements as well.

Happy Fibonacci calculating!
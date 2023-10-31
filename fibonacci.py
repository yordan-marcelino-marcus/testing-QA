import sys
def validate_number_for_fibonacci(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    elif n <= 0:
        raise ValueError("Input must be a positive integer")
    
def fibonacci(n):
    validate_number_for_fibonacci(n)
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_array(start, end):
    validate_number_for_fibonacci(start)
    validate_number_for_fibonacci(end)
    if start > end:
        raise ValueError("end must be after start")
    fib_array = []
    for i in range(start, end+1):
        fib_array.append(fibonacci(i))
    return fib_array

if __name__ == '__main__':
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    print(fibonacci_array(start, end))
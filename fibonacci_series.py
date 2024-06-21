from typing import List
def fibonacci_series(n: int) -> List[int]:
    series = []
    if n <= 0:
        return series
    elif n == 1:
        series.append(0)
        return series
    else:
        series = [0, 1]
        while len(series) < n:
            series.append(series[-1] + series[-2])
        return series

def main():
    n = int(input("Enter the number of terms in the Fibonacci series: "))
    series = fibonacci_series(n)
    print("Fibonacci series:")
    for num in series:
        print(num)

if __name__ == "__main__":
    main()
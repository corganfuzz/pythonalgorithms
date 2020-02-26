# Uses python3
import sys


def gcd_opt(first, second):
    max_number = max(first, second)
    min_number = min(first, second)
    remainder = max_number % min_number

    if remainder == 0:
        return min_number
    else:
        return gcd_opt(min_number, remainder)


def lcm_opt(x, y):
    if x == 0 or y == 0:
        return 0
    else:
        return (x*y) / gcd_opt(x, y)


if __name__ == "__main__":
    numbers = sys.stdin.readline()
    a, b = map(int, numbers.split())
    print(round(lcm_opt(a, b)))

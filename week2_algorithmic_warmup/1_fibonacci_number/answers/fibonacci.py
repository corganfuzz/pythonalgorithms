# Uses python3


def calc_fib(x):
    first_fib = 0
    second_fib = 1
    if x <= 1:
        return x
    else:
        for i in range(1, x):
            sum_fib = first_fib + second_fib
            first_fib = second_fib
            second_fib = sum_fib
    return second_fib


def last_digit(x):
    string_number = str(calc_fib(x))
    last_num = string_number[-1:]
    return last_num


number = int(input())
print(last_digit(number))


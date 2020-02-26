# Uses python3


# def calc_fib(x):
#     if x <= 1:
#         return x
#
#     return calc_fib(x - 1) + calc_fib(x - 2)
#
#
# n = int(input())
# print(calc_fib(n))

def calc_fib(x):

    first_fib = 0
    second_fib = 1

    if x <= 1:
        return x
    else:
        for i in range(1, x):
            sum_fib = first_fib + second_fib
            # print('second', second_fib)
            first_fib = second_fib
            second_fib = sum_fib
            # # print('after', second_fib)
            # print('sum', sum_fib, 'first', first_fib)
    return second_fib


number = int(input())
print(calc_fib(number))

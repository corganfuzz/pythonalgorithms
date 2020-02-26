
# def max_pairwise_product(numbers):
#
#     n = len(numbers)
#     max_product = 0
#     for first in range(n):
#         for second in range(first + 1, n):
#             multiplication_in_between = numbers[first] * numbers[second]
#             max_product = max(max_product, multiplication_in_between)
#     return max_product


def optimal_pairwise(numbers):
    n = len(numbers)

    numbers.sort()
    firstmax = max(numbers)
    secondmax = numbers[-2]

    max_product = int(float(firstmax * secondmax))

    return max_product


if __name__ == '__main__':

    provided_numbers = int(float(input()))
    converted_numbers_toIntegers = [int(float(x)) for x in input().split()]

    # print(max_pairwise_product(converted_numbers_toIntegers))

    print('the test', optimal_pairwise(converted_numbers_toIntegers))





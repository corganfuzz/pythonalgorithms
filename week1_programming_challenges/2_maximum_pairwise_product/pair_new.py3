# python3


def optimal_pairwise(numbers):
    numbers.sort()
    firstmax = max(numbers)
    secondmax = numbers[-2]
    max_product = firstmax * secondmax
    return max_product


if __name__ == '__main__':
    provided_numbers = int(float(input()))
    converted_numbers_toIntegers = [int(float(x)) for x in input().split()]
    print(optimal_pairwise(converted_numbers_toIntegers))
# Uses python3
import sys


def get_change(money):
    coin_number = 0
    while money > 0:
        if money >= 10:
            money = money - 10
            print('in 10', coin_number)
        elif money >= 5:
            money = money - 5
            print('in 5', coin_number)
        else:
            money = money - 1
            print('in 1', coin_number)
        coin_number = coin_number + 1
    return coin_number


if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))

    array = [8, 1, 0, 1]

    print(array.index())

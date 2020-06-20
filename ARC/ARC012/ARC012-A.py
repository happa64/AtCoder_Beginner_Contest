# https://atcoder.jp/contests/arc012/submissions/14484036
# A - 週末
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    day = input()
    if day == "Monday":
        print(5)
    elif day == "Tuesday":
        print(4)
    elif day == "Wednesday":
        print(3)
    elif day == "Thursday":
        print(2)
    elif day == "Friday":
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    resolve()

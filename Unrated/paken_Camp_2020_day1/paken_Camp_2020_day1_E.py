# https://atcoder.jp/contests/pakencamp-2020-day1/tasks/pakencamp_2020_day1_e
# E - Amary
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x, y = map(int, input().split())

    if x == y == 0:
        print(1, 1)
    elif x == y:
        print(-1)
    elif x > y:
        print(x, 2 * x + y)
    else:
        print(x + 2 * y, y)


if __name__ == '__main__':
    resolve()

# https://atcoder.jp/contests/abc162/tasks/abc162_b
# B - FizzBuzz Sum
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    res = 0
    for i in range(1, n + 1):
        if i % 3 != 0 and i % 5 != 0:
            res += i

    print(res)


if __name__ == '__main__':
    resolve()

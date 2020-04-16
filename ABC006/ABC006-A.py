# https://atcoder.jp/contests/abc006/tasks/abc006_1
# A - 世界のFizzBuzz
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    if n % 3 == 0:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    resolve()

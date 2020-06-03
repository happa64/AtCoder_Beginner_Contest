# https://atcoder.jp/contests/agc024/tasks/agc024_a
# A - Fairness
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c, k = map(int, input().split())

    # 髙橋君と中橋君の整数の差の絶対値は不変である
    res = a - b
    # 操作回数が奇数の場合、-1をかける
    op = 1 if k % 2 == 0 else -1
    if abs(res) > 10 ** 18:
        print("Unfair")
    else:
        print(res * op)


if __name__ == '__main__':
    resolve()

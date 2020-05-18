# https://atcoder.jp/contests/abc168/submissions/13294435
# B - ... (Triple Dots)
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    k = int(input())
    s = input()
    n = len(s)
    if n <= k:
        print(s)
    else:
        print(s[:k] + "...")


if __name__ == '__main__':
    resolve()

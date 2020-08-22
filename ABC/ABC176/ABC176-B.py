# https://atcoder.jp/contests/abc176/submissions/16108292
# B - Multiple of 9
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = list(map(int, input()))

    s = 0
    for num in n:
        s += num
        s %= 9

    print("Yes" if s == 0 else "No")


if __name__ == '__main__':
    resolve()

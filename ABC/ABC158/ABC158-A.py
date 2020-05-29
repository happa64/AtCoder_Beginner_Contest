# https://atcoder.jp/contests/abc158/submissions/13123454
# A - Station and Bus
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = list(input())
    if len(set(s)) != 1:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    resolve()

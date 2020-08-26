# https://atcoder.jp/contests/joi2019yo/submissions/16237629
# C - マルバツスタンプ (Circle Cross Stamps)
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    s = input()

    i = 0
    res = 0
    while i < n - 1:
        if (s[i] == "X" and s[i + 1] == "O") or (s[i] == "O" and s[i + 1] == "X"):
            res += 1
            i += 2
        else:
            i += 1
    print(res)


if __name__ == '__main__':
    resolve()

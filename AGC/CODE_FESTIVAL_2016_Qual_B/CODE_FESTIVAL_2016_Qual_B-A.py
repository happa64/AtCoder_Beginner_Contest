# https://atcoder.jp/contests/code-festival-2016-qualb/submissions/13757241
# A - Signboard
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()

    res = 0
    for i, j in zip(s, "CODEFESTIVAL2016"):
        if i != j:
            res += 1
    print(res)


if __name__ == '__main__':
    resolve()

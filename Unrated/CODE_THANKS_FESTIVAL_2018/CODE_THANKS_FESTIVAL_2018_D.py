# https://atcoder.jp/contests/code-thanks-festival-2018-open/submissions/16819686
# D - Concatenation
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input()

    res = 0
    head = S[0]
    for s in S:
        if head >= s:
            res += 1
            head = s
    print(res)


if __name__ == '__main__':
    resolve()

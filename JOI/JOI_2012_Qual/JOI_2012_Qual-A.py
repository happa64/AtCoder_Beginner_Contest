# https://atcoder.jp/contests/joi2012yo/submissions/15056656
# A - ランチ (Lunch)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    P = list(int(input()) for _ in range(3))
    J = list(int(input()) for _ in range(2))

    res = f_inf
    for p in P:
        for j in J:
            res = min(res, p + j - 50)
    print(res)


if __name__ == '__main__':
    resolve()

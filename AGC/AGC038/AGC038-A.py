# https://atcoder.jp/contests/agc038/submissions/14639842
# A - 01 Matrix
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W, A, B = map(int, input().split())

    res = []
    L1 = ["1"] * A + ["0"] * (W - A)
    for _ in range(B):
        res.append("".join(L1))
    L2 = ["0"] * A + ["1"] * (W - A)
    for _ in range(H - B):
        res.append("".join(L2))
    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()

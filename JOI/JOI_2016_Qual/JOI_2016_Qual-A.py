# https://atcoder.jp/contests/joi2016yo/submissions/15096327
# A - 科目選択 (Selecting Subjects)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    L = list(int(input()) for _ in range(6))
    ABCD, EF = sorted(L[:4], reverse=True), sorted(L[4:], reverse=True)
    res = sum(ABCD[:3]) + EF[0]
    print(res)


if __name__ == '__main__':
    resolve()

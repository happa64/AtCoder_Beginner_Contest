# https://atcoder.jp/contests/abc175/submissions/15908487
# A - Rainy Season
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input()
    res = 0
    cnt = 0
    for s in S:
        if s == "R":
            cnt += 1
            res = max(res, cnt)
        else:
            cnt = 0
    print(res)


if __name__ == '__main__':
    resolve()

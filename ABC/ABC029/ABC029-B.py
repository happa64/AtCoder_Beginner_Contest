# https://atcoder.jp/contests/abc029/submissions/13993521
# B - カキ
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    res = 0
    for _ in range(12):
        S = input()
        for s in S:
            if s == "r":
                res += 1
                break
    print(res)


if __name__ == '__main__':
    resolve()

# https://atcoder.jp/contests/agc034/submissions/14695287
# B - ABC
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input().replace("BC", "D")

    res = 0
    cnt = 0
    for s in S:
        if s == "A":
            cnt += 1
        elif s == "D":
            res += cnt
        else:
            cnt = 0
    print(res)


if __name__ == '__main__':
    resolve()

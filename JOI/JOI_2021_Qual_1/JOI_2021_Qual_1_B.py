# https://atcoder.jp/contests/joi2021yo1a/submissions/16942901
# B - JOI ソート (JOI Sort)
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = input()
    cnt = Counter(S)

    res = ""
    for s in ["J", "O", "I"]:
        for _ in range(cnt[s]):
            res += s
    print(res)


if __name__ == '__main__':
    resolve()

# https://atcoder.jp/contests/abc008/tasks/abc008_2
# B - 投票
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = list(input() for _ in range(n))
    D = Counter(S)
    res = ""
    m = 0
    for k, v in D.items():
        if m < v:
            m = v
            res = k
    print(res)


if __name__ == '__main__':
    resolve()

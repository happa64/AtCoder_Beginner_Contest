# https://atcoder.jp/contests/code-festival-2015-qualb/submissions/13451870
# B - 採点
import sys
from collections import Counter
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))

    D = Counter(A)
    res = []
    for k, v in D.items():
        if v > n / 2:
            res.append(k)

    print("?") if len(res) == 0 else print(*res)


if __name__ == '__main__':
    resolve()

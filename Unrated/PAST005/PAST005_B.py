# https://atcoder.jp/contests/past202012-open/submissions/19042583
# B - 上書き
import sys
from collections import Counter
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = input()

    D = Counter(S)
    res = ""
    for s in S:
        if D[s] == 1:
            res += s
        elif D[s] > 1:
            D[s] -= 1
    print(res)


if __name__ == '__main__':
    resolve()

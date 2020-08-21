# https://atcoder.jp/contests/arc017/submissions/16071209
# C - 無駄なものが嫌いな人
import sys
from itertools import product
from collections import Counter

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, x = map(int, input().split())
    W = list(int(input()) for _ in range(n))

    if n % 2 == 0:
        s = t = n // 2
    else:
        s = n // 2
        t = (n + 1) // 2

    W1 = W[:s]
    W2 = W[s:]

    S = []
    for pattern in product([0, 1], repeat=s):
        tmp = 0
        for idx, p in enumerate(pattern):
            if p == 1:
                tmp += W1[idx]
        S.append(tmp)

    T = []
    for pattern in product([0, 1], repeat=t):
        tmp = 0
        for idx, p in enumerate(pattern):
            if p == 1:
                tmp += W2[idx]
        T.append(tmp)

    D = Counter(T)
    res = 0
    for num in S:
        res += D.get(x - num, 0)
    print(res)


if __name__ == '__main__':
    resolve()

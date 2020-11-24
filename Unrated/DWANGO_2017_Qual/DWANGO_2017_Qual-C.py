# https://atcoder.jp/contests/dwacon2017-prelims/submissions/18386125
# C - スキーリフトの相乗り
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    res = 0
    D = defaultdict(int)
    for _ in range(n):
        a = int(input())
        if a != 4:
            D[a] += 1
        else:
            res += 1

    if D[1] < D[3]:
        res += D[1]
        D[3] -= D[1]
        D[1] = 0
    else:
        res += D[3]
        D[1] -= D[3]
        D[3] = 0

    res += D[3]

    res += D[2] // 2
    D[2] = 0 if D[2] % 2 == 0 else 1

    if D[2]:
        res += 1
        D[2] -= 1
        if D[1]:
            D[1] -= 1 if D[1] == 1 else 2

    res += (D[1] + 3) // 4
    print(res)


if __name__ == '__main__':
    resolve()

# https://atcoder.jp/contests/keyence2021/submissions/19466500
# B - Mex Boxes
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    MAX_A = max(A)

    D = Counter(A)
    mi = k
    res = 0
    for i in range(MAX_A + 2):
        if D[i] == 0:
            res += i * mi
            break
        cnt = min(mi, D[i])
        if cnt < mi:
            res += i * (mi - cnt)
            mi = D[i]
    print(res)


if __name__ == '__main__':
    resolve()

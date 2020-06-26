# https://atcoder.jp/contests/abc171/submissions/14689504
# D - Replacing
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    query = [list(map(int, input().split())) for _ in range(q)]

    D = Counter(A)
    res = sum(A)
    for b, c in query:
        if D.get(b) is not None:
            res -= b * D.get(b)
            res += c * D.get(b)

        if D.get(c) is not None:
            D[c] += D[b]
        else:
            D[c] = D[b]
        D[b] = 0

        print(res)


if __name__ == '__main__':
    resolve()

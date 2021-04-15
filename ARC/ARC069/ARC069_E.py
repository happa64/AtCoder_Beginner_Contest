# https://atcoder.jp/contests/arc069/submissions/21776605
# E - Frequency
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    A = list(map(int, input().split()))

    D = Counter(A)
    L = sorted(set(A), reverse=True)
    IND = dict()
    for i in range(n):
        IND[A[i]] = min(IND.get(A[i], f_inf), i)

    res = [0] * n
    for i, now in enumerate(L):
        idx = IND[now]
        if i + 1 < len(L):
            nxt = L[i + 1]
            diff = now - nxt
            res[idx] += diff * D[now]
            D[nxt] += D[now]
            IND[nxt] = min(IND[nxt], IND[now])
        else:
            res[idx] += now * D[now]

    print(*res, sep="\n")


if __name__ == '__main__':
    solve()

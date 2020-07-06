# https://atcoder.jp/contests/abc173/submissions/15038818
# E - Multiplication 4
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    M, P = [], []
    for a in A:
        M.append(a) if a < 0 else P.append(a)

    m, p = len(M), len(P)
    ok = False
    if p > 0:
        ok = m % 2 == 0 if n == k else True
    else:
        ok = k % 2 == 0

    res = 1
    if not ok:
        A.sort(key=lambda x: abs(x))
        for i in range(k):
            res = (res * A[i]) % mod
    else:
        P.sort()
        M.sort(reverse=True)
        if k % 2:
            a = P.pop()
            res = (res * a) % mod
        M_2 = []
        while len(P) >= 2:
            a = P.pop()
            a *= P.pop()
            M_2.append(a)
        while len(M) >= 2:
            a = M.pop()
            a *= M.pop()
            M_2.append(a)
        M_2.sort(reverse=True)
        for i in range(k // 2):
            res = (res * M_2[i]) % mod
    print(res)


if __name__ == '__main__':
    resolve()

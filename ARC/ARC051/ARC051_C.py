# https://atcoder.jp/contests/arc051/submissions/16745726
# C - 掛け算
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, a, b = map(int, input().split())
    A = list(map(int, input().split()))
    MAX = max(A)

    if a == 1:
        A.sort()
        print(*A, sep="\n")
        exit()

    while b != 0:
        A.sort()
        if A[0] > MAX:
            break
        A[0] *= a
        b -= 1

    A.sort()
    q, r = divmod(b, n)
    k = r
    for i in range(n):
        x = 0 if k == 0 else 1
        A[i] = (A[i] * pow(a, q + x, mod)) % mod
        k = max(0, k - 1)
    res = A[r:] + A[:r]
    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()

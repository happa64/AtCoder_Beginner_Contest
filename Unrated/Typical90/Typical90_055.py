# https://atcoder.jp/contests/typical90/submissions/23150247
# 055 - Select 5（★2）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, p, q = map(int, input().split())
    A = tuple(map(lambda x: int(x) % p, input().split()))
    res = 0
    for i in range(n):
        a = A[i]
        for j in range(i + 1, n):
            b = a * A[j] % p
            for k in range(j + 1, n):
                c = b * A[k] % p
                for l in range(k + 1, n):
                    d = c * A[l] % p
                    for m in range(l + 1, n):
                        e = d * A[m] % p
                        if e == q:
                            res += 1
    print(res)


if __name__ == '__main__':
    solve()

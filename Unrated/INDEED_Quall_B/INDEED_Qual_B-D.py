# https://atcoder.jp/contests/indeednow-qualb/submissions/14389425
# D - 高橋くんと数列
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, c = map(int, input().split())
    A = list(map(int, input().split()))

    idx = [[] for _ in range(c + 1)]
    for i in range(n):
        idx[A[i]].append(i)

    for i in range(1, c + 1):
        res = (n + 1) * n // 2
        left = -1
        for j in idx[i]:
            L = j - left - 1
            res -= (L + 1) * L // 2
            left = j
        L = n - 1 - j
        res -= (L + 1) * L // 2
        print(res)


if __name__ == '__main__':
    resolve()

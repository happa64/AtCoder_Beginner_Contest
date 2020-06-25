# https://atcoder.jp/contests/chokudai_S001/submissions/14669098
# K - 辞書順で何番目？
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    class BIT:
        def __init__(self, L):
            self.n = len(L)
            self.bit = [0] * (n + 1)

        def query(self, idx):
            res = 0
            while idx > 0:
                res += self.bit[idx]
                idx -= idx & (-idx)
            return res

        def sec_sum(self, left, right):
            return self.query(right) - self.query(left)

        def update(self, idx, x):
            while idx <= self.n:
                self.bit[idx] += x
                idx += idx & (-idx)

    n = int(input())
    A = list(map(int, input().split()))

    fact = [1, 1]
    for i in range(2, n + 1):
        fact.append((fact[-1] * i) % mod)

    bit = BIT(A)

    res = 0
    for i in range(n):
        res += ((A[i] - 1) - bit.query(A[i] - 1)) * fact[n - (i + 1)]
        res %= mod
        bit.update(A[i], 1)
    print((res + 1) % mod)


if __name__ == '__main__':
    resolve()

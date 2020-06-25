# https://atcoder.jp/contests/chokudai_S001/submissions/14668697
# J - 転倒数
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

    bit = BIT(A)
    res = 0
    for i in range(n):
        res += i - bit.query(A[i])
        bit.update(A[i], 1)

    print(res)


if __name__ == '__main__':
    resolve()

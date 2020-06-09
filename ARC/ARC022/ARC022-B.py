# https://atcoder.jp/contests/arc022/submissions/14128600
# B - 細長いお菓子
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    # しゃくとり法
    res = 0
    Block_idx = {}
    left = 0
    for right in range(n):
        if Block_idx.get(A[right]) is not None and Block_idx.get(A[right]) >= left:
            left = Block_idx[A[right]] + 1
        Block_idx[A[right]] = right
        res = max(res, right - left + 1)

    print(res)


if __name__ == '__main__':
    resolve()

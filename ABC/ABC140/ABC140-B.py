# https://atcoder.jp/contests/abc140/submissions/14115751
# B - Buffet
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    res = 0
    pre = -1
    for i in range(n):
        res += B[A[i] - 1]
        if pre + 1 == A[i]:
            res += C[pre - 1]
        pre = A[i]
    print(res)


if __name__ == '__main__':
    resolve()

# https://atcoder.jp/contests/agc053/submissions/21889881
# A - >< again
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def solve():
    _ = int(input())
    _ = input().rstrip()
    A = tuple(map(int, input().split()))
    k = min(abs(a - b) for a, b in zip(A, A[1:]))
    print(k)
    for i in range(k):
        print(*[a // k + (a % k > i) for a in A])


if __name__ == '__main__':
    solve()

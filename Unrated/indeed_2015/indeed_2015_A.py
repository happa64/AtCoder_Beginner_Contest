# https://atcoder.jp/contests/indeednow-finala-open/submissions/20067858
# A - Table Tennis
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    t = [A[i] + A[-(i + 1)] for i in range(n // 2)]
    print(max(t) - min(t))


if __name__ == '__main__':
    resolve()

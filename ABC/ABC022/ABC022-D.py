# https://atcoder.jp/contests/abc022/submissions/14169531
# D - Big Bang
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = [list(map(int, input().split())) for _ in range(n)]
    B = [list(map(int, input().split())) for _ in range(n)]

    Center_A = [0, 0]
    for x, y in A:
        Center_A[0] += x
        Center_A[1] += y
    Center_A[0] /= n
    Center_A[1] /= n

    long_A = 0
    for x1, y1 in A:
        x2, y2 = Center_A
        dist = pow(pow(x1 - x2, 2) + pow(y1 - y2, 2), 0.5)
        long_A = max(long_A, dist)

    Center_B = [0, 0]
    for x, y in B:
        Center_B[0] += x
        Center_B[1] += y
    Center_B[0] /= n
    Center_B[1] /= n

    long_B = 0
    for x1, y1 in B:
        x2, y2 = Center_B
        dist = pow(pow(x1 - x2, 2) + pow(y1 - y2, 2), 0.5)
        long_B = max(long_B, dist)

    print(long_B / long_A)


if __name__ == '__main__':
    resolve()

# https://atcoder.jp/contests/agc024/submissions/15272453
# C - Sequence Growing Easy
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(int(input()) for _ in range(n))

    if A[0] != 0:
        print(-1)
        exit()
    res = 0
    for i in range(1, n):
        if A[i] != 0:
            if A[i] - A[i - 1] <= 0:
                res += A[i]
            elif A[i] - A[i - 1] == 1:
                res += 1
            else:
                print(-1)
                exit()

    print(res)


if __name__ == '__main__':
    resolve()

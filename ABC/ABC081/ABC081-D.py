# https://atcoder.jp/contests/abc081/submissions/13971980
# D - Non-decreasing
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    max_num = 0
    max_idx = 0
    for i in range(n):
        if abs(A[i]) > abs(max_num):
            max_num = A[i]
            max_idx = i

    res = []
    if max_num >= 0:
        for i in range(n):
            if A[i] < 0:
                A[i] += max_num
                res.append([max_idx + 1, i + 1])

        for i in range(1, n):
            A[i] += A[i - 1]
            res.append([i, i + 1])
    else:
        for i in range(n):
            if A[i] > 0:
                A[i] += max_num
                res.append([max_idx + 1, i + 1])

        for i in reversed(range(n - 1)):
            A[i] += A[i + 1]
            res.append([i + 2, i + 1])

    print(len(res))
    for k in res:
        print(*k)


if __name__ == '__main__':
    resolve()

# https://atcoder.jp/contests/arc093/submissions/13405401
# C - Traveling Plan
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = [0] + list(map(int, input().split())) + [0]

    cost_init = 0
    for i in range(1, n + 2):
        cost_init += abs(A[i - 1] - A[i])

    for i in range(1, n + 1):
        if A[i - 1] <= A[i] <= A[i + 1] or A[i - 1] >= A[i] >= A[i + 1]:
            print(cost_init)
        elif A[i - 1] <= A[i] and A[i] >= A[i + 1] or A[i - 1] >= A[i] and A[i] <= A[i + 1]:
            cost = cost_init - (abs(A[i - 1] - A[i]) + abs(A[i] - A[i + 1])) + abs(A[i - 1] - A[i + 1])
            print(cost)


if __name__ == '__main__':
    resolve()

# https://atcoder.jp/contests/arc039/submissions/14646884
# A - A - B problem
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = input().split()

    res1 = -f_inf
    for i in range(3):
        A = list(a)
        for j in range(10):
            if i == 0 and j == 0:
                continue
            A[i] = str(j)
            diff = int("".join(A)) - int(b)
            res1 = max(res1, diff)

    res2 = -f_inf
    for i in range(3):
        B = list(b)
        for j in range(10):
            if i == 0 and j == 0:
                continue
            B[i] = str(j)
            diff = int(a) - int("".join(B))
            res2 = max(res2, diff)
    print(max(res1, res2))


if __name__ == '__main__':
    resolve()

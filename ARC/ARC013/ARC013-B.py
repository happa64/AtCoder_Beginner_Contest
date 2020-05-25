# https://atcoder.jp/contests/arc013/submissions/13589878
# B - 引越しできるかな？
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    c = int(input())
    Size = [sorted(list(map(int, input().split()))) for _ in range(c)]

    max_N, max_M, max_L = 0, 0, 0
    for n, m, l in Size:
        max_N = max(max_N, n)
        max_M = max(max_M, m)
        max_L = max(max_L, l)

    print(max_N * max_M * max_L)


if __name__ == '__main__':
    resolve()

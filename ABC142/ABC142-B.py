# https://atcoder.jp/contests/abc142/tasks/abc142_b
# B - Roller Coaster
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    H = list(map(int, input().split()))

    res = 0
    for i in range(n):
        if H[i] >= k:
            res += 1
    print(res)


if __name__ == '__main__':
    resolve()

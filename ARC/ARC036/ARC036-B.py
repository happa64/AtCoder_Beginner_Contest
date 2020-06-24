# https://atcoder.jp/contests/arc036/submissions/13470441
# B - 山のデータ
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    H = list(int(input()) for _ in range(n))

    to_east = [1] * n
    for i in range(1, n):
        if H[i - 1] < H[i]:
            to_east[i] = to_east[i - 1] + 1

    to_west = [0] * n
    for j in reversed(range(n - 1)):
        if H[j + 1] < H[j]:
            to_west[j] = to_west[j + 1] + 1

    res = 0
    for e, w in zip(to_east, to_west):
        cnt = e + w
        res = max(res, cnt)

    print(res)


if __name__ == '__main__':
    resolve()

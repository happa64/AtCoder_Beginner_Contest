# https://atcoder.jp/contests/abc190/submissions/19774467
# B - Magic 3
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, s, d = map(int, input().split())
    for i in range(n):
        x, y = map(int, input().split())
        if x >= s or y <= d:
            continue
        print("Yes")
        break
    else:
        print("No")


if __name__ == '__main__':
    resolve()

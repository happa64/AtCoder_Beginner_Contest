# https://atcoder.jp/contests/joi2010yo/submissions/15275957
# B - すごろく
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    grid = list(int(input()) for _ in range(n))
    nums = list(int(input()) for _ in range(m))

    now = 0
    for i in range(m):
        now += nums[i]
        if now >= n - 1:
            print(i + 1)
            break
        now += grid[now]
        if now >= n - 1:
            print(i + 1)
            break


if __name__ == '__main__':
    resolve()

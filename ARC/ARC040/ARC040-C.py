# https://atcoder.jp/contests/arc040/submissions/14934435
# C - Z塗り
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    grid = list(list(input()) for _ in range(n))

    res = 0
    for h in range(n):
        for w in reversed(range(n)):
            if grid[h][w] == ".":
                res += 1
                pos = w
                while 0 <= pos:
                    grid[h][pos] = "o"
                    pos -= 1
                pos = w
                while h + 1 < n and pos < n:
                    grid[h + 1][pos] = "o"
                    pos += 1
                break
    print(res)


if __name__ == '__main__':
    resolve()

# https://atcoder.jp/contests/arc016/submissions/14422600
# B - 音楽ゲーム
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    X = [list(input()) for _ in range(n)]

    res = 0
    for w in range(9):
        h = 0
        while h < n:
            if X[h][w] == "x":
                res += 1
                h += 1
            elif X[h][w] == "o":
                res += 1
                while h < n and X[h][w] == "o":
                    h += 1
            else:
                h += 1
    print(res)


if __name__ == '__main__':
    resolve()

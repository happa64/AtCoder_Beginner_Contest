# https://atcoder.jp/contests/code-formula-2014-quala/submissions/14691590
# B - ボウリングゲーム
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())
    P = input().split()
    Q = input().split()
    init = [
        ["x", " ", "x", " ", "x", " ", "x"],
        [" ", "x", " ", "x", " ", "x", " "],
        [" ", " ", "x", " ", "x", " ", " "],
        [" ", " ", " ", "x", " ", " ", " "]
    ]
    num = [
        ["7", " ", "8", " ", "9", " ", "0"],
        [" ", "4", " ", "5", " ", "6", " "],
        [" ", " ", "2", " ", "3", " ", " "],
        [" ", " ", " ", "1", " ", " ", " "]
    ]

    for p in P:
        for i in range(4):
            for j in range(7):
                if num[i][j] == p:
                    init[i][j] = "."
                    break
            else:
                continue
            break

    for q in Q:
        for i in range(4):
            for j in range(7):
                if num[i][j] == q:
                    init[i][j] = "o"
                    break
            else:
                continue
            break

    for i in init:
        print("".join(i))


if __name__ == '__main__':
    resolve()

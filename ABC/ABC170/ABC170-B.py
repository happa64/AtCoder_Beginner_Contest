# https://atcoder.jp/contests/abc170/submissions/14289623
# B - Crane and Turtle
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x, y = map(int, input().split())
    for i in range(200):
        for j in range(200):
            if i + j == x and i * 2 + j * 4 == y:
                print("Yes")
                exit()
    else:
        print("No")


if __name__ == '__main__':
    resolve()

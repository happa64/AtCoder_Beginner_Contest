# https://codeforces.com/contest/1455/submission/100030962
# C - Ping-pong
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        a, b = 0, 0
        if x == 1:
            if y == 0:
                a = 1
                b = 0
            else:
                a = 0
                b = y
        else:
            if y == 0:
                a = x
                b = 0
            else:
                a = x - 1
                b = y
        print(a, b)


if __name__ == '__main__':
    resolve()

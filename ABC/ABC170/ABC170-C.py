# https://atcoder.jp/contests/abc170/submissions/14296349
# C - Forbidden List
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x, n = map(int, input().split())
    P = set(list(map(int, input().split())))
    res = 0
    mi = f_inf
    for i in range(-200, 200):
        if i not in P:
            if abs(x - i) < mi:
                mi = abs(x - i)
                res = i
    print(res)


if __name__ == '__main__':
    resolve()

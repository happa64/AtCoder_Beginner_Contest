# https://atcoder.jp/contests/arc009/submissions/14462909
# A - 元気にお使い！高橋君
import sys
import math
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    res = 0
    for _ in range(n):
        a, b = map(int, input().split())
        res += a * b
    print(math.floor(res * 1.05))


if __name__ == '__main__':
    resolve()

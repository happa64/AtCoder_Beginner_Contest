# https://atcoder.jp/contests/agc026/submissions/19412213
# B - rng_10s
import sys
from math import gcd

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    t = int(input())
    for _ in range(t):
        a, b, c, d = map(int, input().split())
        if a < b:
            print("No")
        elif b > d:
            print("No")
        elif c >= b:
            print("Yes")
        else:
            g = gcd(b, d)
            l = a - b + 1
            r = a - c - 1
            cnt_r = r // g
            cnt_l = (l - 1) // g
            cnt = cnt_r - cnt_l
            if cnt:
                print("No")
            else:
                print("Yes")


if __name__ == '__main__':
    resolve()

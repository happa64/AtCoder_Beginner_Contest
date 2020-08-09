# https://atcoder.jp/contests/chokudai_S002/submissions/15790620
# G - GCD α
import sys
from math import gcd
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    for _ in range(n):
        a, b = map(int, input().split())
        print(gcd(a, b))


if __name__ == '__main__':
    resolve()

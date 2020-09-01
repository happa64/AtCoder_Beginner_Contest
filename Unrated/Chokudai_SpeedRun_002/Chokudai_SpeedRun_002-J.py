# https://atcoder.jp/contests/chokudai_S002/submissions/16443667
# J - GCD β
import sys
from math import gcd

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    AB = [list(map(int, input().split())) for _ in range(n)]
    res1, res2 = AB[0]
    for i in range(1, n):
        a, b = AB[i]
        res1 = max(gcd(res1, a), gcd(res1, b))
        res2 = max(gcd(res2, a), gcd(res2, b))
    print(max(res1, res2))


if __name__ == '__main__':
    resolve()

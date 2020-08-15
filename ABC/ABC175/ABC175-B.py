# https://atcoder.jp/contests/abc175/submissions/15912739
# B - Making Triangle
import sys
from itertools import combinations

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    L = list(map(int, input().split()))

    res = 0
    for a, b, c in combinations(L, 3):
        if a == b or b == c or c == a:
            continue
        if a + b > c and b + c > a and c + a > b:
            res += 1
    print(res)


if __name__ == '__main__':
    resolve()

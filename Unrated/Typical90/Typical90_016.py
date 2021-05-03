# https://atcoder.jp/contests/typical90/submissions/21932399
# 016 - Minimum Coins（★3）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    A, B, C = map(int, input().split())
    MAX = 10000

    res = f_inf
    for i in range(MAX):
        a = i * A
        for j in range(MAX - i):
            b = j * B
            c = n - a - b
            if c >= 0 and c % C == 0:
                res = min(res, i + j + c // C)
    print(res)


if __name__ == '__main__':
    solve()

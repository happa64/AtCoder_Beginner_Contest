# https://atcoder.jp/contests/abc209/submissions/24113622
# C - Not Equal
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    C = list(map(int, input().split()))
    C.sort()

    res = 1
    for i in range(n):
        cnt = C[i] - i
        res *= cnt
        res %= MOD
    print(res)

if __name__ == '__main__':
    solve()

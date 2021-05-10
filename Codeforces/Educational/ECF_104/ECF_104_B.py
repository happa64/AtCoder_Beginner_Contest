# https://codeforces.com/contest/1487/submission/109073559
# B - Cat Cycle
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, k = map(int, input().split())
    k -= 1
    res = (k + (n % 2) * (k // (n // 2))) % n + 1
    print(res)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()

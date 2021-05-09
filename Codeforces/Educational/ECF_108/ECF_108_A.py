# https://codeforces.com/contest/1519/submission/115765560
# A - Red and Blue Beans
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    r, b, d = map(int, input().split())
    if r > b:
        r, b = b, r
    print("YES" if b <= (1 + d) * r else "NO")


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()

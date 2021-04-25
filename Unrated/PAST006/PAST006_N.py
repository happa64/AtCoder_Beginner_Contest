# https://atcoder.jp/contests/past202104-open/submissions/22052544
# N - 活動
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, h = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(n)]
    AB.sort(key=lambda x: -x[0] / x[1])

    dp = [0] * (h + 1)
    for a, b in AB:
        for i in range(h + 1):
            dp[max(0, i - b)] = max(dp[max(0, i - b)], dp[i] + a * i)
    print(max(dp))


if __name__ == '__main__':
    solve()

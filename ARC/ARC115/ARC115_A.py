# https://atcoder.jp/contests/arc115/submissions/21219720
# A - Two Choices
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, m = map(int, input().split())
    S = tuple(input().rstrip() for _ in range(n))

    even = odd = 0
    for s in S:
        cnt = s.count("1")
        if cnt % 2:
            odd += 1
        else:
            even += 1
    res = even * odd
    print(res)


if __name__ == '__main__':
    solve()

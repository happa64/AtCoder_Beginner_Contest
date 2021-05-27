# https://atcoder.jp/contests/typical90/submissions/22911256
# 048 - I will not drop out（★3）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, k = map(int, input().split())
    AB = tuple(tuple(map(int, input().split())) for _ in range(n))
    C = []
    for a, b in AB:
        C.extend((b, a - b))
    C.sort(reverse=True)
    res = sum(C[:k])
    print(res)


if __name__ == '__main__':
    solve()

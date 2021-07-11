# https://atcoder.jp/contests/typical90/submissions/24168243
# 086 - Snuke's Favorite Arrays（★5）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
MOD = 10 ** 9 + 7


def solve():
    n, q = map(int, input().split())
    query = tuple(tuple(map(int, input().split())) for _ in range(q))
    res = 1
    for i in range(60):
        cnt = 0
        for bit in range(1 << n):
            for x, y, z, w in query:
                flg = 0
                for mask in [x - 1, y - 1, z - 1]:
                    flg |= 1 if bit & (1 << mask) else 0
                if flg != (1 if w & (1 << i) else 0):
                    break
            else:
                cnt += 1
        res = (res * cnt) % MOD
    print(res)


if __name__ == '__main__':
    solve()

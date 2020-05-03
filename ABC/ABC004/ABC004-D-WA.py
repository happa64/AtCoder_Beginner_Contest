# https://atcoder.jp/contests/abc004/tasks/abc004_4
# D - マーブル（40点解法）
import sys

sys.setrecursionlimit(10 ** 7)


def solve(n):
    i = 0
    cost = 0
    res = 0
    while n != i + 1:
        if i % 2 == 0:
            cost += 1
        res += cost
        i += 1
    return res


def resolve():
    R, G, B = map(int, input().split())
    print(solve(R) + solve(G) + solve(B))


if __name__ == '__main__':
    resolve()

# https://atcoder.jp/contests/abc103/submissions/14915037
# D - Islands War
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    AB = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: x[1])

    res = 0
    remove = -1
    for a, b in AB:
        if remove <= a:
            res += 1
            remove = b
    print(res)


if __name__ == '__main__':
    resolve()

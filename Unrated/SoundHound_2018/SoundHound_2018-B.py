# https://atcoder.jp/contests/soundhound2018/submissions/15490405
# B - 音量
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, L, R = map(int, input().split())
    A = list(map(int, input().split()))

    res = []
    for a in A:
        if a < L:
            res.append(L)
        elif R < a:
            res.append(R)
        else:
            res.append(a)
    print(*res)


if __name__ == '__main__':
    resolve()

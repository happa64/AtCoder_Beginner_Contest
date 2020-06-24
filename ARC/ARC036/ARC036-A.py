# https://atcoder.jp/contests/arc036/submissions/14646747
# A - ぐっすり
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    T = list(int(input()) for _ in range(n))

    tot = 0
    for i in range(n):
        if i <= 2:
            tot += T[i]
        else:
            if tot < k:
                print(i)
                break
            else:
                tot -= T[i - 3]
                tot += T[i]
    else:
        print(-1)


if __name__ == '__main__':
    resolve()

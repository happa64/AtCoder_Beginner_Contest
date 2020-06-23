# https://atcoder.jp/contests/sumitrust2019/submissions/13004623
# E - Colorful Hats 2
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    res = 1
    cnt = [3 if i == 0 else 0 for i in range(n + 1)]

    for a in A:
        res = res * cnt[a] % mod
        cnt[a] -= 1
        cnt[a + 1] += 1

    print(res)


if __name__ == '__main__':
    resolve()

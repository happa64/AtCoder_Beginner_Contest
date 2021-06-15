# https://atcoder.jp/contests/typical90/submissions/23493919
# 066 - Various Arrays（★5）
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def solve():
    n = int(input())
    LR = tuple(tuple(map(int, input().split())) for _ in range(n))

    res = 0
    for i in range(n):
        li, ri = LR[i]
        for j in range(i + 1, n):
            lj, rj = LR[j]
            tot = 0
            cnt = 0
            for a in range(li, ri + 1):
                for b in range(lj, rj + 1):
                    tot += 1
                    if a > b:
                        cnt += 1
            res += cnt / tot
    print(res)


if __name__ == '__main__':
    solve()

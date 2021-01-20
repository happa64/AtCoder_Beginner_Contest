# https://atcoder.jp/contests/pakencamp-2020-day1/submissions/19532432
# G - 同意書
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    query = [list(map(int, input().split())) for _ in range(m)]

    res = -1
    for bit in range(1 << n):
        for l, r, x in query:
            cnt = 0
            for mask in range(l - 1, r):
                if bit & (1 << mask):
                    cnt += 1
            if cnt != x:
                break
        else:
            res = max(res, bin(bit).count("1"))
    print(res)


if __name__ == '__main__':
    resolve()

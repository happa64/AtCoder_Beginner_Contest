# https://atcoder.jp/contests/abc015/submissions/13970299
# B - 高橋くんの集計
import sys
import math

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    total = 0
    cnt = 0
    for a in A:
        if a != 0:
            cnt += 1
            total += a
    res = math.ceil(total / cnt)
    print(res)


if __name__ == '__main__':
    resolve()

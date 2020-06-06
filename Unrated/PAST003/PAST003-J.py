# https://atcoder.jp/contests/past202005/submissions/14066094
# J - 回転寿司
import sys
import bisect

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))

    L = [0] * n
    for a in A:
        idx = bisect.bisect_left(L, a)
        if idx == 0:
            print(-1)
        else:
            L[idx - 1] = a
            res = n - idx + 1
            print(res)


if __name__ == '__main__':
    resolve()

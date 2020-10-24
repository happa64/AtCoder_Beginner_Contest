# https://atcoder.jp/contests/discovery2016-qual/submissions/17597044
# B - ディスコ社内ツアー
import sys
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    MAX = max(A)
    num_index = [[] for _ in range(MAX)]
    for idx, a in enumerate(A):
        num_index[a - 1].append(idx)

    res = 1
    prev = -1
    for i in range(MAX):
        if not num_index[i]:
            continue
        j = bisect_left(num_index[i], prev)
        if j != 0:
            res += 1
            prev = num_index[i][j - 1]
        else:
            prev = num_index[i][-1]

    if prev == 0:
        res -= 1

    print(res)


if __name__ == '__main__':
    resolve()

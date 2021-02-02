# https://atcoder.jp/contests/arc014/submissions/19879106
# D - grepマスター
import sys
from itertools import accumulate
from bisect import bisect_right

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, n, m = map(int, input().split())
    L = [int(input()) for _ in range(n)]
    query = [list(map(int, input().split())) for _ in range(m)]

    diff = [L[i] - L[i - 1] - 1 for i in range(1, n)]
    diff.sort()
    diff_acc = [0] + list(accumulate(diff))
    diff_head = L[0] - 1
    diff_foot = a - L[-1]
    for x, y in query:
        idx = bisect_right(diff, x + y)
        res = diff_acc[idx] + (n - idx - 1) * (x + y) + n
        res += min(x, diff_head) + min(y, diff_foot)
        print(res)


if __name__ == '__main__':
    resolve()

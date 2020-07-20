# https://atcoder.jp/contests/dwacon5th-prelims/submissions/15333042
# B - Sum AND Subarrays
import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    R = [0] + list(accumulate(A))
    subs = []
    for left in range(n):
        for right in range(left + 1, n + 1):
            subs.append(R[right] - R[left])

    res = 0
    for mask in reversed(range(40)):
        if len(subs) == 0:
            break
        tmp = []
        for i in range(len(subs)):
            if subs[i] & (1 << mask):
                tmp.append(subs[i])
        if len(tmp) >= k:
            res += 1 << mask
            subs = tmp
    print(res)


if __name__ == '__main__':
    resolve()

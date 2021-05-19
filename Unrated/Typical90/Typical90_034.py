# https://atcoder.jp/contests/typical90/submissions/22379469
# 034 - There are few types of elements（★4）
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    res = 0
    left = 0
    right = 0
    num_cnt = defaultdict(int)
    while right < n:
        while right < n and len(num_cnt) <= k:
            if len(num_cnt) == k and num_cnt.get(A[right]) is None:
                break
            num_cnt[A[right]] += 1
            right += 1
        res = max(res, right - left)
        while left < right and len(num_cnt) >= k:
            num_cnt[A[left]] -= 1
            if num_cnt[A[left]] == 0:
                num_cnt.pop(A[left])
            left += 1
    print(res)


if __name__ == '__main__':
    solve()

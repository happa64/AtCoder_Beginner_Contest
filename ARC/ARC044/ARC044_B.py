# https://atcoder.jp/contests/arc044/submissions/16654461
# B - 最短路問題
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    if A[0] != 0 or A.count(0) > 1:
        print(0)
        exit()

    MAX = max(A)
    dist_cnt = [0] * (MAX + 1)
    for a in A:
        dist_cnt[a] += 1

    if 0 in dist_cnt:
        print(0)
        exit()

    res = 1
    for i in range(1, MAX + 1):
        prev = dist_cnt[i - 1]
        now = dist_cnt[i]
        res *= (pow(2, (now - 1) * now // 2, mod) * pow((pow(2, prev, mod) - 1), now, mod)) % mod
        res %= mod
    print(res)


if __name__ == '__main__':
    resolve()

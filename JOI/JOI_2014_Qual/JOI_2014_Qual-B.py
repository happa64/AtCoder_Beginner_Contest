# https://atcoder.jp/contests/joi2014yo/submissions/15124291
# B - 投票 (Vote)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    A = list(int(input()) for _ in range(n))

    res = [0] * n
    for _ in range(m):
        b = int(input())
        for i in range(n):
            if A[i] <= b:
                res[i] += 1
                break
    print(res.index(max(res)) + 1)


if __name__ == '__main__':
    resolve()

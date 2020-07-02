# https://atcoder.jp/contests/code-festival-2014-qualb/submissions/14894613
# B - 歩く人
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    total = 0
    for i in range(n):
        a = int(input())
        total += a
        if total >= k:
            print(i + 1)
            break


if __name__ == '__main__':
    resolve()

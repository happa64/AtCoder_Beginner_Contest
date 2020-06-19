# https://atcoder.jp/contests/arc010/submissions/14462968
# A - 名刺交換
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m, a, b = map(int, input().split())
    for i in range(m):
        c = int(input())
        if n <= a:
            n += b
        if n < c:
            print(i + 1)
            break
        n -= c
    else:
        print("complete")


if __name__ == '__main__':
    resolve()

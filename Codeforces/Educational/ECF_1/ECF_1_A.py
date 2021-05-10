# https://codeforces.com/contest/598/submission/99604984
# A - Tricky Sum
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        res = (1 + n) * n // 2
        k = 1
        while n >= k:
            res -= k * 2
            k *= 2
        print(res)


if __name__ == '__main__':
    resolve()

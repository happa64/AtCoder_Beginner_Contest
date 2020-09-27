# https://atcoder.jp/contests/joisc2010/submissions/17064121
# poster - JOIポスター (JOI Poster)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    if pow(2, n) == k:
        print("I" * (k - 1) + "J")
        exit()
    res = ""
    while n and k > pow(2, n - 1):
        res += "I" * pow(2, n - 1)
        k -= pow(2, n - 1)
        n -= 1
    res += "J" * pow(2, n - 1) + "O" * pow(2, n - 1)
    print(res)


if __name__ == '__main__':
    resolve()

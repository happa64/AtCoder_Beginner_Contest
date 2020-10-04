# https://atcoder.jp/contests/abc165/submissions/17188761
# E - Rotation Matching
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())

    if n % 2:
        left = 1
        right = n - 1
        while left < right and m:
            print(left, right)
            left += 1
            right -= 1
            m -= 1
    else:
        left = 1
        right = n - 1
        flg = False
        while left < right and m:
            if not flg and right - left <= n // 2:
                right -= 1
                flg = True
            print(left, right)
            left += 1
            right -= 1
            m -= 1


if __name__ == '__main__':
    resolve()

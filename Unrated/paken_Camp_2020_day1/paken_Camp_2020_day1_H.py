# https://atcoder.jp/contests/pakencamp-2020-day1/submissions/19533632
# H - その計算、合ってますか？
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())

        n = max(a, b, c).bit_length() + 1
        even = odd = False
        for mask in range(n):
            if (b & (1 << mask)) and not (a & (1 << mask)):
                print("No")
                break
            if (c & (1 << mask)) and not (a & (1 << mask)):
                print("No")
                break
            if (b & (1 << mask)) and not (c & (1 << mask)):
                even = True
            if (b & (1 << mask)) and (c & (1 << mask)):
                odd = True
            if even and odd:
                print("No")
                break
        else:
            print("Yes")


if __name__ == '__main__':
    resolve()

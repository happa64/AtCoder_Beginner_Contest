# https://atcoder.jp/contests/abl/submissions/17027270
# B - Integer Preference
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c, d = map(int, input().split())
    if a <= c <= b <= d or a <= c <= d <= b or c <= a <= d <= b or a <= c <= b <= d or c <= a <= b <= d or c <= a <= d <= b:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    resolve()

# https://atcoder.jp/contests/abc037/submissions/14167832
# A - 饅頭
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c = map(int, input().split())
    res = c // min(a, b)
    print(res)


if __name__ == '__main__':
    resolve()

# https://atcoder.jp/contests/gigacode-2019/submissions/15226149
# A - 教室
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())
    res = a * b * b
    print(res)


if __name__ == '__main__':
    resolve()

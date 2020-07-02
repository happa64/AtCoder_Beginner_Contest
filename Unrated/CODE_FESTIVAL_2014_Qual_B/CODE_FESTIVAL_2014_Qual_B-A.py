# https://atcoder.jp/contests/code-festival-2014-qualb/submissions/14894601
# A - あるピアニスト
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())
    print(max(a, b))


if __name__ == '__main__':
    resolve()

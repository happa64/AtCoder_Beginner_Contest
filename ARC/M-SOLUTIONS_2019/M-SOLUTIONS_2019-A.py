# https://atcoder.jp/contests/m-solutions2019/submissions/13700397
# A - Sum of Interior Angles
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    print(180 * (n - 2))


if __name__ == '__main__':
    resolve()

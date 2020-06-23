# https://atcoder.jp/contests/arc027/submissions/14638274
# A - 門限
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    h, m = map(int, input().split())
    goal = 18 * 60
    now = h * 60 + m
    res = goal - now
    print(res)


if __name__ == '__main__':
    resolve()

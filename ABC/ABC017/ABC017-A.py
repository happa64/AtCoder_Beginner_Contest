# https://atcoder.jp/contests/abc017/submissions/14079907
# A - プロコン
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    res = 0
    for i in range(3):
        s, e = map(int, input().split())
        res += s * e // 10
    print(res)


if __name__ == '__main__':
    resolve()

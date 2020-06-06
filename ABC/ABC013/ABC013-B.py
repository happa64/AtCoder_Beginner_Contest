# https://atcoder.jp/contests/abc013/submissions/13970240
# B - 錠
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a = int(input())
    b = int(input())
    res1 = abs(a - b)
    if a < b:
        res2 = a + 9 - b + 1
    else:
        res2 = b + 9 - a + 1

    print(min(res1, res2))


if __name__ == '__main__':
    resolve()

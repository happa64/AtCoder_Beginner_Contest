# https://atcoder.jp/contests/arc052/submissions/14378795
# A - 何期生？
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input()
    res = ""
    num = [str(i) for i in range(10)]
    for s in S:
        if s in num:
            res += s
    print(res)


if __name__ == '__main__':
    resolve()

# https://atcoder.jp/contests/abc038/submissions/14167866
# A - お茶
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    print("YES" if s[-1] == "T" else "NO")


if __name__ == '__main__':
    resolve()

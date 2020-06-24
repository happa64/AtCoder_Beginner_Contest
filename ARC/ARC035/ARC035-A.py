# https://atcoder.jp/contests/arc035/submissions/14646696
# A - 高橋くんと回文
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    n = len(s)

    for i in range(n // 2):
        if s[i] == s[-(i + 1)] or (s[i] == "*" or s[-(i + 1)] == "*"):
            continue
        else:
            print("NO")
            break
    else:
        print("YES")


if __name__ == '__main__':
    resolve()

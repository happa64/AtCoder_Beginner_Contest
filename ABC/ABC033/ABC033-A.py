# https://atcoder.jp/contests/abc033/submissions/14152009
# A - 暗証番号
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = input()
    for i in range(1, 4):
        if n[i - 1] != n[i]:
            print("DIFFERENT")
            break
    else:
        print("SAME")


if __name__ == '__main__':
    resolve()

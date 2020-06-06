# https://atcoder.jp/contests/abc039/submissions/14045268
# B - エージェント高橋君
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x = int(input())

    for i in range(1, 300):
        if pow(i, 4) == x:
            print(i)
            break


if __name__ == '__main__':
    resolve()

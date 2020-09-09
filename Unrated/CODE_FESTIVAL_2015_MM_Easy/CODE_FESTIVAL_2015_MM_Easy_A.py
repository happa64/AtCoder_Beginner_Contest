# https://atcoder.jp/contests/code-festival-2015-morning-easy/submissions/16598158
# A - ヘイホー君と加算
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    k = n
    while pow(k, 0.5) != int(pow(k, 0.5)):
        k += 1
    print(k - n)


if __name__ == '__main__':
    resolve()

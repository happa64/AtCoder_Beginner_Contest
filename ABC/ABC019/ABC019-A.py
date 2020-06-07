# https://atcoder.jp/contests/abc019/submissions/14080048
# A - 高橋くんと年齢
import sys
from statistics import median

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    A = list(map(int, input().split()))
    print(median(A))


if __name__ == '__main__':
    resolve()

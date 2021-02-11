# https://atcoder.jp/contests/maximum-cup-2018/submissions/20070016
# A - フィギュアスケート界の貴公子埼大選手
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    query = [list(map(int, input().split())) for _ in range(n)]
    res = sum(m for t, d, m in query if t + 10 <= d)
    print(res)


if __name__ == '__main__':
    resolve()

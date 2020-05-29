# https://atcoder.jp/contests/yahoo-procon2019-qual/submissions/13677614
# A - Anti-Adjacency
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())

    res = [i for i in range(1, n + 1, 2)]
    print("YES" if len(res) >= k else "NO")


if __name__ == '__main__':
    resolve()

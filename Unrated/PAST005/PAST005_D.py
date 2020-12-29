# https://atcoder.jp/contests/past202012-open/submissions/19042597
# D - リーディングゼロ
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = list(input().rstrip() for _ in range(n))
    T = [[int(s), len(s), s] for s in S]
    T.sort(key=lambda x: [x[0], -x[1]])
    res = [t for _, _,  t in T]
    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()

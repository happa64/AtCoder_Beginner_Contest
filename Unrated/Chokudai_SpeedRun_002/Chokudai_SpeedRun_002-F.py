# https://atcoder.jp/contests/chokudai_S002/submissions/15790555
# F - 種類数 α
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    res = 0
    used = set()
    for _ in range(n):
        a, b = map(int, input().split())
        if (a, b) not in used:
            res += 1
            used.add((a, b))
            used.add((b, a))
    print(res)


if __name__ == '__main__':
    resolve()

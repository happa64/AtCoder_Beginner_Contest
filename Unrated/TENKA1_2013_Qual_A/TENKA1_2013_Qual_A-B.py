# https://atcoder.jp/contests/tenka1-2013-quala/submissions/14670313
# B - 天下一難易度設定
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    res = 0
    for _ in range(n):
        p = list(map(int, input().split()))
        s = sum(p)
        if 0 <= s < 20:
            res += 1
    print(res)


if __name__ == '__main__':
    resolve()

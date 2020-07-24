# https://atcoder.jp/contests/code-festival-2018-qualb/submissions/15396002
# B - Tensai
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, x = map(int, input().split())
    AB = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: -x[1])
    AB[0][0] += x
    res = sum([a * b for a, b in AB])
    print(res)


if __name__ == '__main__':
    resolve()

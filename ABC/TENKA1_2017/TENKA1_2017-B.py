# https://atcoder.jp/contests/tenka1-2017-beginner/submissions/13608583
# B - Different Distribution
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    AB = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
    res = AB[-1][0] + AB[-1][1]
    print(res)


if __name__ == '__main__':
    resolve()

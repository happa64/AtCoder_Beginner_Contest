# https://atcoder.jp/contests/abc093/submissions/13954070
# C - Same Integers
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    ABC = sorted(list(map(int, input().split())))

    res = 0
    ABC[0] += ABC[2] - ABC[1]
    res += ABC[2] - ABC[1]
    res += (ABC[2] - ABC[0]) // 2 if (ABC[2] - ABC[0]) % 2 == 0 else (ABC[2] - ABC[0]) // 2 + 2
    print(res)


if __name__ == '__main__':
    resolve()

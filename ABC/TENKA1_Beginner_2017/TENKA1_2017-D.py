# https://atcoder.jp/contests/tenka1-2017-beginner/submissions/19394384
# D - IntegerotS
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(n)]

    MAX = k.bit_length() + 1
    res = sum(b for a, b in AB if a | k == k)
    check = 0
    for i in reversed(range(MAX)):
        if k & (1 << i):
            check |= 1 << i
            t = sum(b for a, b in AB if (a | (check - 1)) == check - 1)
            res = max(res, t)
    print(res)


if __name__ == '__main__':
    resolve()

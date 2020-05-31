# https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_a
# A - Sum of Two Integers
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    res = 0
    for i in range(1, (n + 1) // 2):
        if i != n - i:
            res += 1

    print(res)


if __name__ == '__main__':
    resolve()

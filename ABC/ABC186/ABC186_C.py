# https://atcoder.jp/contests/abc186/submissions/18867727
# C - Unlucky 7
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    res = 0
    for i in range(1, n + 1):
        if not ("7" in str(i)) and not ("7" in oct(i)):
            res += 1
    print(res)


if __name__ == '__main__':
    resolve()

# https://atcoder.jp/contests/abc019/submissions/14081584
# D - 高橋くんと木の直径
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    target = 0
    ma = 0
    for i in range(1, n + 1):
        print("? {} {}".format(1, i))
        dist = int(input())
        if ma < dist:
            ma = dist
            target = i

    res = 0
    for i in range(1, n + 1):
        print("? {} {}".format(target, i))
        dist = int(input())
        res = max(res, dist)

    print("! {}".format(res))
    exit()


if __name__ == '__main__':
    resolve()

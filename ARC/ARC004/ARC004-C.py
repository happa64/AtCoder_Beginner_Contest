# https://atcoder.jp/contests/arc004/submissions/18502947
# C - 平均値太郎の憂鬱 ( The melancholy of Taro Heikinchi )
import sys
from math import gcd

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x, y = map(int, input().split("/"))
    g = gcd(x, y)
    x //= g
    y //= g
    ma = 2 * x // y + 10
    mi = 2 * x / y - 10

    res = []
    for n in reversed(range(1, ma)):
        if mi > n - 2 / n:
            break
        if (n * (n * y + y - 2 * x)) % (2 * y) == 0:
            m = (n * (n * y + y - 2 * x)) // (2 * y)
            if 1 <= m <= n:
                res.append([n, m])

    if len(res) == 0:
        print("Impossible")
    else:
        res.sort()
        for i in res:
            print(*i)


if __name__ == '__main__':
    resolve()

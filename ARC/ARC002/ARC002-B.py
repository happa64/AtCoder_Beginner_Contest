# https://atcoder.jp/contests/arc002/submissions/14423288
# B - 割り切れる日付
import sys
from datetime import datetime, timedelta

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    y, m, d = map(int, input().split("/"))
    init = datetime(y, m, d)
    for i in range(100000):
        now = init + timedelta(i)
        y = now.year
        m = now.month
        d = now.day
        if y % (m * d) == 0:
            y = str(y)
            m = str(m).zfill(2)
            d = str(d).zfill(2)
            print("/".join([y, m, d]))
            break


if __name__ == '__main__':
    resolve()

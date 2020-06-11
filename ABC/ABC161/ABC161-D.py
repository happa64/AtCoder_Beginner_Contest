# https://atcoder.jp/contests/abc161/submissions/12823160
# D - Lunlun Number
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    k = int(input())
    res = []

    def dfs(x):
        res.append(x)
        if len(str(x)) == 10:
            return

        for i in range(10):
            if abs(x % 10 - i) <= 1:
                dfs(x * 10 + i)

        return

    for i in range(1, 10):
        dfs(i)
    res.sort()
    print(res[k - 1])


if __name__ == '__main__':
    resolve()

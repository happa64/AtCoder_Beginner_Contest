# https://atcoder.jp/contests/dwango2016-prelims/submissions/13468657
# B - 積み鉛筆
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    K = list(map(int, input().split()))

    res = [K[0]]
    for i in range(n - 2):
        res.append(min(K[i], K[i + 1]))
    res.append(K[-1])

    print(*res)


if __name__ == '__main__':
    resolve()

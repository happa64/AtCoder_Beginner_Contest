# https://atcoder.jp/contests/arc040/submissions/13429608
# B - 直線塗り
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    """
    解法概要：

    :return:
    """
    n, r = list(map(int, input().split()))
    s = input()

    res = 0
    last = s.rfind(".")
    res += max(0, last - r + 1)

    s = list(s)

    for i in reversed(range(n)):
        if s[i] == ".":
            res += 1
            for j in reversed(range(max(0, i + 1 - r), i + 1)):
                s[j] = "o"

    print(res)


if __name__ == '__main__':
    resolve()

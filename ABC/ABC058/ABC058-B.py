# https://atcoder.jp/contests/abc058/tasks/abc058_b
# B - ∵∴∵
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    o = list(input())
    e = list(input())

    res = [""] * (len(o) + len(e))
    for i in range(len(o) + len(e)):
        if i % 2 != 0:
            s = e.pop(0)
            res[i] = s
        else:
            s = o.pop(0)
            res[i] = s

    print("".join(res))


if __name__ == '__main__':
    resolve()

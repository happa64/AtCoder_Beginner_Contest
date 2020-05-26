# https://atcoder.jp/contests/abc062/tasks/abc062_b
# B - Picture Frame
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())

    res = [["#"] * (W + 2)]

    for _ in range(H):
        a = list(input())
        res.append(["#"] + a + ["#"])

    res.append(["#"] * (W + 2))

    for i in res:
        print("".join(i))


if __name__ == '__main__':
    resolve()

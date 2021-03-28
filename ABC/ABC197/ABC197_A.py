# https://atcoder.jp/contests/abc197/submissions/21290796
# A - Rotate
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    S = list(input())
    a = S.pop(0)
    S.append(a)
    res = "".join(S)
    print(res)


if __name__ == '__main__':
    solve()

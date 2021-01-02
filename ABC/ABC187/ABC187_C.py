# https://atcoder.jp/contests/abc187/submissions/19127084
# C - 1-SAT
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S, S_ = [], set()
    for _ in range(n):
        s = input()
        if s[0] == "!":
            S_.add(s)
        else:
            S.append(s)

    for s in S:
        if "!" + s in S_:
            print(s)
            break
    else:
        print("satisfiable")


if __name__ == '__main__':
    resolve()

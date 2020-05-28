# https://atcoder.jp/contests/diverta2019/tasks/diverta2019_c
# C - AB Substrings
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = list(input() for _ in range(n))

    cnt_AB = 0
    cnt_A = 0
    cnt_B = 0
    res = 0
    for s in S:
        res += s.count("AB")
        if s[0] == "B" and s[-1] == "A":
            cnt_AB += 1
        elif s[0] == "B":
            cnt_B += 1
        elif s[-1] == "A":
            cnt_A += 1

    if cnt_A + cnt_B > 0:
        print(res + cnt_AB + min(cnt_A, cnt_B))
    else:
        print(res + max(0, cnt_AB - 1))


if __name__ == '__main__':
    resolve()

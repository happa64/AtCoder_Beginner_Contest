# https://atcoder.jp/contests/colopl2018-final-open/submissions/16819942
# A - ファイティング・タカハシ
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = input()

    if len(set(S)) == 1 and S[0] == "A":
        res = ((len(S) * n) + 1) * len(S) * n // 2
        print(res)
        exit()

    comb = 0
    res = 0
    for i in range(len(S)):
        if S[i] == "A":
            comb += 1
            res += comb
        else:
            comb = 0

    if n > 1:
        loop_score = 0
        for i in range(len(S)):
            if S[i] == "A":
                comb += 1
                res += comb
                loop_score += comb
            else:
                comb = 0
        res += (n - 2) * loop_score

    print(res)


if __name__ == '__main__':
    resolve()

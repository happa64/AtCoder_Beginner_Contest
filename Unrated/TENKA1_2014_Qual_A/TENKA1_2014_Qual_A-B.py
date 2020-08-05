# https://atcoder.jp/contests/tenka1-2014-quala/submissions/15704411
# B - かぶりん！
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input()
    n = len(S)
    MAX = n + 10

    kaburin = 5
    res = 0
    wait = 0
    Return = [0] * MAX
    Combo = [0] * MAX
    for i in range(n):
        kaburin += Return[i]
        Combo[i + 1] += Combo[i]
        if wait:
            wait -= 1
            continue
        if S[i] == "N" and kaburin >= 1:
            res += 10 + Combo[i] // 10
            Combo[i + 2] += 1
            Return[i + 7] += 1
            kaburin -= 1
        elif S[i] == "C" and kaburin >= 3:
            res += 50 + 5 * (Combo[i] // 10)
            Combo[i + 4] += 1
            Return[i + 9] += 3
            kaburin -= 3
            wait = 2
    print(res)


if __name__ == '__main__':
    resolve()

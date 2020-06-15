# https://atcoder.jp/contests/tenka1-2015-qualb/submissions/14386067
# B - 天下一リテラル
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input()
    n = len(S)

    if S == "{}":
        print("dict")
        exit()

    left = 0
    right = 0
    for i in range(n):
        if S[i] == "{":
            left += 1
        elif S[i] == "}":
            right += 1

        if left - right == 1:
            if S[i] == ":":
                print("dict")
                break
    else:
        print("set")


if __name__ == '__main__':
    resolve()

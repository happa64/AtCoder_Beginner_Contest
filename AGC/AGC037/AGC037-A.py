# https://atcoder.jp/contests/agc037/tasks/agc037_a
# A - Dividing a String（嘘解法）
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    n = len(s)

    # これだと例えばaaaaaを正しく分割できない
    subss = [""]
    subs = ""
    res = 0
    for i in range(n):
        subs += s[i]
        if subss[-1] != subs:
            subss.append(subs)
            res += 1
            subs = ""

    print(res)


if __name__ == '__main__':
    resolve()

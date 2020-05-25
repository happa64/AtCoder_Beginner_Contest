# https://atcoder.jp/contests/code-formula-2014-final/submissions/13587569
# C - 次世代SNS
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = list(input().split())

    res = set()
    for s in S:
        for i in range(len(s)):
            if s[i] == "@":
                subs = ""
                for j in range(i + 1, len(s)):
                    if s[j] == "@":
                        res.add(subs)
                        break
                    subs += s[j]
                else:
                    res.add(subs)

    res = sorted(list(res))
    for i in res:
        if i != "":
            print(i)


if __name__ == '__main__':
    resolve()

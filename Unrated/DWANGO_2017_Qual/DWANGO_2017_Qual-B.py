# https://atcoder.jp/contests/dwacon2017-prelims/submissions/17889743
# B - ニコニコレベル
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    T = input()

    res = []
    num = ["2", "5"]
    S = [num[i % 2] for i in range(len(T))]
    ss = ""
    for s, t in zip(S, T):
        if s == t or t == "?":
            ss += s
        else:
            if ss != "":
                res.append(ss)
            ss = ""
    if ss != "":
        res.append(ss)

    S = [num[i % 2 - 1] for i in range(len(T))]
    ss = ""
    for s, t in zip(S, T):
        if s == t or t == "?":
            ss += s
        else:
            if ss != "":
                res.append(ss)
            ss = ""
    if ss != "":
        res.append(ss)

    ans = 0
    for ss in res:
        t = len(ss)
        if ss[0] == "5":
            t -= 1
        if ss[-1] == "2":
            t -= 1
        ans = max(ans, t)
    print(ans)


if __name__ == '__main__':
    resolve()

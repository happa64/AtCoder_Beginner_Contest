# https://atcoder.jp/contests/abc076/submissions/13480535
# C - Dubious Document 2
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    """
    解法概要：
        sの先頭から順にtがマッチングする場所を探索し、当てはまる場合は、当てはまる場所以外の？をaで埋めて解の候補に入れる。
        解の候補を昇順ソートし、一番先頭のものが解となる。

    計算量：O(ST)
    """
    s = input()
    t = input()
    n = len(s)

    res = []
    for i in range(n):
        ss = list(s)
        if (s[i] == t[0] or s[i] == "?") and i + len(t) <= n:
            pos = 0
            for j in range(i, i + len(t)):
                if s[j] != "?" and s[j] != t[pos]:
                    break
                pos += 1
            else:
                pos = 0
                for j in range(i, i + len(t)):
                    ss[j] = t[pos]
                    pos += 1
                ss = "".join(ss).replace("?", "a")
                res.append(ss)

    if len(res) == 0:
        print("UNRESTORABLE")
    else:
        res = sorted(res)
        print(res[0])


if __name__ == '__main__':
    resolve()

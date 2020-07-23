# https://atcoder.jp/contests/arc027/submissions/15376339
# B - 大事な数なのでZ回書きまLた。
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def dfs(v, p):
        if v.isdigit():
            return True

        for u in edge[ord(v) - ord("A")]:
            if ord(u) - ord("A") == p:
                continue
            else:
                if dfs(u, ord(v) - ord("A")):
                    return True

    n = int(input())
    S = list(input())
    T = list(input())

    edge = [[] for _ in range(26)]
    for s, t in zip(S, T):
        if s != t:
            if s.isdigit() or t.isdigit():
                if s.isdigit():
                    edge[ord(t) - ord("A")].append(s)
                else:
                    edge[ord(s) - ord("A")].append(t)
            else:
                edge[ord(t) - ord("A")].append(s)
                edge[ord(s) - ord("A")].append(t)

    res = 1
    for i in range(n):
        if not dfs(S[i], -1):
            res *= 9 if i == 0 else 10
            edge[ord(S[i]) - ord("A")].append("0")
    print(res)


if __name__ == '__main__':
    resolve()

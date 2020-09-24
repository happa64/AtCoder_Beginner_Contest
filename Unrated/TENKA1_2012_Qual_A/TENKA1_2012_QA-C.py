# https://atcoder.jp/contests/tenka1-2012-qualA/submissions/16985960
# C - 敵対的引用
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())

    route = {}
    for _ in range(m):
        a, b = map(int, input().split())
        if a not in route:
            route[a] = set()
        route[a].add(b)

    S = input().lstrip("\"").split("\"")
    res = {int(S[0].strip("groupw"))}
    for s in S:
        if "w" in s:
            tmp = set()
            for k, v in route.items():
                if res & v:
                    tmp.add(k)
        else:
            tmp = set(range(1, n + 1))
            for k, v in route.items():
                if res <= v:
                    tmp.remove(k)
        res = tmp

    print(len(res))


if __name__ == '__main__':
    resolve()

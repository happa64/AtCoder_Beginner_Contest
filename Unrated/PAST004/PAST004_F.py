# https://atcoder.jp/contests/past202010-open/submissions/18010709
# F - 構文解析
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    S = [input().rstrip() for _ in range(n)]
    D = Counter(S)
    res = [[v, k] for k, v in D.items()]
    res.sort(reverse=True)
    num, ans = res[k - 1]
    cnt = 0
    for v in D.values():
        if v == num:
            cnt += 1

    print(ans if cnt == 1 else "AMBIGUOUS")


if __name__ == '__main__':
    resolve()

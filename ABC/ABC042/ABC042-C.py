# https://atcoder.jp/contests/abc042/submissions/12848498
# C - こだわり者いろはちゃん
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7
res = []


def resolve():
    n, k = map(int, input().split())
    D = set(list(map(int, input().split())))
    Available = []

    for i in range(10):
        if i not in D:
            Available.append(str(i))

    # 使用可能な数値を使って、99999以下の数字を全列挙
    def dfs(Price):
        if len(Price) == 5:
            return

        for value in Available:
            Price.append(value)
            res.append(int("".join(Price)))
            dfs(Price)
            Price.pop()

    dfs([])

    # 列挙した中で、n以上の数値の最小値を返す
    ans = f_inf
    for i in res:
        if i >= n:
            ans = min(ans, i)

    print(ans)


if __name__ == '__main__':
    resolve()

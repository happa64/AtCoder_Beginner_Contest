# https://atcoder.jp/contests/abc131/submissions/10042990
# E - Friendships
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())

    mx = int((n - 1) * (n - 2) / 2)
    if mx < k:
        print(-1)
        exit()

    # スターグラフを作る
    ans = []
    for i in range(n - 1):
        ans.append([i + 1, n])

    # 頂点間に辺をはると、最短距離2を一つ減らせる
    edge = []
    add = int(mx - k)
    for i in range(n - 1):
        for j in range(i):
            edge.append([i + 1, j + 1])

    for i in range(add):
        ans.append(edge[i])

    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])


if __name__ == '__main__':
    resolve()

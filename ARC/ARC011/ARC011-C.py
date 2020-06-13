# https://atcoder.jp/contests/arc011/submissions/14209000
# C - ダブレット
import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    first, last = input().split()
    if first == last:
        print(0)
        print(first)
        print(last)
        exit()

    n = int(input())
    S = [first] + list(input() for _ in range(n)) + [last]

    # 単語をノードとして、一文字違う単語同士にエッジを引く
    tree = [[] for _ in range(n + 2)]
    for i in range(n + 2):
        for j in range(i + 1, n + 2):
            diff = 0
            for s1, s2 in zip(S[i], S[j]):
                if s1 != s2:
                    diff += 1
            if diff == 1:
                tree[i].append(j)
                tree[j].append(i)

    # firstからの距離
    dist = [f_inf] * (n + 2)
    dist[0] = 0
    # 直前に使った単語
    prev = [-1] * (n + 2)
    que = deque([0])
    # 幅優先探索
    while que:
        v = que.popleft()
        for u in tree[v]:
            if dist[u] > dist[v] + 1:
                dist[u] = dist[v] + 1
                prev[u] = v
                que.append(u)

    # lastに辿り着けなかったら-1を出力
    if dist[-1] == f_inf:
        print(-1)
        exit()

    # 経路復元
    pos = n + 1
    res = []
    while pos != -1:
        res.append(S[pos])
        pos = prev[pos]

    print(len(res) - 2)
    print(*res[::-1], sep="\n")


if __name__ == '__main__':
    resolve()

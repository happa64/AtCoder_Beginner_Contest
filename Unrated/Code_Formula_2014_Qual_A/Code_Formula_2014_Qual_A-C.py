# https://atcoder.jp/contests/code-formula-2014-quala/submissions/15702024
# C - 決勝進出者
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())

    res = []
    rank = [0] * (n * k)
    used = set()
    L = k
    for i in range(n):
        A = list(map(int, input().split()))
        for j in range(k):
            idx = j * n + i
            rank[idx] = A[j]

        cnt = 0
        tmp = []
        for l in range(n * k):
            if rank[l] in used:
                continue
            cnt += 1
            if cnt > L:
                break
            if rank[l] != 0:
                tmp.append(rank[l])
                used.add(rank[l])
        tmp.sort()
        res.append(tmp)
        L -= len(tmp)

    for i in res:
        print(*i)


if __name__ == '__main__':
    resolve()

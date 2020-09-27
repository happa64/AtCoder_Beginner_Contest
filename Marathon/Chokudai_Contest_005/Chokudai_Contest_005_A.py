# https://atcoder.jp/contests/chokudai005/submissions/17069423
# A - カラフルパネル
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    T, N, K = map(int, input().split())
    S = [list(input().rstrip()) for _ in range(N)]

    res = []
    max_score = 0
    for target in range(1, 10):
        score = 0
        tmp = []
        visited = [[False] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if visited[i][j]:
                    continue
                if int(S[i][j]) == target:
                    score += 100
                    continue
                tmp.append([i + 1, j + 1, target])
                score -= 1
                que = deque([[i, j]])
                while que:
                    h, w = que.popleft()
                    for dh, dw in ((1, 0), (-1, 0), (0, 0), (0, 1), (0, -1)):
                        next_h, next_w = h + dh, w + dw
                        if next_h < 0 or next_h >= N or next_w < 0 or next_w >= N:
                            continue
                        elif visited[next_h][next_w]:
                            continue
                        else:
                            if S[next_h][next_w] == S[h][w]:
                                visited[next_h][next_w] = True
                                score += 100
                                que.append([next_h, next_w])
        if max_score < score:
            res = tmp
            max_score = score

    print(len(res))
    for i in res:
        print(*i)


if __name__ == '__main__':
    resolve()

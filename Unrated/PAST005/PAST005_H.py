# https://atcoder.jp/contests/past202012-open/submissions/19042662
# H - コンベア
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def main():
    H, W = map(int, input().split())
    r, c = map(lambda x: int(x) - 1, input().split())
    S = tuple(input().rstrip() for _ in range(H))

    ok = [[False] * W for _ in range(H)]
    ok[r][c] = True
    que = deque([(r, c)])
    while que:
        y, x = que.popleft()
        for dy, dx in ([0, 1], [1, 0], [-1, 0], [0, -1]):
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= H or nx < 0 or nx >= W or S[ny][nx] == "#" or ok[ny][nx]:
                continue
            if dy == 1 and not (S[ny][nx] == "^" or S[ny][nx] == "."):
                continue
            if dy == -1 and not (S[ny][nx] == "v" or S[ny][nx] == "."):
                continue
            if dx == 1 and not (S[ny][nx] == "<" or S[ny][nx] == "."):
                continue
            if dx == -1 and not (S[ny][nx] == ">" or S[ny][nx] == "."):
                continue
            ok[ny][nx] = True
            que.append((ny, nx))

    res = [[""] * W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if S[h][w] == "#":
                res[h][w] = "#"
            else:
                res[h][w] = "o" if ok[h][w] else "x"

    for i in res:
        print("".join(i))


if __name__ == '__main__':
    main()

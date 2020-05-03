import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    W, H = map(int, input().split())
    n = int(input())
    XY = [list(map(int, input().split())) for _ in range(n)]

    def DFS(L, R, D, U):
        max_cnt = 0
        for x, y in XY:
            # 範囲外ならスキップ
            if not (L <= x <= R and D <= y <= U):
                continue
            cnt = R - L + U - D + 1
            cnt += DFS(x + 1, R, y + 1, U)
            cnt += DFS(L, x - 1, y + 1, U)
            cnt += DFS(L, x - 1, D, y - 1)
            cnt += DFS(x + 1, R, D, y - 1)
            max_cnt = max(max_cnt, cnt)
        return max_cnt

    ans = DFS(1, W, 1, H)
    print(ans)


if __name__ == '__main__':
    resolve()

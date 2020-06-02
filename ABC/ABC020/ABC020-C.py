# https://atcoder.jp/contests/abc020/submissions/13943212
# C - 壁抜け
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W, T = map(int, input().split())
    grid = [list(input()) for _ in range(H)]

    for h in range(H):
        for w in range(W):
            if grid[h][w] == "S":
                sh, sw = h, w
            elif grid[h][w] == "G":
                gh, gw = h, w

    def is_ok(x):
        """
        幅優先探索でSからGまで向かう最小時間を計算し、それがT秒以内かどうかを返す
        :param x: 黒マスに移動するコスト
        """
        dp = [[f_inf] * W for _ in range(H)]
        dp[sh][sw] = 0
        que = deque([[sh, sw]])
        while que:
            h, w = que.popleft()
            for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_h, next_w = h + dh, w + dw
                if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W:
                    continue

                if grid[next_h][next_w] == "." or grid[next_h][next_w] == "G" or grid[next_h][next_w] == "S":
                    if dp[next_h][next_w] > dp[h][w] + 1:
                        dp[next_h][next_w] = dp[h][w] + 1
                        que.append([next_h, next_w])
                else:
                    if dp[next_h][next_w] > dp[h][w] + x:
                        dp[next_h][next_w] = dp[h][w] + x
                        que.append([next_h, next_w])
        return dp[gh][gw] <= T

    def meguru_bisect(ng, ok):
        """
        初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
        まずis_okを定義すべし
        ng ok は  とり得る最小の値-1 とり得る最大の値+1
        最大最小が逆の場合はよしなにひっくり返す
        """
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    ok = 0
    ng = 10 ** 9
    res = meguru_bisect(ng, ok)
    print(res)


if __name__ == '__main__':
    resolve()

# https://atcoder.jp/contests/abc020/submissions/13998312
# C - 壁抜け
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


class BinarySearch:
    def meguru_bisect(self, is_ok, left, right):
        """
        :param is_ok: 定義して下さい
        :param left: 取りうる最小の値-1
        :param right: 取りうる最大の値+1
        :return: is_okを満たす最小(もしくは最大)の値
        """
        while abs(left - right) > 1:
            mid = (left + right) // 2
            if is_ok(mid):
                left = mid
            else:
                right = mid
        return left


def resolve():
    def bfs(x):
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
                if grid[next_h][next_w] == "." or grid[next_h][next_w] == "G":
                    if dp[next_h][next_w] > dp[h][w] + 1:
                        dp[next_h][next_w] = dp[h][w] + 1
                        que.append([next_h, next_w])
                else:
                    if dp[next_h][next_w] > dp[h][w] + x:
                        dp[next_h][next_w] = dp[h][w] + x
                        que.append([next_h, next_w])
        return dp[gh][gw] <= T

    H, W, T = map(int, input().split())
    grid = [list(input()) for _ in range(H)]

    for h in range(H):
        for w in range(W):
            if grid[h][w] == "S":
                sh, sw = h, w
            elif grid[h][w] == "G":
                gh, gw = h, w

    bs = BinarySearch()
    res = bs.meguru_bisect(bfs, 0, 10 ** 9)
    print(res)


if __name__ == '__main__':
    resolve()

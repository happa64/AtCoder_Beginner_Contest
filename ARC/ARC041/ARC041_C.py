# https://atcoder.jp/contests/arc041/submissions/16801444
# C - ウサギ跳び
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def calc(res, cnt_L, cnt_R):
        if cnt_L > cnt_R:
            target = que_R.pop() if que_R else 0
            r = target
            while que_R:
                prev_x = que_R.pop()
                res += r - prev_x - 1
                r -= 1
            l = target
            while que_L:
                prev_x = que_L.popleft()
                res += prev_x - l - 1
                l += 1
        else:
            target = que_L.popleft() if que_L else L + 1
            l = target
            while que_L:
                prev_x = que_L.popleft()
                res += prev_x - l - 1
                l += 1
            r = target
            while que_R:
                prev_x = que_R.pop()
                res += r - prev_x - 1
                r -= 1
        return res

    N, L = map(int, input().split())
    XD = [list(input().split()) for _ in range(N)]

    res = 0
    prev = None
    cnt_L = cnt_R = 0
    que_L, que_R = deque(), deque()
    for x, d in XD:
        x = int(x)
        if prev == "L" and d == "R":
            res = calc(res, cnt_L, cnt_R)
            prev = "R"
            cnt_L, cnt_R = 0, 1
            que_R.append(x)
        else:
            if d == "R":
                prev = "R"
                cnt_R += 1
                que_R.append(x)
            else:
                prev = "L"
                cnt_L += 1
                que_L.append(x)

    res = calc(res, cnt_L, cnt_R)
    print(res)


if __name__ == '__main__':
    resolve()

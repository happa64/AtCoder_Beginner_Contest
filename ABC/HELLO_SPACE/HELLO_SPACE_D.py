# https://atcoder.jp/contests/zone2021/submissions/22217587
# D - 宇宙人からのメッセージ
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
if sys.platform == 'ios':
    sys.stdin = open('input_file.txt')
else:
    input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    S = input().rstrip()

    que = deque()
    flg = 1
    for s in S:
        if s == "R":
            flg ^= 1
        else:
            if flg:
                if que and que[-1] == s:
                    que.pop()
                    continue
                que.append(s)
            else:
                if que and que[0] == s:
                    que.popleft()
                    continue
                que.appendleft(s)
    if not flg:
        que = reversed(que)

    res = "".join(que)
    print(res)


if __name__ == '__main__':
    solve()
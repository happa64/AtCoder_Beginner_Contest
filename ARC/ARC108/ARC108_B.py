# https://atcoder.jp/contests/arc108/submissions/18258895
# B - Abbreviate Fox
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = input()

    que = deque()
    for s in S:
        que.append(s)
        while len(que) >= 3 and que[-3] == "f" and que[-2] == "o" and que[-1] == "x":
            for _ in range(3):
                que.pop()
    print(len(que))


if __name__ == '__main__':
    resolve()

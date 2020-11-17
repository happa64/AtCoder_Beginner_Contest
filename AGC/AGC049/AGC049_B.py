# https://atcoder.jp/contests/agc049/submissions/18189482
# B - Flip Digits
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = list(input())
    T = list(input())

    que = deque()
    for i in range(n):
        if S[i] == "1":
            que.append(i)

    res = 0
    for i in range(n):
        s, t = S[i], T[i]
        if s == t:
            if s == "1":
                que.popleft()
        else:
            if s == "1" and t == "0":
                if len(que) < 2:
                    print(-1)
                    exit()
                que.popleft()
                j = que.popleft()
                res += j - (i + 1) + 1
                S[i] = "0"
            else:
                if not que:
                    print(-1)
                    exit()
                j = que.popleft()
                res += j - i
                S[i] = "1"
            S[j] = "0"
    print(res)


if __name__ == '__main__':
    resolve()

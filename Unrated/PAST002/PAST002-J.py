# https://atcoder.jp/contests/past202004-open/submissions/13678731
# J - 文字列解析
import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = deque(list(input().rstrip()))

    T = deque([])

    while S:
        s = S.popleft()
        if s == ")":
            tmp = []
            while T:
                t = T.pop()
                if t == "(":
                    break
                tmp.append(t)
            T.extend(tmp[::-1] + tmp)
        else:
            T.append(s)

    print("".join(T))






if __name__ == '__main__':
    resolve()

# https://atcoder.jp/contests/past202104-open/submissions/22052120
# E - 前から3番目
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    S = input()

    que = deque()
    for i in range(n):
        if S[i] == "L":
            que.appendleft(str(i + 1))
        elif S[i] == "R":
            que.append(str(i + 1))
        elif S[i] == "A":
            if len(que) <= 0:
                print("ERROR")
            else:
                print(que.popleft())
        elif S[i] == "B":
            if len(que) <= 1:
                print("ERROR")
            else:
                a = que.popleft()
                print(que.popleft())
                que.appendleft(a)
        elif S[i] == "C":
            if len(que) <= 2:
                print("ERROR")
            else:
                a = que.popleft()
                b = que.popleft()
                print(que.popleft())
                que.appendleft(b)
                que.appendleft(a)
        elif S[i] == "D":
            if len(que) <= 0:
                print("ERROR")
            else:
                print(que.pop())
        elif S[i] == "E":
            if len(que) <= 1:
                print("ERROR")
            else:
                a = que.pop()
                print(que.pop())
                que.append(a)
        else:
            if len(que) <= 2:
                print("ERROR")
            else:
                a = que.pop()
                b = que.pop()
                print(que.pop())
                que.append(b)
                que.append(a)


if __name__ == '__main__':
    solve()

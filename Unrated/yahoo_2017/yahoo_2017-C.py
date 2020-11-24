# https://atcoder.jp/contests/yahoo-procon2017-qual/submissions/18383404
# C - 検索
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    A = set(list(map(lambda x: int(x) - 1, input().split())))
    S = [input().rstrip() for _ in range(n)]

    hit = []
    no_hit = []
    for i in range(n):
        hit.append(S[i]) if i in A else no_hit.append(S[i])

    if len(no_hit) == 0:
        print("")
        exit()

    max_string = deque(list(hit[0]))
    for string in hit:
        tmp = deque()
        for ms, s in zip(max_string, string):
            if ms == s:
                tmp.append(ms)
            else:
                break
        max_string = tmp

    if len(max_string) == 0:
        print(-1)
        exit()

    res = ""
    res += max_string.popleft()
    for word in no_hit:
        while len(res) <= len(word) and word[:len(res)] == res:
            if not max_string:
                print(-1)
                exit()
            res += max_string.popleft()
    print(res)


if __name__ == '__main__':
    resolve()

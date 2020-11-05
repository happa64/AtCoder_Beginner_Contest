# https://atcoder.jp/contests/dwacon2018-prelims/submissions/17889979
# B - 2525文字列分解
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input()
    cnt2 = 0
    cnt5 = 0
    for s in S:
        if cnt2 < cnt5:
            print(-1)
            exit()
        if s == "2":
            cnt2 += 1
        else:
            cnt5 += 1

    if cnt2 != cnt5:
        print(-1)
        exit()

    res = 0
    used = set()
    while len(used) != len(S):
        que = []
        res += 1
        for i in range(len(S)):
            if i in used:
                continue
            if not que:
                if S[i] == "2":
                    que.append("2")
                    used.add(i)
            else:
                if que[-1] == "2" and S[i] == "5":
                    que.append("5")
                    used.add(i)
                elif que[-1] == "5" and S[i] == "2":
                    que.append("2")
                    used.add(i)
    print(res)


if __name__ == '__main__':
    resolve()

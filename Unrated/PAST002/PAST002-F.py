# https://atcoder.jp/contests/past202004-open/tasks/past202004_f
# F - タスクの消化
import sys
import heapq
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    AB = []
    # heapを使うため、bに-1をかけて配列に入れる
    for i in range(n):
        a, b = map(int, input().split())
        AB.append([a, -b])
    # 日程順に昇順ソートする
    AB = sorted(AB, key=lambda x: x[0])
    que = [0]
    heapq.heapify(que)

    pos = 0
    i = 1
    res = 0
    ans = []
    while que:
        # i日目までに消化できるタスクをqueに入れていく
        if pos < n and AB[pos][0] <= i:
            heapq.heappush(que, AB[pos][1])
            pos += 1
        # 入れられるタスクが無くなったら、queの中からポイントが高いタスクを消化し、次の日へ行く
        else:
            point = heapq.heappop(que) * (-1)
            res += point
            ans.append(res)
            i += 1

    for i in range(n):
        print(ans[i])


if __name__ == '__main__':
    resolve()

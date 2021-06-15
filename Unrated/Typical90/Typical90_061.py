# https://atcoder.jp/contests/typical90/submissions/23293342
# 061 - Deck（★2）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


class Deque:
    """ 両端の数値をO(1)で取り出し可能かつ、ランダムアクセスがO(1)で可能な両端キュー """

    def __init__(self):
        self.front = []
        self.back = []

    def push_front(self, x: int):
        """ キューの先頭にxを追加 """
        self.front.append(x)

    def push_back(self, x: int):
        """ キューの最後尾にxを追加 """
        self.back.append(x)

    def get_kth_num(self, k: int):
        """ キューのk番目(0-index)の値を返す """
        if k < len(self.front):
            return self.front[-(k + 1)]
        else:
            k -= len(self.front)
            return self.back[k]


def solve():
    q = int(input())
    que = Deque()
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            que.push_front(x)
        elif t == 2:
            que.push_back(x)
        else:
            print(que.get_kth_num(x - 1))


if __name__ == '__main__':
    solve()

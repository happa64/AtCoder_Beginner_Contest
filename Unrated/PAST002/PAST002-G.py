# https://atcoder.jp/contests/past202004-open/tasks/past202004_g
# G - ストリング・クエリ
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    query = [list(map(str, input().split())) for _ in range(n)]
    que = deque([])

    for i in range(n):
        # クエリ；１ならqueの末尾に、挿入する文字と文字の長さを挿入する
        if query[i][0] == "1":
            _, c, x = query[i]
            que.append([c, int(x)])
        else:
            res = 0
            _, d = query[i]
            d = int(d)
            delete_list = dict()
            # クエリ：２なら、dがゼロになるか、queが空になるまで以下の操作を行う
            while d and que:
                c, x = que[0]
                # 文字の長さがdより小さければ、文字を削除し、キー；文字、バリュー；文字の長さとした辞書を作成する（元々キーがあれば加算）
                if x <= d:
                    que.popleft()
                    delete_list[c] = delete_list.get(c, 0) + x
                    d -= x
                # 文字の長さがdより大きければ、文字の長さからdを引き、キー；文字、バリュー；dとした辞書を作成する（元々キーがあれば加算）
                else:
                    que[0][1] = int(que[0][1]) - d
                    delete_list[c] = delete_list.get(c, 0) + d
                    d = 0

            # 辞書からバリューを取り出して、2乗した和を計算
            for v in delete_list.values():
                res += pow(v, 2)

            print(res)


if __name__ == '__main__':
    resolve()

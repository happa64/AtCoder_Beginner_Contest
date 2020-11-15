class Avltree:
    """
    AVL木
    Methods
    -------
        search(x: int) -> Union(int)
            ◯.data == x のものが存在するある場合それを出力、ない場合 None を返す
        insert(x: int) -> None
            ◯.data == x がない場合 ◯.data == x なる頂点を作る。ある場合はなにもしない（上書きしない）
        y.to_s() -> int
            頂点yのdataを返す
        y.left_s() -> Union(int, key=None)
            頂点yのleftを返す(ない場合は key)
        search_lower(x: int, key_lower) -> int
            ○.data が x より小さいものの中で最も大きいものを出力、ない場合 key_lower を返す
        search_higher(x:int , key_higher) -> int
            ○.data が x より大きいものの中で最も小さいものを出力、ない場合 key_higher を返す
    """
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
        self.balance = "Even"

    def search(self, key):
        node = self
        while node is not None:
            if node.key == key:
                return node  # node.key == keyの場合
            if node.key > key:
                node = node.left
            elif node.key < key:
                node = node.right
        return None

    def search_lower(self, key, key_lower):
        node = self
        if node.key is None:
            return key_lower
        ans = key_lower
        while node is not None:
            if node.key < key:
                if ans < node.key:
                    ans = node.key
                node = node.right
            elif node.key >= key:
                node = node.left
        return ans

    def search_higher(self, key, key_higher):
        node = self
        if node.key is None:
            return key_higher
        ans = key_higher
        while node is not None:
            if node.key > key:
                if ans > node.key:
                    ans = node.key
                node = node.left
            elif node.key <= key:
                node = node.right
        return ans

    def end_lower(self, end_lower_key):
        node = self
        while node.left is not None:
            node = node.left
        return node.key

    def end_higher(self, end_higher_key):
        node = self
        while node.right is not None:
            node = node.right
        return node.key

    def DoubleRightRotation(self):
        tl = self.left
        self.left = tl.right.right
        tl.right.right = self  # selfはそのノード
        tlr = tl.right
        tl.right = tlr.left
        tlr.left = tl
        if tlr.balance == "Left":
            tlr.right.balance = "Right"
            tlr.left.balance = "Even"
        elif tlr.balance == "Right":
            tlr.right.balance = "Even"
            tlr.left.balance = "Left"
        elif tlr.balance == "Even":
            tlr.right.balance = "Even"
            tlr.left.balance = "Even"
        tlr.balance = "Even"
        return tlr

    def DoubleLeftRotation(self):
        tr = self.right
        self.right = tr.left.left
        tr.left.left = self
        trl = tr.left
        tr.left = trl.right
        trl.right = tr
        if trl.balance == "Right":
            trl.left.balance = "Left"
            trl.right.balance = "Even"
        elif trl.balance == "Left":
            trl.left.balance = "Even"
            trl.right.balance = "Right"
        elif trl.balance == "Even":
            trl.left.balance = "Even"
            trl.right.balance = "Even"
        trl.balance = "Even"
        return trl

    def SingleLeftRotation(self):
        tr = self.right
        tr.balance = "Even"
        self.balance = "Even"
        self.right = tr.left
        tr.left = self
        return tr

    def SingleRightRotation(self):
        tl = self.left
        tl.balance = "Even"
        self.balance = "Even"
        self.left = tl.right
        tl.right = self
        return tl

    def replace(self, p, v):  # 親ノードpの下にある自分(self)をvに置き換える。
        if p.left == self:
            p.left = v
        else:
            p.right = v

    def insert(self, key):  # rootでのみ呼ばれる挿入
        if self.key is None:  # rootを含むrotationはしないことにする。
            self.key = key
            return self
        if key < self.key:
            if self.left is None:
                self.left = Avltree(key)
            else:
                self.left.insertx(self, key)
        elif key > self.key:
            if self.right is None:
                self.right = Avltree(key)
            else:
                self.right.insertx(self, key)
        else:  # key == self.key:
            pass  # do not overwrite

    def insertx(self, p, key):  # replaceを呼ぶために一つ上の親を持っているinsert
        node = self
        s = []
        while True:
            if node.key > key:
                s.append((node, -1))
                if node.left is None:
                    node.left = Avltree(key)
                    node = node.left
                    break
                else:
                    node = node.left
            elif node.key < key:
                s.append((node, 1))
                if node.right is None:
                    node.right = Avltree(key)
                    node = node.right
                    break
                else:
                    node = node.right
        while len(s) != 0:
            node, direct = s.pop()
            if len(s) != 0:
                par = s[-1][0]
            else:
                par = p
            if direct == -1:
                if node.balance == "Right":
                    node.balance = "Even"
                    break
                elif node.balance == "Even":
                    node.balance = "Left"
                elif node.balance == "Left":
                    if node.left.balance == "Right":
                        node.replace(par, node.DoubleRightRotation())
                    elif node.left.balance == "Left":
                        node.replace(par, node.SingleRightRotation())
                    break
            elif direct == 1:
                if node.balance == "Left":
                    node.balance = "Even"
                    break
                elif node.balance == "Even":
                    node.balance = "Right"
                elif node.balance == "Right":
                    if node.right.balance == "Left":
                        node.replace(par, node.DoubleLeftRotation())
                    elif node.right.balance == "Right":
                        node.replace(par, node.SingleLeftRotation())
                    break

    def to_s(self):
        return self.key

    def left_s(self):
        if self.left is None:
            return None
        return (self.left).key

    def right_s(self):
        if self.right is None:
            return None
        return (self.right).key


class BalancingTree:
    def __init__(self, n):
        self.N = n
        self.root = self.node(1 << n, 1 << n)

    def debug(self):
        def debug_info(nd_):
            return (nd_.value - 1, nd_.pivot - 1, nd_.left.value - 1 if nd_.left else -1,
                    nd_.right.value - 1 if nd_.right else -1)

        def debug_node(nd):
            re = []
            if nd.left:
                re += debug_node(nd.left)
            if nd.value: re.append(debug_info(nd))
            if nd.right:
                re += debug_node(nd.right)
            return re

        print("Debug - root =", self.root.value - 1, debug_node(self.root)[:50])

    def append(self, v):  # v を追加（その時点で v はない前提）
        v += 1
        nd = self.root
        while True:
            if v == nd.value:
                # v がすでに存在する場合に何か処理が必要ならここに書く
                return 0
            else:
                mi, ma = min(v, nd.value), max(v, nd.value)
                if mi < nd.pivot:
                    nd.value = ma
                    if nd.left:
                        nd = nd.left
                        v = mi
                    else:
                        p = nd.pivot
                        nd.left = self.node(mi, p - (p & -p) // 2)
                        break
                else:
                    nd.value = mi
                    if nd.right:
                        nd = nd.right
                        v = ma
                    else:
                        p = nd.pivot
                        nd.right = self.node(ma, p + (p & -p) // 2)
                        break

    def leftmost(self, nd):
        if nd.left: return self.leftmost(nd.left)
        return nd

    def rightmost(self, nd):
        if nd.right: return self.rightmost(nd.right)
        return nd

    def find_l(self, v):  # vより真に小さいやつの中での最大値（なければ-1）
        v += 1
        nd = self.root
        prev = 0
        if nd.value < v: prev = nd.value
        while True:
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                prev = nd.value
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    def find_r(self, v):  # vより真に大きいやつの中での最小値（なければRoot）
        v += 1
        nd = self.root
        prev = 0
        if nd.value > v: prev = nd.value
        while True:
            if v < nd.value:
                prev = nd.value
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    @property
    def max(self):
        return self.find_l((1 << self.N) - 1)

    @property
    def min(self):
        return self.find_r(-1)

    def delete(self, v, nd=None, prev=None):  # 値がvのノードがあれば削除（なければ何もしない）
        v += 1
        if not nd: nd = self.root
        if not prev: prev = nd
        while v != nd.value:
            prev = nd
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return
        if (not nd.left) and (not nd.right):
            if nd.value < prev.value:
                prev.left = None
            else:
                prev.right = None
        elif not nd.left:
            if nd.value < prev.value:
                prev.left = nd.right
            else:
                prev.right = nd.right
        elif not nd.right:
            if nd.value < prev.value:
                prev.left = nd.left
            else:
                prev.right = nd.left
        else:
            nd.value = self.leftmost(nd.right).value
            self.delete(nd.value - 1, nd.right, nd)

    def __contains__(self, v: int) -> bool:
        return self.find_r(v - 1) == v

    class node:
        def __init__(self, v, p):
            self.value = v
            self.pivot = p
            self.left = None
            self.right = None

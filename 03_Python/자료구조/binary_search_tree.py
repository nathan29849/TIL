from linked_binary_tree import LinkedBinaryTree
from map_base import MapBase


class TreeMap(LinkedBinaryTree, MapBase):

    # ---------------------------- override Position class ----------------------------
    class Position(LinkedBinaryTree.Position):
        def key(self):
            return self.element()._key

        def value(self):
            return self.element()._value

    # ------------------------------- nonpublic utilities -------------------------------
    def _subtree_search(self, p, k):
        if k == p.key():                                   # found match
            return p
        elif k < p.key():                                  # search left subtree
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        else:                                              # search right subtree
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        return p                                           # unsucessful search

    def _subtree_first_position(self, p):
        walk = p
        while self.left(walk) is not None:                 # keep walking left
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p):
        walk = p
        while self.right(walk) is not None:                # keep walking right
            walk = self.right(walk)
        return walk

    # --------------------- public methods providing "positional" support ---------------------
    def first(self):
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self, p):
        self._validate(
            p)                            # inherited from LinkedBinaryTree
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            # walk upward
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def after(self, p):
        self._validate(p)                            # inherited from LinkedBinaryTree
        if self.right(p):
            return self._subtree_first_position(self.right(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
            return above

    def find_position(self, k):
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            # hook for balanced tree subclasses
            self._rebalance_access(p)
            return p

    def delete(self, p):
        self._validate(
            p)                            # inherited from LinkedBinaryTree
        if self.left(p) and self.right(p):           # p has two children
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element())    # from LinkedBinaryTree
            p = replacement
        # now p has at most one child
        parent = self.parent(p)
        # inherited from LinkedBinaryTree
        self._delete(p)
        # if root deleted, parent is None
        self._rebalance_delete(parent)

    # --------------------- public methods for (standard) map interface ---------------------
    def __getitem__(self, k):
        if self.is_empty():
            raise KeyError('Key Error: ' + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            # hook for balanced tree subclasses
            self._rebalance_access(p)
            if k != p.key():
                raise KeyError('Key Error: ' + repr(k))
            return p.value()

    def __setitem__(self, k, v):
        if self.is_empty():
            leaf = self._add_root(self._Item(k, v))     # from LinkedBinaryTree
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                p.element()._value = v                   # replace existing item's value
                # hook for balanced tree subclasses
                self._rebalance_access(p)
                return
            else:
                item = self._Item(k, v)
                if p.key() < k:
                    # inherited from LinkedBinaryTree
                    leaf = self._add_right(p, item)
                else:
                    # inherited from LinkedBinaryTree
                    leaf = self._add_left(p, item)
        # hook for balanced tree subclasses
        self._rebalance_insert(leaf)

    def __delitem__(self, k):
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                # rely on positional version
                self.delete(p)
                return                                   # successful deletion complete
            # hook for balanced tree subclasses
            self._rebalance_access(p)
        raise KeyError('Key Error: ' + repr(k))

    def __iter__(self):
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)

    # --------------------- public methods for sorted map interface ---------------------
    def __reversed__(self):
        p = self.last()
        while p is not None:
            yield p.key()
            p = self.before(p)

    def find_min(self):
        if self.is_empty():
            return None
        else:
            p = self.first()
            return (p.key(), p.value())

    def find_max(self):
        if self.is_empty():
            return None
        else:
            p = self.last()
            return (p.key(), p.value())

    def find_le(self, k):
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if k < p.key():
                p = self.before(p)
            return (p.key(), p.value()) if p is not None else None

    def find_lt(self, k):
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if not p.key() < k:
                p = self.before(p)
            return (p.key(), p.value()) if p is not None else None

    def find_ge(self, k):
        if self.is_empty():
            return None
        else:
            # may not find exact match
            p = self.find_position(k)
            if p.key() < k:                             # p's key is too small
                p = self.after(p)
            return (p.key(), p.value()) if p is not None else None

    def find_gt(self, k):
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if not k < p.key():
                p = self.after(p)
            return (p.key(), p.value()) if p is not None else None

    def find_range(self, start, stop):
        if not self.is_empty():
            if start is None:
                p = self.first()
            else:
                # we initialize p with logic similar to find_ge
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)
            while p is not None and (stop is None or p.key() < stop):
                yield (p.key(), p.value())
                p = self.after(p)

    # --------------------- hooks used by subclasses to balance a tree ---------------------
    def _rebalance_insert(self, p):
        pass

    def _rebalance_delete(self, p):
        pass

    def _rebalance_access(self, p):
        pass

    # --------------------- nonpublic methods to support tree balancing ---------------------

    def _relink(self, parent, child, make_left_child):
        if make_left_child:                           # make it a left child
            parent._left = child
        else:                                         # make it a right child
            parent._right = child
        if child is not None:                         # make child point to parent
            child._parent = parent

    def _rotate(self, p):
        x = p._node
        y = x._parent                                 # we assume this exists
        # grandparent (possibly None)
        z = y._parent
        if z is None:
            self._root = x                              # x becomes root
            x._parent = None
        else:
            # x becomes a direct child of z
            self._relink(z, x, y == z._left)
        # now rotate x and y, including transfer of middle subtree
        if x == y._left:
            # x._right becomes left child of y
            self._relink(y, x._right, True)
            # y becomes right child of x
            self._relink(x, y, False)
        else:
            # x._left becomes right child of y
            self._relink(y, x._left, False)
            # y becomes left child of x
            self._relink(x, y, True)

    def _restructure(self, x):
        y = self.parent(x)
        z = self.parent(y)
        if (x == self.right(y)) == (y == self.right(z)):  # matching alignments
            # single rotation (of y)
            self._rotate(y)
            return y                                        # y is new subtree root
        else:                                             # opposite alignments
            # double rotation (of x)
            self._rotate(x)
            self._rotate(x)
            return x                                        # x is new subtree root

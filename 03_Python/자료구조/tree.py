import collections

class Tree:

  class Position:
    def element(self):
      raise NotImplementedError('must be implemented by subclass')
      
    def __eq__(self, other):
      raise NotImplementedError('must be implemented by subclass')

    def __ne__(self, other):
      return not (self == other)            # opposite of __eq__

  def root(self):
    raise NotImplementedError('must be implemented by subclass')

  def parent(self, p):
    raise NotImplementedError('must be implemented by subclass')

  def num_children(self, p):
    raise NotImplementedError('must be implemented by subclass')

  def children(self, p):
    raise NotImplementedError('must be implemented by subclass')

  def __len__(self):
    raise NotImplementedError('must be implemented by subclass')

  def is_root(self, p):
    """Return True if Position p represents the root of the tree."""
    return self.root() == p

  def is_leaf(self, p):
    return self.num_children(p) == 0

  def is_empty(self):
    return len(self) == 0

  def depth(self, p):
    if self.is_root(p):
      return 0
    else:
      return 1 + self.depth(self.parent(p))

  def _height(self, p):                  # time is linear in size of subtree
    if self.is_leaf(p):
      return 0
    else:
      return 1 + max(self._height(c) for c in self.children(p))

  def height(self, p=None):
    if p is None:
      p = self.root()
    return self._height(p)        # start _height2 recursion

  def __iter__(self):
    for p in self.positions():                        # use same order as positions()
      yield p.element()                               # but yield each element

  def positions(self):
    return self.preorder()                            # return entire preorder iteration

  def preorder(self):
    if not self.is_empty():
      for p in self._subtree_preorder(self.root()):  # start recursion
        yield p

  def _subtree_preorder(self, p):
    yield p                                           # visit p before its subtrees
    for c in self.children(p):                        # for each child c
      for other in self._subtree_preorder(c):         # do preorder of c's subtree
        yield other                                   # yielding each to our caller

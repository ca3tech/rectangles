from typing import List
import math

def get_rectangles(points : List[tuple]) -> List[List[tuple]]:
    pgraph = graph(points)
    r = pgraph.get_rectangles()
    print_rectangles(r)
    return r

def num_rectangles(points : List[tuple]) -> int:
    return len(get_rectangles(points))

def print_rectangles(rectangles : List[List[tuple]]):
    print("[")
    for p in rectangles:
        print(f"    {p}")
    print("]")

class node(object):
    def __init__(self, point : tuple):
        self._point = point
        self._rot_sum = 0.0
        self._predecessor : node = None
        self._successors : List[node] = []

    @property
    def point(self) -> tuple:
        return self._point

    @property
    def successors(self):
        # type: (node) -> List[node]
        return self._successors

    def add_successor(self, succ_node):
        # type: (node, node)
        self._successors.append(succ_node)
        succ_node.predecessor = self
    
    @property
    def predecessor(self):
        # type: (node) -> node
        return self._predecessor
    
    @predecessor.setter
    def predecessor(self, pred_node):
        # type: (node, node)
        self._predecessor = pred_node

class graph(object):
    def __init__(self, points : List[tuple]):
        if len(points) < 4:
            raise Exception("Rectangles cannot be built from less than 4 points")
        self._ops = 0
        self._points = points
        self._leafs = []
        self._rectangles : List[List[tuple]] = None

    def get_rectangles(self) -> List[List[tuple]]:
        if self._rectangles is None:
            self._build_trees()
            # _build_trees will add the leaf node of each path
            # computed to the _leafs attribute. Now we need to
            # walk up the tree to reconstruct the set of points
            # that were navigated to form the rectangle paths.
            r = []
            for l in self._leafs:
                self._ops += 1
                p = self._get_path(l)
                if p[0] == p[len(p)-1]:
                    r.append(p)
            # Multiple sequences of points can define the same
            # rectangle, therefore, we need to trim the rectangles
            # determined above to a unique set of rectangles.
            self._rectangles = self._unique_paths(r)
        return self._rectangles

    @property
    def operations(self) -> int:
        return self._ops

    def _unique_paths(self, paths : List[List[tuple]]) -> List[List[tuple]]:
        def point_sorter(t):
            return float(f"{t[0]}.{t[1]}")
        keys = []
        for path in paths:
            self._ops += 1
            path.sort(key=point_sorter)
            tstr = list(set([f"{_}" for _ in path]))
            keys.append(",".join(tstr))
        pdict = dict(zip(keys, paths))
        return [_ for _ in pdict.values()]
        
    def _get_path(self, lnode : node) -> List[tuple]:
        # Given a node in a tree return the sequence of
        # points leading to it
        p = [lnode.point]
        cn = lnode
        while cn.predecessor is not None:
            self._ops += 1
            pn = cn.predecessor
            p = [pn.point] + p
            cn = pn
        return p
    
    def _build_trees(self):
        # For each input point, build a tree rooted at
        # that point. All paths through the trees will
        # correspond to a sequence of points that can
        # be connected to form a rectangle.
        for p1 in self._points:
            self._ops += 1
            self._build_tree(node(p1))

    def _build_tree(self, pnode, depth = 1):
        # type: (graph, node, int)
        if depth == 5:
            # This is a leaf node since a closed rectangular
            # path consists of 5 points
            self._leafs.append(pnode)
        else:
            # Find all points to which this node is connected
            # that form a right angle with this and the
            # predecessor node
            for p in self._points:
                self._ops += 1
                nn = node(p)
                if pnode.predecessor is None:
                    # The input node is a root node and so long as
                    # the current node is not that node, then it forms
                    # a potential connection in a rectangular path.
                    if pnode.point == p:
                        # This is the same point so throw it out
                        nn = None
                elif pnode.point == p or pnode.predecessor.point == p:
                    # This is the same point as the input node or the
                    # input nodes predecessor so throw it out
                    nn = None
                else:
                    # If the predecessor point, input node point, and
                    # the current point form a right angle then they
                    # potentially form a corner of a rectangle
                    a1 = __angle__(pnode.predecessor, pnode)
                    a2 = __angle__(pnode, nn)
                    if abs(a1) + abs(a2) != math.pi / 2:
                        # They don't forma right angle so throw it out
                        nn = None
                if nn is not None:
                    # The current node is potentially connected to the
                    # input node in a rectangular path, therefore, we
                    # connect the 2 nodes in the graph, then we build
                    # out the rest of the tree below the current node.
                    pnode.add_successor(nn)
                    nn.predecessor = pnode
                    self._build_tree(nn, depth + 1)

def __angle__(node1, node2):
    # type: (node, node) -> float
    dx = node2.point[0] - node1.point[0]
    dy = node2.point[1] - node1.point[1]
    s = math.inf
    if dx != 0:
        s = dy / dx
    return math.atan(s)

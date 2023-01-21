
import changable
import pickle
import math
from collections import Counter, defaultdict



with open('data/cir_graph.p', 'rb') as f:
    graph = pickle.load(f)


class Node:
    char_graph = graph

    def __init__(self, parent, curr_char, history = {}):
        self.n, self.w = 0, 0
        self.parent = parent
        self.curr_char = curr_char
        self.history = history
        self.children = {}

    def select(self):
        children = self.children.values()
        selectedChild = max(children, lambda x : x.UTC())
        return selectedChild
    
    def UTC(self):
        return self.w / self.n + math.sqrt(2 * math.log(self.t()) / self.n)
    
    def t(self):
        return self.parent.n
    
    def expand(self):
        for char in self.nextChar():
            if char not in self.children:
                history = self.history.copy()
                if char not in history:
                    history[char] = set()
                history[char].add(char)
                return Node(self, char, )

    def nextChar(self):
        result = []
        for char in changable.changable(self.curr_char):
            if char in self.history:
                result += list(Node.char_graph[char] - self.history[char])
        return Counter(result)
        


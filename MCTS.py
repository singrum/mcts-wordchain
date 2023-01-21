
import changable
import pickle
import math
from collections import Counter, defaultdict




with open('data/cir_graph.p', 'rb') as f:
    all_words_graph = pickle.load(f)

def copy(object):
    return {k: v.copy() for (k, v) in object.items()}

def filter(object): # object = Counter
    for val, key in object.items():
        if key == 0:
            object.pop(val)


class Node:
    def __init__(self, parent, curr_char, graph = all_words_graph):
        self.n, self.w = 0, 0
        self.parent = parent
        self.curr_char = curr_char
        self.graph = graph
        self.children = {}

    def select(self):
        children = self.children.values()
        selectedChild = max(children, key = lambda x : x.UTC())
        return selectedChild
    
    def UTC(self):
        return self.w / self.n + math.sqrt(2 * math.log(self.t()) / self.n)
    
    def t(self):
        return self.parent.n
    
    def expand(self):
        
        for char in self.nextChar():
            if char not in self.children:
                graph_copy = copy(self.graph)
                for c in changable.changable(self.curr_char):
                    if c not in graph_copy:
                        continue
                    if char in graph_copy[c]:
                        graph_copy[c][char] -= 1
                        if graph_copy[c][char] == 0:
                            graph_copy[c].pop(char)
                child = Node(self, char, graph_copy)
                self.children[char] = child
                return child

    def nextChar(self):
        result = Counter({})
        for char in changable.changable(self.curr_char):
            if char not in self.graph:
                continue
            result += self.graph[char]
        return result
        
    def isEnd(self):
        return False if self.nextChar() else True
    
    def isComplete(self):
        return len(self.children) == len(self.nextChar())

    def __str__(self):
        return self.curr_char

    def __repr__(self):
        return f'({self.curr_char})'


stack = []
def simulate(root, stack):
    ptr = root
    stack.append(ptr)
    while ptr.nextChar():
        if ptr.isComplete():
            ptr = ptr.select()
        else:
            ptr = ptr.expand()
        stack.append(ptr)
def backpropagate(stack):
    alternater = True
    while stack:
        node = stack.pop()
        node.n += 1
        if alternater:
            node.w += 1

        alternater = not alternater

def learn(root, stack,num = 100):
    for i in range(num):
        print(f'{i}회')
        simulate(root, stack)
        backpropagate(stack)
    print(max(root.children, key = lambda x : root.children[x].w))

learn(Node(None, '족'), stack, 1000)

# dictionary 대신 graph로 바꾸자
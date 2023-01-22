
import changable
import pickle
import math
import wordchain as wc
import various_rules as vr
from collections import Counter, defaultdict

def makePickle():
    wm = wc.WordManager(vr.Kor())
    graph = {}
    for cir in wm.cir_index:
        counter = Counter({})
        graph[cir] = counter
        for word in wm.rule.word_dict[cir]:
            if word[-1] in wm.cir_index:
                counter[word[-1]] += 1
    with open('data/cir_graph.p', 'wb') as f:
        pickle.dump(graph,f)

def getGraph():
    with open('data/cir_graph.p', 'rb') as f:
        graph = pickle.load(f)
    return graph

all_words_graph = getGraph()



def copy(object):
    return {k: v.copy() for (k, v) in object.items()}

def filter(object): # object = Counter
    for val, key in object.items():
        if key == 0:
            object.pop(val)

def makeChangableNode(graph):
    changable_subgraph = {}
    for char in graph:
        if len(changable.changable(char)) > 1:
            for chan in changable.changable(char)[1:]:
                changable_subgraph[(char, chan)] = Counter({})
                changable_subgraph[(char, chan)][chan] += 1
                graph[char][(char, chan)] += 1
    for key,val in changable_subgraph.items():
        graph[key] = val
    

makeChangableNode(all_words_graph)


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
        return f'({self.curr_char}), {self.w}/{self.n}'

    def __repr__(self):
        return f'({self.curr_char}), {self.w}/{self.n}'


# stack = []
# def simulate(root, stack):
#     ptr = root
#     stack.append(ptr)
#     while ptr.nextChar():
#         if ptr.isComplete():
#             ptr = ptr.select()
#         else:
#             ptr = ptr.expand()
#         stack.append(ptr)
# def backpropagate(stack):
#     alternater = True
#     while stack:
#         node = stack.pop()
#         node.n += 1
#         if alternater:
#             node.w += 1

#         alternater = not alternater

# def learn(root, stack,num = 50):
#     for i in range(num):
#         print(f'{i}회')
#         simulate(root, stack)
#         backpropagate(stack)
#     with open("learn_record/1.p", 'wb') as f:
#         pickle.dump(root, f)
#     print(max(root.children, key = lambda x : root.children[x].w))

# learn(Node(None, "족"), stack, 200)
# with open("learn_record/1.p", 'rb') as f:
#     root = pickle.load(f)
# print(root.children)
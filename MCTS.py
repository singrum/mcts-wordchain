
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
                if not chan in graph:
                    continue
                changable_subgraph[(char, chan)] = Counter({})
                changable_subgraph[(char, chan)][chan] += 1
                graph[char][(char, chan)] += 1
    for key,val in changable_subgraph.items():
        graph[key] = val

def showDict(d):
    char = d.keys()
    for c in char:
        print(c, ' : ', d[c])



makeChangableNode(all_words_graph)
# 두음 노드는 써도 사라지지 않음

class Node:
    def __init__(self, curr_char, parent = None, graph = all_words_graph):
        self.n, self.w = 0, 0
        self.parent = parent
        self.curr_char = curr_char
        self.graph = graph
        self.next_char = self.graph[self.curr_char]
        self.children = {}

    def select(self):
        children = self.children.values()
        selectedChild = max(children, key = lambda x : x.UTC())
        return selectedChild
    
    def UTC(self):
        return self.w / self.n + math.sqrt(2 * math.log(self.parent.n) / self.n)
    
    
    def expand(self):
        for char in self.next_char:
            if char not in self.children:
                graph_copy = copy(self.graph)
                if not (type(self.curr_char) == tuple or type(char) == tuple):
                    graph_copy[self.curr_char][char] -= 1
                    if graph_copy[self.curr_char][char] == 0:
                        graph_copy[self.curr_char].pop(char)
                child = Node(char, self, graph_copy)
                self.children[char] = child
                return child
        
    def isEnd(self):
        return False if self.next_char else True
    
    def isComplete(self):
        return len(self.children) == len(self.next_char)

    def loseProb(self):
        return self.w/self.n

    def winProb(self):
        return 1 - self.w/self.n

    def __str__(self):
        return f'({self.curr_char}, {self.w}/{self.n}, {round(self.w/self.n, 2)})'

    def __repr__(self):
        return f'({self.curr_char}, {self.w}/{self.n}, {round(self.w/self.n, 2)})'



def simulate(node, stack, expand = True):
    ptr = node
    stack.append(ptr)
    if expand:
        while True:
            if ptr.isComplete():
                ptr = ptr.select()
            else:
                ptr = ptr.expand()
            stack.append(ptr)
            if not ptr.next_char:
                break
        
    else:
        while True:
            ptr = ptr.select()
            stack.append(ptr)
            if not ptr.next_char:
                break

def backpropagate(stack):
    alternater = True
    while stack:
        node = stack.pop()
        node.n += 1
        if alternater:
            node.w += 1

        alternater = not alternater

def learn(node, expand = 50, select =0): # expand : 200회 넘어가면 killed
    stack = []
    for i in range(expand):
        if (i+1) % 100 == 0:
            print(f'...expand {i+1}회')
        simulate(node, stack)
        backpropagate(stack)
    for i in range(select):
        if (i+1) % 100 == 0:
            print(f'...select {i+1}회')
        simulate(node, stack, expand = False)
        backpropagate(stack)

    

def recommendNextChar(node):
    return max(node.children, key = lambda x : node.children[x].w / node.children[x].n)
    

def game():
    root = Node(input("start : "))
    node = root
    learn(node, 100,0)
    print("승률 : ", node.winProb())
    [print(child) for child in node.children.values()]
    print("recommend : ", recommendNextChar(node))
    while True:
        print()
        input_char = input("input : ")
        if input_char == "r":
            input_char = recommendNextChar(node)
        node = node.children[input_char]
        learn(node, 50,0)
        print("승률 : ", node.winProb())
        [print(child) for child in node.children.values()]
        print("recommend : ", recommendNextChar(node))
        
game()

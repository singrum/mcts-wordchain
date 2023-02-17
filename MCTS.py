# Node에 다음에 올 음절들, 히스토리만 저장




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

nodesMemory = []
class Node:

    def __init__(self, curr_char, history, parent = None): 
        self.n, self.w = 0, 0
        self.parent = parent
        self.curr_char = curr_char
        self.history = history # history에 두음 엣지는 없음
        self.next_char = all_words_graph[self.curr_char].copy()
        if self.curr_char in self.history:
            self.next_char -= self.history[self.curr_char]
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
                child = self.makeChild(char)
                self.children[char] = child
                return child

    def makeChild(self, char):
        history_copy = copy(self.history)
        if not (type(self.curr_char) == tuple or type(char) == tuple):
            if self.curr_char not in history_copy:
                history_copy[self.curr_char] = Counter({})
            history_copy[self.curr_char][char] += 1

        child = Node(char, history = history_copy, parent = self)
        nodesMemory.append(child)
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
        return f'({self.curr_char}, {self.w}/{self.n}, {round(self.w/self.n, 3)})'

    def __repr__(self):
        return f'({self.curr_char}, {self.w}/{self.n}, {round(self.w/self.n, 3)})'



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

def learn(node, expand = 50): # expand : 200회 넘어가면 killed
    
    stack = []
    print(f'...learning start ({expand} times)')
    j = 1
    for i in range(expand):
        if (i+1) == expand * j// 10:
            print(f'...learning {j}0%')
            j += 1
        simulate(node, stack)
        backpropagate(stack)


    

def recommendNextChar(node):
    return max(node.children, key = lambda x : node.children[x].w / node.children[x].n)
    

def game(firstLearningNum, restLearningNum):
    i = 0
    # 처음 음절 제시
    while 1:
        input_char = input(f"input[{i}] : ")
        if input_char in all_words_graph:
            break
    root = Node(input_char, history = {})
    node = root
    learn(node, firstLearningNum)
    print("승률 : ", node.winProb())
    [print(child) for child in sorted(node.children.values(), key = lambda x : x.w/x.n, reverse=True)]
    print("recommend : ", recommendNextChar(node))
    

    #그담부터
    while True:
        i += 1
        print()
        while 1:
            input_char = input(f"input[{i}] : ")
            if input_char in all_words_graph or input_char == "r":
                break
            
        if input_char == "r":
            input_char = recommendNextChar(node)
        if input_char not in node.children:
            print("Game End")
            break
        node = node.children[input_char]
        learn(node, restLearningNum)
        print("승률 : ", node.winProb())
        [print(child) for child in sorted(node.children.values(), key = lambda x : x.w/x.n, reverse=True)]
        print("recommend : ", recommendNextChar(node))
        



def wordsToHistory(*words):
    history = {}
    for word in words:
        if word[0] not in history:
            history[word[0]] = Counter({})
        history[word[0]][word[-1]] += 1
    return history

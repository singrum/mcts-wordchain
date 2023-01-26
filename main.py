from MCTS import *


node = Node("즉", wordsToHistory('축융', '융즉'))
learn(node, 4000)
[print(child) for child in sorted(node.children.values(), key = lambda x : x.w/x.n, reverse=True)]
print(recommendNextChar(node))

from collections import Counter
import wordchain as wc
import various_rules as vr
import sys
import numpy as np
import gc
import json
import pickle



with open('json/cir_words_dict.json', 'r') as f:
    dic = json.load(f)


wm = wc.WordManager(vr.Kor())
# with open('json/word_class.json', 'w') as f:
#     json.dump({"cir" : sorted(list(wm.cir_index)), "win" : sorted(list(wm.win_index)), "los" : sorted(list(wm.los_index))}, f)

with open('json/word_class.json', 'r') as f:
    print(json.load(f))
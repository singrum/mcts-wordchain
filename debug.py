from collections import Counter
import wordchain as wc
import various_rules as vr
import sys
import numpy as np
import gc
import json
import pickle



wm = wc.WordManager(vr.Kor())

with open("json/char_class.json", "w") as f:
    json.dump(wm.index_class, f)
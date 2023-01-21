# -*- coding: utf-8 -*-

from collections import defaultdict
from abc import ABC, abstractmethod

class WordRule(ABC):

    def __init__(self):
        self.word_list = self.get_data()
        self.word_dict = self.set_dict()

    @abstractmethod
    def head(self, word):
        return word[0]
    
    @abstractmethod
    def tail(self, word):
        return word[-1]
    
    @abstractmethod
    def changable(self, index):
        return index

    @abstractmethod
    def get_data(self):
        return

    def set_dict(self):
        result = defaultdict(set)
        for word in self.word_list:
            result[self.head(word)].add(word)
            result[self.tail(word)]
        return result

# class Turn:

#     trail = []

#     def __init__(self, rule, curr, history):
#         self.rule = rule
#         self.curr = curr
#         self.history = history

#     def next_words(self):
#         result = set()
#         for c_index in self.rule.changable(self.curr):
#             result.update(self.rule.word_dict[c_index])
#         return result - self.history

#     def make_move(self, word):
#         Turn.trail.append(word)
#         return Turn(self.rule, self.rule.tail(word), self.history | {word})
    
#     def is_win(self, trail = None):
#         if not trail:
#             trail = []
#         if not self.next_words() and len(trail) % 2 == 1:
#             print(trail)
#         for word in self.next_words():
#             next_turn = self.make_move(word)
#             if not next_turn.is_win(trail + [word]):
#                 return word
#         return False            


class IndexManager:

    def __init__(self, rule):
        self.rule = rule
        self.win_index = set()
        self.los_index = set()
        self.cir_index = set()
        self.set_index(self.rule.word_list)
        self.win_word_dict = {}

    def next_words(self, index):
        result = set()
        for c_index in self.rule.changable(index):
            result.update(self.rule.word_dict[c_index])
        return result

    def set_index(self, words):
        self.cir_index = set(self.rule.word_dict.keys())

    def __is_los_index(self, index):
        for word in self.next_words(index):
            if self.rule.tail(word) not in self.win_index:
                return False
        return True

    def __is_win_index(self, index):
        for word in self.next_words(index):
            if self.rule.tail(word) in self.los_index:
                self.win_word_dict[index] = word
                return True 

    def classify_index(self):
        i = 0
        updated_index = set()
        is_updated = True
        while is_updated == True:

            i += 1
            is_updated = False

            for index in self.cir_index:
                if index in updated_index:
                    continue

                if self.__is_los_index(index):
                    self.los_index.add(index)
                    is_updated = True
                    updated_index.add(index)
                    continue

                if self.__is_win_index(index):
                    self.win_index.add(index)
                    is_updated = True
                    updated_index.add(index)

            self.cir_index -= updated_index

        return updated_index

    def show_index_cls(self):
        print("패배음절 : ", ', '.join(sorted(list(self.los_index))))
        print("승리음절 : ", ', '.join(sorted(list(self.win_index))))
        print("순환음절 : ", ', '.join(sorted(list(self.cir_index))))


class WordManager(IndexManager):

    def __init__(self, rule):
        super().__init__(rule)
        self.classify_index()

    def next_win_word(self, index):
        return self.win_word_dict[index]

    def next_cir_word(self, index): # win word 하나만 반환
        return {word for word in self.next_words(index) if self.rule.tail(word) in self.cir_index}
    
    def make_cir_dict(self):
        result = {}
        for index in self.cir_index:
            result[index] = self.next_cir_word(index)
        return result

    def cir_word_num(self):
        result = 0 
        for index in self.cir_index:
            result += len(self.next_cir_word(index))
        return result

    def next_win_words(self, index): #모든 win words 집합 반환
        return {word for word in self.next_words(index) if self.rule.tail(word) in self.los_index}

    def next_word_auto(self, index):
        if index in self.cir_index:
            return self.next_cir_word(index)
        if index in self.win_index:
            return self.next_win_word
        return None

    def show_cir_dict(self):
        return "\n".join([index + " : " +  ', '.join(sorted(list(self.next_cir_word(index)))) for index in sorted(list(self.cir_index))])
    
    def show_win_dict(self):
        return "\n".join([index + ' : ' + ', '.join(sorted(list(self.next_win_words(index)))) for index in sorted(list(self.win_index))])

    def make_cir_dict2(self):
        cir_head_dict = self.make_cir_dict()
        cir_tail_dict = defaultdict(set)

        for index in cir_head_dict:
            for word in cir_head_dict[index]:
                cir_tail_dict[self.rule.tail(word)].add(word)
        return (cir_head_dict, cir_tail_dict)
    
    def make_degree_dict(self):
        cir_head_dict, cir_tail_dict = self.make_cir_dict2()
        degree_dict = {}
        for index in self.cir_index:
            degree_dict[index] = len(cir_head_dict[index]) + len(cir_tail_dict[index])
        return degree_dict

    def max_cir_word(self):
        degree_dict = self.make_degree_dict()
        max_cir_word = max(self.cir_index, key = lambda x : degree_dict[x])
        return max_cir_word, degree_dict[max_cir_word]

    def sort_cir_word(self):
        degree_dict = self.make_degree_dict()
        result = sorted(list(self.cir_index), key = lambda x : degree_dict[x], reverse=1)
        for i in range(5):
            print(result[i], degree_dict[result[i]])
        


    def show_representative_val(self):
        return f"단어수 : {len(self.rule.word_list)}\n음절수 : {len(self.win_index) + len(self.los_index) + len(self.cir_index)}\n승리음절수 : {len(self.win_index)}\n패배음절수 : {len(self.los_index)}\n순환음절수 : {len(self.cir_index)}\n평균순환단어수 : {round(self.cir_word_num()/len(self.cir_index),2)}\n최대순환음절 : {self.max_cir_word()[0]}({self.max_cir_word()[1]})"

class TrailManager(WordManager):

    def show_los_trail(self, index, curr = None):
        if not curr:
            curr = []

        if not self.next_words(index):
            print('-'.join(curr))

        for los in self.next_words(index):
            curr_ = curr.copy()
            curr_.append(los)
            win = self.next_win_word(self.rule.tail(los))
            curr_.append(win)
            self.show_los_trail(self.rule.tail(win), curr_)

    def show_win_trail(self, index, curr = None):
        if not curr:
            curr = [self.next_win_word(index)]
        self.show_los_trail(self.rule.tail(self.next_win_word(index)), curr)
    
    def show_trail_auto(self, index):
        if index in self.win_index:
            self.show_win_trail(index)
        if index in self.los_index:
            self.show_los_trail(index)
        return None
                
class RuleTheory(WordManager):
    
    def __init__(self, rule):
        super().__init__(rule)
    
    def make_index_cluster(self, index):
        cluster = {index}
        curr = index
        is_updated = True
        updated_index = {index}
        while is_updated:
            is_updated = False
            for curr in updated_index.copy():
                for word in self.next_cir_word(curr):
                    if self.rule.tail(word) not in cluster:
                        cluster.add(self.rule.tail(word))
                        is_updated = True
                        updated_index.add(self.rule.tail(word))
                updated_index.discard(curr)
        return cluster
    
    def everage_cir_num(self):
        sum = 0
        # count = 0
        for cir in self.cir_index:
            sum += len(self.make_index_cluster(cir))
            # count += 1
            # print(count, "/", len(self.cir_index))
        return sum / len(self.cir_index)
    
    def adj_mat(self):
        cir_list = list(self.cir_index)
        mat = [[0] * len(self.cir_index) for _ in range(len(self.cir_index))]
        for i in range(len(cir_list)):
            for j in range(len(cir_list)):
                for word in self.next_cir_word(cir_list[i]):
                    if self.rule.tail(word) == cir_list[j]:
                        mat[i][j] = 1
        for i in mat:
            for j in i:
                print(j, end = " ")
            print()
        return mat
    




# class GameTurn(WordManager):

#     def __init__(self, rule, curr):
#         super().__init__(rule)
#         self.curr = curr
#         self.depth = 0
#         self.trail = []

#     def move(self, word):
#         self.rule.word_dict[self.rule.head(word)].remove(word)
#         self.curr = self.rule.tail(word)
#         self.depth += 1
#         self.trail.append(word)
        
#     def unmove(self, word):
#         self.rule.word_dict[self.rule.head(word)].add(word)
#         self.curr = self.rule.head(word)
#         self.depth -= 1
#         self.trail.pop()

#     def unclassify_index(self, updated_index):
#         self.cir_index |= updated_index
#         self.win_index -= updated_index
#         self.los_index -= updated_index

#     def is_win(self):
#         if self.depth >= 30:
#             return False
#         if self.curr in self.win_index:
#             return self.next_win_word(self.curr)
#         if self.curr in self.los_index:
#             return False

#         if len(self.next_cir_word(self.curr)) == 1:
#             to_update = True
#         else:
#             to_update = False
            
#         for word in self.next_cir_word(self.curr):
#             self.move(word)
#             if to_update:
#                 updated_index = self.classify_index()
#             if not self.is_win():
#                 print(self.trail)
#                 self.unmove(word)
#                 if to_update:
#                     self.unclassify_index(updated_index)
#                 return word
#             else:
#                 self.unmove(word)
#                 if to_update:
#                     self.unclassify_index(updated_index)
#         return False



#!/usr/bin/env python
# encoding: utf-8

from random import choice
import vocab
from vocab import NounType, AdjType
from words import *
from utils import *

class Time:
	Pres, Past, Fut = 'Pres', 'Past', 'Fut'
	Times = [Pres, Past, Fut]

class Context(object):
	def __init__(self):
		self._time = Time.Pres

	def make_noun_phrase(self, case, noun_type, has_adj=-1, compound_nums=-1):
		if compound_nums == -1:
			compound_nums = weighted_choice([85,15,5]) + 1
		result, number = self._make_simple_noun_phrase(case, noun_type, has_adj=has_adj)
		for i in range(compound_nums-1):
			new_simple_noun_phrase, _ = self._make_simple_noun_phrase(case, noun_type, adj_nums=1, for_conjunct=1)
			result = result + ' ' + new_simple_noun_phrase
		return result, (number if compound_nums == 1 else Number.Pl)

	def _make_simple_noun_phrase(self, case, noun_type, has_adj=-1, adj_nums=-1, for_conjunct=0):
		noun_vocab_list = vocab.NOUNS[noun_type]
		if noun_type != NounType.Geographic and noun_type != NounType.Proper:
			number = choice(Number.Numbers)
		else:
			number = Number.Sg

		word_entry = choice(noun_vocab_list)
		word = word_entry.inflect(case, number)

		if has_adj == -1:
			has_adj = weighted_choice([60,30,10])

		if has_adj == 0:
			return (word if for_conjunct == 0 else conjunct(word)), number
		else:
			if adj_nums == -1:
				adj_nums = weighted_choice([75,25])+1
			adj_type = AdjType.get_adj_types(noun_type)
			adj_vocab_list = vocab.ADJS[choice(adj_type)]
			epithet = [choice(adj_vocab_list).inflect(case, number, word_entry.sex()) for i in (0,1)]
			while epithet[1] == epithet[0]:
				epithet[1] = choice(adj_vocab_list).inflect(case, number, word_entry.sex())
			if has_adj == 1:
				return (word if for_conjunct == 0 else conjunct(word)) + ' ' +\
						epithet[0] + ('' if adj_nums == 1 else ' ' + conjunct(epithet[1])), number
			else:
				return (epithet[0] if for_conjunct ==0 else conjunct(epithet[0])) +\
						('' if adj_nums == 1 else ' ' + conjunct(epithet[1])) + ' ' + word, number

# test code
def t():
	myc = Context()
	subj, subj_num = myc.make_noun_phrase(Case.Nom, NounType.Personal)
	obj, obj_num = myc.make_noun_phrase(Case.Acc, NounType.Personal)
	print subj + ' ' + obj + ' ' + ('perdidit' if subj_num == Number.Sg else 'perdiderunt')

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

	def gen_noun_phrase(self, case, noun_type):
		noun_vocab_list = vocab.NOUNS[noun_type]
		number = choice(Number.Numbers)
		word_entry = choice(noun_vocab_list)
		word = word_entry.inflect(case, number)
		has_adj = weighted_choice([50,25,25])
		if has_adj == 0:
			return word
		else:
			adj_type = AdjType.get_adj_types(noun_type)
			adj_vocab_list = vocab.ADJS[choice(adj_type)]
			epithet = choice(adj_vocab_list).inflect(case, number, word_entry.sex())
			if has_adj == 1:
				return word + ' ' + epithet
			else:
				return epithet + ' ' + word

# test code
def t():
	myc = Context()
	print myc.gen_noun_phrase(Case.Dat, NounType.Personal)

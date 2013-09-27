#!/usr/bin/env python
# encoding: utf-8

from random import random, choice

def weighted_choice(weights):
	rnd = random() * sum(weights)
	for i, w in enumerate(weights):
		rnd -= w
		if rnd < 0:
			return i

def conjunct(word):
	return choice(['et ' + word, word + 'que', 'ac ' + word, 'atque ' + word])

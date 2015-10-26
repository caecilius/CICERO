#!/usr/bin/env python
# encoding: utf-8

import reference
from inflection import *

class Decl(object):
	D1, D2, D3, D3i, D4, D5 = 1, 2, 3, 6, 4, 5

class DeclAdj(object):
	D12, D3a, D3b = 1, 2, 3

class Noun(object):
	def __init__(self, nom, stem, decl, sex):
            self._nom = nom
            self._stem = stem
            self._decl = decl
            self._sex = sex

        def nom(self):
            return self._nom

	def sex(self):
            return self._sex

	def inflect(self, case, number):
		if case == Case.Acc and self._sex == Sex.N:
			case = Case.Nom
		if number == Number.Sg and case == Case.Nom:
			return self._nom
		elif case == Case.Voc:
			if self._decl == Decl.D2 and self._sex == Sex.M:
				if self._nom.endswith('ius'):
					return self._stem + 'ī'
				elif self._nom.endswith('us'):
					return self._stem + 'e'
				else:
					return self._nom
			else:
				return self._nom
		elif self._nom == 'vīs' and number == Number.Sg: 	# irregular
			return {
					Case.Gen : 'virium',
					Case.Dat : 'viribus',
					Case.Acc : 'vim',
					Case.Abl : 'vī'
					}[case]
		elif self._decl == Decl.D1:
			return self._stem + reference.NOUN_ENDINGS[1][number][case]
		elif self._decl == Decl.D2:
			return self._stem + reference.NOUN_ENDINGS[2][self._sex][number][case]
		elif self._decl == Decl.D3:
			return self._stem + reference.NOUN_ENDINGS[3][self._sex][number][case]
		elif self._decl == Decl.D3i:
			if number == Number.Pl and case == Case.Gen:
				return self._stem + 'ium'
			elif self._sex == Sex.N and number == Number.Sg and case == Case.Abl:
				return self._stem + 'ī'
			elif self._sex == Sex.N and number == Number.Pl and case == Case.Nom:
				return self._stem + 'ia'
			else:
				return self._stem + reference.NOUN_ENDINGS[3][self._sex][number][case]
		elif self._decl == Decl.D4:
			return self._stem + reference.NOUN_ENDINGS[4][self._sex][number][case]
		elif self._decl == Decl.D5:
			return self._stem + reference.NOUN_ENDINGS[5][number][case]

class Adjective(object):
	def __init__(self, nom, stem, decl):
		self._nom = nom
		self._stem = stem
		self._decl = decl

	def inflect(self, case, number, sex):
		if self._decl == DeclAdj.D12:
			if sex == Sex.M:
				fake_noun = Noun(self._nom, self._stem, Decl.D2, Sex.M)
			elif sex == Sex.F:
				fake_noun = Noun(self._stem + 'a', self._stem, Decl.D1, Sex.F)
			elif sex == Sex.N:
				fake_noun = Noun(self._stem + 'um', self._stem, Decl.D2, Sex.N)
		elif self._decl == DeclAdj.D3a:
			if sex == Sex.M:
				fake_noun = Noun(self._nom, self._stem, Decl.D3i, Sex.M)
			elif sex == Sex.F:
				fake_noun = Noun(self._stem + 'is', self._stem, Decl.D3i, Sex.F)
			elif sex == Sex.N:
				fake_noun = Noun(self._stem + 'e', self._stem, Decl.D3i, Sex.N)
		elif self._decl == DeclAdj.D3b:
			fake_noun = Noun(self._nom, self._stem, Decl.D3i, sex)
		return fake_noun.inflect(case, number)

class Verb(object):
	def __init__(self, pres, pres_stem, perf_stem, part_stem, conj, perf_def=0, dep=0, case=Case.Acc):
		self._pres = pres
		self._pres_stem = pres_stem
		self._perf_stem = perf_stem
		self._part_stem = part_stem
		self._conj = conj
		self._perf_def = perf_def
		self._dep = dep
		self._case = case

	def conjugate(self, person, number, tense, voice, mood):
		pass

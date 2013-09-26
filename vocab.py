#!/usr/bin/env python
# encoding: utf-8

from words import *

class NounType:
	Personal, Thing, Abstract, Geographic, Proper = 'Personal', 'Thing', 'Abstract', 'Geographic', 'Proper'
	NounTypes = [Personal, Thing, Geographic, Proper]

class AdjType:
	Common, Personal, Tangible = 'Common', 'Personal', 'Tangible'
	AdjTypes = [Common, Personal, Tangible]

	@staticmethod
	def get_adj_types(noun_type):
		if noun_type == NounType.Personal or noun_type == NounType.Proper:
			return [AdjType.Common, AdjType.Personal, AdjType.Tangible]
		elif noun_type != NounType.Abstract:
			return [AdjType.Common, AdjType.Tangible]
		else:
			return [AdjType.Common]


PERSONAL_NOUNS = [
		Noun('agricola', 'agricol', Decl.D1, Sex.M),
		Noun('dea', 'de', Decl.D1, Sex.F),
		Noun('fīlia', 'fīli', Decl.D1, Sex.F),
		Noun('nauta', 'naut', Decl.D1, Sex.M),
		Noun('poēta', 'poēt', Decl.D1, Sex.M),
		Noun('rēgīna', 'rēgīn', Decl.D1, Sex.F),

		Noun('fīlius', 'fīli', Decl.D2, Sex.M),
		Noun('bellum', 'bell', Decl.D2, Sex.N),
		]

THING_NOUNS = [
		Noun('īnsula', 'īnsul', Decl.D1, Sex.F),
		Noun('pecūnia', 'pecūni', Decl.D1, Sex.F),
		Noun('viā', 'vi', Decl.D1, Sex.F),
		]

ABSTRACT_NOUNS = [
		Noun('anima', 'anim', Decl.D1, Sex.F),
		Noun('fāma', 'fām', Decl.D1, Sex.F),
		]

GEOGRAPHIC_NOUNS = [
		Noun('Italia', 'Itali', Decl.D1, Sex.F),
		Noun('Gallia', 'Galli', Decl.D1, Sex.F),
		]

PROPER_NOUNS = [
		Noun('Catilina', 'Catilin', Decl.D1, Sex.M),
		Noun('Iūlia', 'Iūli', Decl.D1, Sex.F),
		]

NOUNS = {
		NounType.Personal : PERSONAL_NOUNS,
		NounType.Thing : THING_NOUNS,
		NounType.Abstract : ABSTRACT_NOUNS,
		NounType.Geographic : GEOGRAPHIC_NOUNS,
		NounType.Proper : PROPER_NOUNS,
		}

PERSONAL_ADJS = [
		Adjective('laetus', 'laet', DeclAdj.D12),
		]

TANGIBLE_ADJS = [
		Adjective('ūmidus', 'ūmid', DeclAdj.D12),
		]

COMMON_ADJS = [
		Adjective('magnus', 'magn', DeclAdj.D12),
		Adjective('paulus', 'paul', DeclAdj.D12),
		]

ADJS = {
		AdjType.Common : COMMON_ADJS,
		AdjType.Personal : PERSONAL_ADJS,
		AdjType.Tangible : TANGIBLE_ADJS,
		}

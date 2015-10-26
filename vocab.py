#!/usr/bin/env python
# encoding: utf-8

from words import *

class NounType:
	Personal, Thing, Abstract, Geographic, Proper = 'Personal', 'Thing', 'Abstract', 'Geographic', 'Proper'
	NounTypes = [Personal, Thing, Geographic, Proper]

class AdjType:
	Common, Personal, Tangible, Impersonal = 'Common', 'Personal', 'Tangible', 'Impersonal'
	AdjTypes = [Common, Personal, Tangible, Impersonal]

	@staticmethod
	def get_adj_types(noun_type):
		if noun_type == NounType.Personal or noun_type == NounType.Proper:
			return [AdjType.Common, AdjType.Personal, AdjType.Tangible]
		elif noun_type != NounType.Abstract:
			return [AdjType.Common, AdjType.Tangible, AdjType.Impersonal]
		else:
			return [AdjType.Common]


PERSONAL_NOUNS = [
		Noun('agricola', 'agricol', Decl.D1, Sex.M),
		Noun('dea', 'de', Decl.D1, Sex.F),
		Noun('fīlia', 'fīli', Decl.D1, Sex.F),
		Noun('nauta', 'naut', Decl.D1, Sex.M),
		Noun('poēta', 'poēt', Decl.D1, Sex.M),
		Noun('rēgīna', 'rēgīn', Decl.D1, Sex.F),

		Noun('vir', 'vir', Decl.D2, Sex.M),
		Noun('bellum', 'bell', Decl.D2, Sex.N),
                Noun('deus', 'de', Decl.D2, Sex.M),

		Noun('frāter', 'frātr', Decl.D3, Sex.M),
		Noun('soror', 'soror', Decl.D3, Sex.F),
                Noun('homō', 'homin', Decl.D3, Sex.M),
                Noun('rēx', 'rēg', Decl.D3, Sex.M),
		]

THING_NOUNS = [
		Noun('īnsula', 'īnsul', Decl.D1, Sex.F),
		Noun('pecūnia', 'pecūni', Decl.D1, Sex.F),
		Noun('viā', 'vi', Decl.D1, Sex.F),
                Noun('terra', 'terr', Decl.D1, Sex.F),

		Noun('līber', 'lībr', Decl.D2, Sex.M),

		Noun('animal', 'animal', Decl.D3, Sex.N),
		Noun('corpus', 'corpor', Decl.D3, Sex.N),
                Noun('urbs', 'urb', Decl.D3, Sex.F),

                Noun('manus', 'man', Decl.D4, Sex.F),
		]

ABSTRACT_NOUNS = [
		Noun('anima', 'anim', Decl.D1, Sex.F),
		Noun('fāma', 'fām', Decl.D1, Sex.F),
                Noun('vīta', 'vīt', Decl.D1, Sex.F),
                Noun('causa', 'caus', Decl.D1, Sex.F),

                Noun('animus', 'anim', Decl.D2, Sex.M),

                Noun('pars', 'part', Decl.D3, Sex.F),
                Noun('tempus', 'tempor', Decl.D3, Sex.N),
                Noun('mors', 'mort', Decl.D3, Sex.F),
                Noun('vīs', 'vir', Decl.D3, Sex.F),

		Noun('senātus', 'senāt', Decl.D4, Sex.M),

		Noun('diēs', 'di', Decl.D5, Sex.F),
		Noun('rēs', 'r', Decl.D5, Sex.F),
		]

GEOGRAPHIC_NOUNS = [
		Noun('Italia', 'Itali', Decl.D1, Sex.F),
		Noun('Gallia', 'Galli', Decl.D1, Sex.F),
		Noun('Rōma', 'Rōm', Decl.D1, Sex.F),

		Noun('Carthāgo', 'Carthāgin', Decl.D3, Sex.F),
		]

PROPER_NOUNS = [
		Noun('Catilina', 'Catilin', Decl.D1, Sex.M),
		Noun('Iūlia', 'Iūli', Decl.D1, Sex.F),
                Noun('Sulla', 'Sull', Decl.D1, Sex.M),

		Noun('Mārcus', 'Mārc', Decl.D2, Sex.M),
		Noun('Quintus', 'Quint', Decl.D2, Sex.M),

		Noun('Caesar', 'Caesar', Decl.D3, Sex.M),
		Noun('Cicerō', 'Cicerōn', Decl.D3, Sex.M),
		Noun('Dīdō', 'Dīdōn', Decl.D3, Sex.F),
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
		Adjective('cārus', 'cār', DeclAdj.D12),
		Adjective('miser', 'miser', DeclAdj.D12),
                Adjective('saevus', 'saev', DeclAdj.D12),
                Adjective('fortis', 'fort', DeclAdj.D3b),
                Adjective('dīgnus', 'dīgn', DeclAdj.D12),
                Adjective('fēlix', 'fēlic', DeclAdj.D3b),
		]

TANGIBLE_ADJS = [
		Adjective('altus', 'alt', DeclAdj.D12),
		Adjective('ūmidus', 'ūmid', DeclAdj.D12),
                Adjective('gravis', 'grav', DeclAdj.D3b),
                Adjective('longus', 'long', DeclAdj.D12),
                Adjective('levis', 'lev', DeclAdj.D3b),
		]

IMPERSONAL_ADJS = [
		Adjective('acidus', 'acid', DeclAdj.D12),
                Adjective('ferus', 'fer', DeclAdj.D12),
                Adjective('dīrus', 'dīr', DeclAdj.D12),
                Adjective('hūmānus', 'hūmān', DeclAdj.D12),
		]

COMMON_ADJS = [
		Adjective('magnus', 'magn', DeclAdj.D12),
		Adjective('paulus', 'paul', DeclAdj.D12),
                Adjective('omnis', 'omn', DeclAdj.D3b),
                Adjective('multus', 'mult', DeclAdj.D12),
                Adjective('bonus', 'bon', DeclAdj.D12),
                Adjective('prīmus', 'prīm', DeclAdj.D12),
                Adjective('tantus', 'tant', DeclAdj.D12),
                Adjective('novus', 'nov', DeclAdj.D12),
                Adjective('parvus', 'parv', DeclAdj.D12),
                Adjective('cūnctus', 'cūnct', DeclAdj.D12),
                Adjective('vetus', 'veter', DeclAdj.D3b),
		]

ADJS = {
		AdjType.Common : COMMON_ADJS,
		AdjType.Personal : PERSONAL_ADJS,
		AdjType.Tangible : TANGIBLE_ADJS,
		}

#!/usr/bin/env python
# encoding: utf-8

from inflection import *

NOUN_ENDINGS = {
		1 : {
			Number.Sg : {
				Case.Gen : 'ae',
				Case.Dat : 'ae',
				Case.Acc : 'am',
				Case.Abl : 'ā',
				},
			Number.Pl : {
				Case.Nom : 'ae',
				Case.Gen : 'ārum',
				Case.Dat : 'īs',
				Case.Acc : 'ās',
				Case.Abl : 'īs',
				},
			},
		2 : {
			Sex.M : {
				Number.Sg : {
					Case.Gen : 'ī',
					Case.Dat : 'ō',
					Case.Acc : 'um',
					Case.Abl : 'ō',
					},
				Number.Pl : {
					Case.Nom : 'ī',
					Case.Gen : 'ōrum',
					Case.Dat : 'īs',
					Case.Acc : 'ōs',
					Case.Abl : 'īs',
					},
				},
			Sex.N : {
				Number.Sg : {
					Case.Gen : 'ī',
					Case.Dat : 'ō',
					Case.Abl : 'ō',
					},
				Number.Pl : {
					Case.Nom : 'a',
					Case.Gen : 'ōrum',
					Case.Dat : 'īs',
					Case.Abl : 'īs',
					}
				},
			},
		3: {
			Sex.M : {
				Number.Sg : {
					Case.Gen : 'is',
					Case.Dat : 'ī',
					Case.Acc : 'em',
					Case.Abl : 'e',
					},
				Number.Pl : {
					Case.Nom : 'ēs',
					Case.Gen : 'um',
					Case.Dat : 'ibus',
					Case.Acc : 'ēs',
					Case.Abl : 'ibus',
					},
				},
			Sex.F : {
				Number.Sg : {
					Case.Gen : 'is',
					Case.Dat : 'ī',
					Case.Acc : 'em',
					Case.Abl : 'e',
					},
				Number.Pl : {
					Case.Nom : 'ēs',
					Case.Gen : 'um',
					Case.Dat : 'ibus',
					Case.Acc : 'ēs',
					Case.Abl : 'ibus',
					},
				},
			Sex.N : {
				Number.Sg : {
					Case.Gen : 'is',
					Case.Dat : 'ī',
					Case.Abl : 'e',
					},
				Number.Pl : {
					Case.Nom : 'a',
					Case.Gen : 'um',
					Case.Dat : 'ibus',
					Case.Abl : 'ibus',
					},
				},
			},
		4: {
			Sex.M : {
				Number.Sg : {
					Case.Gen : 'ūs',
					Case.Dat : 'uī',
					Case.Acc : 'um',
					Case.Abl : 'ū',
					},
				Number.Pl : {
					Case.Nom : 'ūs',
					Case.Gen : 'uum',
					Case.Dat : 'ibus',
					Case.Acc : 'ūs',
					Case.Abl : 'ibus',
					},
				},
			Sex.F : {
				Number.Sg : {
					Case.Gen : 'ūs',
					Case.Dat : 'uī',
					Case.Acc : 'um',
					Case.Abl : 'ū',
					},
				Number.Pl : {
					Case.Nom : 'ūs',
					Case.Gen : 'uum',
					Case.Dat : 'ibus',
					Case.Acc : 'ūs',
					Case.Abl : 'ibus',
					},
				},
			Sex.N : {
				Number.Sg : {
					Case.Gen : 'ūs',
					Case.Dat : 'uī',
					Case.Abl : 'ū',
					},
				Number.Pl : {
					Case.Nom : 'ua',
					Case.Gen : 'uum',
					Case.Dat : 'ibus',
					Case.Abl : 'ibus',
					},
				},
			},
		5: {
				Number.Sg : {
					Case.Gen : 'ēs',
					Case.Dat : 'eī',
					Case.Acc : 'em',
					Case.Abl : 'ē',
					},
				Number.Pl : {
					Case.Nom : 'ēs',
					Case.Gen : 'erum',
					Case.Dat : 'ebus',
					Case.Acc : 'ēs',
					Case.Abl : 'ebus',
					},
			},
		}

VERB_ENDINGS = {
		# this is going to be hell
		}

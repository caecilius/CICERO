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
					Case.Acc : 'um',
					Case.Abl : 'ō',
					},
				Number.Pl : {
					Case.Nom : 'a',
					Case.Gen : 'ōrum',
					Case.Dat : 'īs',
					Case.Acc : 'ōs',
					Case.Abl : 'īs',
					}
				},
			}
		}

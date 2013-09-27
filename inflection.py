#!/usr/bin/env python
# encoding: utf-8

class Person:
	P1, P2, P3 = 'P1', 'P2', 'P3'
	Persons = [P1, P2, P3]

class Case:
	Nom, Gen, Dat, Acc, Abl, Voc = 'NOM', 'GEN', 'DAT', 'ACC', 'ABL', 'VOC'
	Cases = [Nom, Gen, Dat, Acc, Abl, Voc]

class Sex:
	M, F, N = 'M', 'F', 'N'
	Sexes = [M, F, N]

class Number:
	Sg, Pl = 'Singular', 'Plural'
	Numbers = [Sg, Pl]

class Tense:
	Pres, Impf, Fut, Perf, Plup, Futp = 'Pres', 'Impf', 'Fut', 'Perf', 'Plup', 'Futp'
	Tenses = [Pres, Impf, Fut, Perf, Plup, Futp]

class Mood:
	Indic, Subj, Imp = 'Indic', 'Subj', 'Imp'
	Moods = [Indic, Subj, Imp]

class Voice:
	Act, Pas = 'Act', 'Pas'
	Voices = [Act, Pas]

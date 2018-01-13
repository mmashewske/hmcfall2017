#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pizza.py
#  
#  Copyright 2017 Matthew Mashewske <matthew@matthew-W65-67SJ>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


def main(args):
	#print(sys.stdin.readlines())
	tests = int(sys.stdin.readline())
	for i in range(tests):
		pizzas = int(sys.stdin.readline())
		combos = []
		pizzaDict = {}
		foreignWords = []
		nativeWords = []
		foreignDict = {}
		for b in range(pizzas):
			pizza = sys.stdin.readline()
			foreign = sys.stdin.readline().lower().split()
			native = sys.stdin.readline().lower().split()
			pizzaDict[pizza] = native[1:]+foreign[1:]
			for word in foreign[1:]:
				if word not in foreignWords:
					foreignWords.append(word)
			for word in native[1:]:
				if word not in nativeWords:
					nativeWords.append(word)
		for foreignIng in foreignWords:
			if foreignIng not in foreignDict.keys():
				foreignDict[foreignIng] = []
			for nativeIng in nativeWords:
				good = True
				for pizza in pizzaDict.keys():
					#print(pizzaDict.keys())
					if (foreignIng in pizzaDict[pizza] and nativeIng in pizzaDict[pizza]) or (foreignIng not in pizzaDict[pizza] and nativeIng not in pizzaDict[pizza]):
						pass
					else:
						good = False
				if good:
					foreignDict[foreignIng].append(nativeIng)
		sortedKeys = foreignDict.keys()
		sortedKeys.sort()
		for thing in sortedKeys:
			sortedThings = foreignDict[thing]
			sortedThings.sort()
			for possible in sortedThings:
				print ("("+thing+", "+possible+")")
		foreignDict = {}
		print("")
			
						

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

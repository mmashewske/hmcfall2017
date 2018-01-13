#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  meta.py
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
	inputs = sys.stdin.readlines()
	#print inputs
	knownVars = {} 
	for i in inputs:
		things = i.split()
		if things[0] == "define":
			knownVars[things[2]] = int(things[1])
		else:
			if (things[1] in knownVars.keys() ) and (things[3] in knownVars.keys() ):
				if things[2] == "<":
					print( knownVars[things[1]] < knownVars[things[3]])
				elif things[2] == ">":
					print( knownVars[things[1]] > knownVars[things[3]])
				else:
					print( knownVars[things[1]] == knownVars[things[3]])
			else:
				print("undefined")
			

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

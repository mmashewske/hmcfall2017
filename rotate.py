#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rotate.py
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
	numLines = int(sys.stdin.readline())
	while numLines != 0:
		origShape = []
		width = 0
		for line in range(numLines):
			origShape.append(sys.stdin.readline())
			if len(origShape[line]) > width:
				width = len(origShape[line])
		print(len(origShape))
		for line in origShape:
			if len(line) < width:
				line += " "*(width-len(line))
			print(len(line))
				
		for l in range(width-1):
			newLine = ""
			for line in origShape:
				if line[l] == '|':
					newLine+='-'
				elif line[l] == '-':
					newLine+='|'
				else:	
					newLine+=line[l]
			print(newLine[::-1])
		numLines = int(sys.stdin.readline())

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

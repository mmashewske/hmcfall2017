#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  target.py
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
	numTargets = int(sys.stdin.readline() )
	targets = []
	for target in range(numTargets):
		targets.append(sys.stdin.readline().split())
	shots = int(sys.stdin.readline())
	for i in range(shots):
		hit = 0
		shot = sys.stdin.readline().split()
		for target in targets:
			if target[0] == "circle":
				if math.sqrt( pow( ( int(shot[0])-int(target[1]) ) , 2) + pow( ( int(shot[1]) -int(target[2]) ), 2)  ) <= int(target[3]):
					hit+=1
			else:
				if ( int(shot[0]) <= int(target[3]) and int(shot[0]) >= int(target[1]) ) and (int(shot[1]) <= int(target[4]) and int(shot[1]) >= int(target[2]) ):
					hit+=1
		print(hit)

if __name__ == '__main__':
    import sys
    import math
    sys.exit(main(sys.argv))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dungeon.py
#  
#  Copyright 2018 Matthew Mashewske <matthew@matthew-W65-67SJ>
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
	lrc = sys.stdin.readline()
	while not (lrc == "0 0 0\n"):
		lrcArr = lrc.split()
		ePlace = [-1,-1,-1]
		sPlace = [-1,-1,-1]
		charArr = []
		
		for l in range(int(lrcArr[0])):
			charArr.append([])
			for r in range(int(lrcArr[1])):
				charArr[l].append(sys.stdin.readline())
				if 'E' in charArr[l][r]:
					ePlace = [l,r,charArr[l][r].find('E')]
				if 'S' in charArr[l][r]:
					sPlace = [l,r,charArr[l][r].find('S')]
			sys.stdin.readline()
		valArr = [ [[-1 for a in range(int(lrcArr[2]))] for b in range(int(lrcArr[1]))] for c in range(int(lrcArr[0]))]
		queue = [ePlace]
		found = False
		while not (queue == []):
			current = queue.pop(0)
			if current[2] < (int(lrcArr[2])-1):
				after = charArr[current[0]][current[1]][current[2]+1]
				afterVal = valArr[current[0]][current[1]][current[2]+1]
				currentVal = valArr[current[0]][current[1]][current[2]]
				if after != '#' and (afterVal < currentVal+1 or afterVal == -1):
					if after == 'S':
						print("Escaped in "+str(currentVal+2)+" minute(s).")
						found = True
						break
					else:
						valArr[current[0]][current[1]][current[2]+1] = currentVal+1
						queue.append([current[0],current[1],current[2]+1])
			if current[2] > 0:
				after = charArr[current[0]][current[1]][current[2]-1]
				afterVal = valArr[current[0]][current[1]][current[2]-1]
				currentVal = valArr[current[0]][current[1]][current[2]]
				if after != '#' and (afterVal < currentVal+1 or afterVal == -1):
					if after == 'S':
						print("Escaped in "+str(currentVal+2)+" minute(s).")
						found = True
						break
					else:
						valArr[current[0]][current[1]][current[2]-1] = currentVal+1
						queue.append([current[0],current[1],current[2]-1])
			if current[1] < (int(lrcArr[1])-1):
				after = charArr[current[0]][current[1]+1][current[2]]
				afterVal = valArr[current[0]][current[1]+1][current[2]]
				currentVal = valArr[current[0]][current[1]][current[2]]
				if after != '#' and (afterVal < currentVal+1 or afterVal == -1):
					if after == 'S':
						print("Escaped in "+str(currentVal+2)+" minute(s).")
						found = True
						break
					else:
						valArr[current[0]][current[1]+1][current[2]] = currentVal+1
						queue.append([current[0],current[1]+1,current[2]])
			if current[1] > 0:
				after = charArr[current[0]][current[1]-1][current[2]]
				afterVal = valArr[current[0]][current[1]-1][current[2]]
				currentVal = valArr[current[0]][current[1]][current[2]]
				if after != '#' and (afterVal < currentVal+1 or afterVal == -1):
					if after == 'S':
						print("Escaped in "+str(currentVal+2)+" minute(s).")
						found = True
						break
					else:
						valArr[current[0]][current[1]-1][current[2]] = currentVal+1
						queue.append([current[0],current[1]-1,current[2]])
			if current[0] < (int(lrcArr[0])-1):
				after = charArr[current[0]+1][current[1]][current[2]]
				afterVal = valArr[current[0]+1][current[1]][current[2]]
				currentVal = valArr[current[0]][current[1]][current[2]]
				if after != '#' and (afterVal < currentVal+1 or afterVal == -1):
					if after == 'S':
						print("Escaped in "+str(currentVal+2)+" minute(s).")
						found = True
						break
					else:
						valArr[current[0]+1][current[1]][current[2]] = currentVal+1
						queue.append([current[0]+1,current[1],current[2]])
			if current[0] > 0:
				after = charArr[current[0]-1][current[1]][current[2]]
				afterVal = valArr[current[0]-1][current[1]][current[2]]
				currentVal = valArr[current[0]][current[1]][current[2]]
				if after != '#' and (afterVal < currentVal+1 or afterVal == -1):
					if after == 'S':
						print("Escaped in "+str(currentVal+2)+" minute(s).")
						found = True
						break
					else:
						valArr[current[0]-1][current[1]][current[2]] = currentVal+1
						queue.append([current[0]-1,current[1],current[2]])
		if not found:
			print("Trapped!")
		lrc = sys.stdin.readline()
	return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

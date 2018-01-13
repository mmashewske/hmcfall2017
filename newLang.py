#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  newLang.py
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
	rep = ["@",'8','(','|)','3','#','6',"[-]",'|',"_|","|<",'1',"[]\/[]","[]\[]",'0',"|D","(,)","|Z",'$',"']['","|_|","\/","\/\/", "}{", "`/","2"]
	a = ""
	#print (rep[25])
	#print(sys.stdin.readline())
	for char in sys.stdin.readline().lower():
		#print char
		if ( (ord(char)-97) < 0) or ( (ord(char)-97) > 25 ):
			a+=char
		else:
			a = a+rep[ord(char)-97]
	print(a)
	#print (a == "@11 `/0|_||Z 8@$3 @|Z3 8310[]\[]6 ']['0 |_|$." )
	
			

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

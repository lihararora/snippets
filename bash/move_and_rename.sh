#!/bin/bash

for filename in ./*.py 
do
		t=`grep '@cryptopals: s[0-9]_c[0-9]$' "$filename" | grep -oh 's[0-9]_c[0-9]$'`
		if [ $t ]
		then
			mv $filename cryptopals/$t.py	
		fi
done

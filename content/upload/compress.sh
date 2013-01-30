#! /bin/bash

for file in `ls *.png`; do
	pngcrush $file $file -brute
done

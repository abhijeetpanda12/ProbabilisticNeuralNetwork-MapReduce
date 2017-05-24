#!/usr/bin/env python
import sys
last_count = None
last_class = None
for line in sys.stdin:
	line = line.strip()         
	count,clas,calc=line.split()        
	if not last_count or last_count != count:
		print(last_count, last_clas, mean)
		last_count = count
	if not last_class or last_class != clas:
		mean = summ/clas_count
		print(last_count, last_clas, mean)
		last_class = clas
		summ = clac
		clas_count = 1
	else:
		summ += calc
		clas_count += 1
#!/usr/bin/env python
import sys
last_count = None
new_count = 0
for line in sys.stdin:
    line = line.strip()
    count, category, clas, features=line.split()
    if category == "test":
    	test = features
    	new_count += 1
    if not last_cou or last_count != count:
        last_count = count
    elif category == "train":
    	#need to write the complete calculation
    	calc = (test - features)**2
    	print(new_count, clas,calc)
#!/usr/bin/env python
import sys
test_samples = 32
test_count = 1
for line in sys.stdin:
	line = line.strip()         
	splits = line.split("\t")        
	if splits[-1] == "train":
		for i in range(test_samples):
			print(i, "train", splits[-2], splits[:-2])
	elif:
		if splits[-1] == "test":
			print(test_count, "test", splits[-2], splits[:-2])
			test_count += 1
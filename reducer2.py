#!/usr/bin/env python
import sys
last_count = None
new_count = 0
for line in sys.stdin:
    line = line.strip()
    count, category, clas, features=line.split()
#!/usr/bin/env python3
import re
import sys

mapper_output = []
for line in sys.stdin:
    line = line.strip().lower()
    words = re.split(r"\s+", line) 
    for word in words:
        if word:
            mapper_output.append((word, 1))

for word, count in mapper_output:
    print(f"{word}\t{count}")

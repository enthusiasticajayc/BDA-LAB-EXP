#!/usr/bin/env python3
import sys
from collections import defaultdict

reducer_output = defaultdict(int) 
for line in sys.stdin:
    word, count = line.strip().split('\t')
    reducer_output[word] += int(count)

for word, count in reducer_output.items():
    print(f"{word}\t{count}")

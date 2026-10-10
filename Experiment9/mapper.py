#!/usr/bin/env python3
import sys
import json
import csv

header = next(sys.stdin).strip().split(',')
header = [h.strip() for h in header]

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    try:
        reader = csv.reader([line])
        values = next(reader)
    except Exception as e:
        continue
    
    document = {}
    for i, field in enumerate(header):
        try:
            if field in ['quantity', 'price']:
                document[field] = float(values[i])
            else:
                document[field] = values[i]
        except (ValueError, IndexError):
            document[field] = values[i]
            
    print(f"null\t{json.dumps(document)}")

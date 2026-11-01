
#!/usr/bin/env python3

import sys
import json
import csv

# Read CSV header
header_line = sys.stdin.readline()

if not header_line:
    sys.exit(0)

header = next(csv.reader([header_line.strip()]))

# Process each CSV record
for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    try:
        values = next(csv.reader([line]))

        document = {}

        for i, field in enumerate(header):
            if i >= len(values):
                document[field] = None
                continue

            value = values[i].strip()

            if field in ["quantity", "price"]:
                try:
                    document[field] = float(value)
                except ValueError:
                    document[field] = value
            else:
                document[field] = value

        # Output JSON document
        print("null\t" + json.dumps(document))

    except Exception:
        continue

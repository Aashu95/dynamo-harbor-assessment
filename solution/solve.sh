#!/bin/bash

python3 -c '
import json
from collections import Counter

with open("/workspace/access.log", "r") as f:
    lines = f.readlines()

ips = set()
paths = Counter()

for line in lines:
    parts = line.split()
    if len(parts) > 6:
        ips.add(parts[0])
        paths[parts[6]] += 1

top_path = paths.most_common(1)[0][0] if paths else ""

report_data = {
    "total_requests": len(lines),
    "unique_ips": len(ips),
    "top_path": top_path
}

with open("/workspace/report.json", "w") as f:
    json.dump(report_data, f)
'

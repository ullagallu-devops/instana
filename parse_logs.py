import sys
import re
import json

log_pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<timestamp>[^\]]+)] "(?P<method>\S+) (?P<endpoint>[^\s]+) [^"]+" (?P<status>\d+) (?P<size>\d+) "(?P<referer>[^"]+)" "(?P<user_agent>[^"]+)"')

for line in sys.stdin:
    match = log_pattern.match(line)
    if match:
        log_data = match.groupdict()
        log_data["status"] = int(log_data["status"])  # Convert status to integer
        log_data["size"] = int(log_data["size"]) if log_data["size"].isdigit() else 0
        print(json.dumps(log_data))

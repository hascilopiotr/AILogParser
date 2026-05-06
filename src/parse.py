import re
from datetime import datetime
from collections import Counter
pattern = re.compile(r'\[(.*?)\] \[(\w+)\] \[(\w+)\] (.+)')

class LogParser:
    def parse_line(self, line):
        match = pattern.match(line)
        if match:
            timestamp, level, module, message = match.groups()
            ts = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
            return { 'timestamp' : ts,
                     'level' : level,
                     'module' : module,
                     'message' : message }
        else:
            return None
    def parse_file(self, path):
        with open(path, 'r') as f:
            for line in f:
                parsed = self.parse_line(line.strip())
                if parsed:
                    yield parsed

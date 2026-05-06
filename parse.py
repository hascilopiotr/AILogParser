import re

pattern = re.compile(r'\[(.*?)\] \[(\w+)\] \[(\w+)\] (.+)')


class LogParser:
    def parse_line(self, line):
        match = pattern.match(line)
        if match:
            timestamp, level, module, message = match.groups()
            return { 'timestamp' : timestamp,
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

if __name__ == '__main__':
    parser = LogParser()
    entries = list(parser.parse_file('test_logs.log'))
    print(f"Sparsowano: {len(entries)} linii")
    if entries:
        print(f"Pierwsza: {entries[0]}")
        print(f"Ostatnia: {entries[-1]}")
from src.parse import LogParser
from src.analyzer import LogAnalyzer

parser = LogParser()
entries = list(parser.parse_file('test_logs.log'))
analyzer = LogAnalyzer(entries)

print("=== Levels ===")
print(analyzer.count_by_level())

print("\n=== Modules ===")
print(analyzer.count_by_module())

print("\n=== Errors per module ===")
print(analyzer.errors_per_module())

print("\n=== Top 5 messages ===")
for msg, count in analyzer.top_messages(5):
    print(f"  {count:4d}  {msg}")


print("\n=== Summary ===")
print(analyzer.summary())
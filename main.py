from src.parse import LogParser
from src.analyzer import LogAnalyzer
from src.ai_insights import AIInsights

parser = LogParser()
entries = list(parser.parse_file('test_logs.log'))
analyzer = LogAnalyzer(entries)
ai = AIInsights()
print(ai.summarize_logs(analyzer.to_stats_dict()))
print(ai.categorize_errors(analyzer.to_stats_dict()))

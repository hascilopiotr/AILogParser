from collections import Counter

class LogAnalyzer:
    def __init__(self, entries):
        self.entries = list(entries)

    def count_by_level(self):
        return Counter(e['level'] for e in self.entries)
    def count_by_module(self):
        return Counter(e['module'] for e in self.entries)
    def errors_per_module(self):
        return Counter(e['module'] for e in self.entries if e['level'] == 'ERROR')
    def top_messages(self, n=10):
        counter = Counter(e['message'] for e in self.entries)
        return counter.most_common(n)


    def summary(self):
        return {
            'by_level': self.count_by_level(),
            'by_module': self.count_by_module(),
            'errors_per_module': self.errors_per_module(),
        }
    def to_stats_dict(self):
        s = self.summary()
        return {
            'total' : self.entries.count,
            'by_level' : dict(self.count_by_level()),
            'errors_per_module' : dict(self.errors_per_module()),
            'top_errors' : self.top_messages(5),
            'unique_errors': list(set(
                e['message'] for e in self.entries if e['level'] == 'ERROR'
            )),
        }
# Deduplicator class

class Deduplicator:
    def __init__(self, df):
        self.df = df

    def transform(self):
        return self.df[['Imię']].drop_duplicates()

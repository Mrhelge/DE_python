# JsonLoader class

class JsonLoader:
    def __init__(self, df, orient='records', index=False, lines=True):
        self.df = df
        self.orient = orient
        self.index = index
        self.lines = lines

    def load(self, path):
        self.df.to_json(path, orient=self.orient, index=self.index, lines=self.lines)

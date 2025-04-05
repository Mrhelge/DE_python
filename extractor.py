#  CsvExtractor class

import pandas as pd


class CsvExtractor:
    def __init__(self, path):
        self.path = path

    def extract(self):
        return pd.read_csv(self.path)

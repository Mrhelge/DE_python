from extractor import CsvExtractor
from deduplicator import Deduplicator
from loader import JsonLoader


class Job:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def run(self):
        source_data = CsvExtractor(self.input_path).extract()
        transformed_data = Deduplicator(source_data).transform()
        JsonLoader(transformed_data).load(self.output_path)

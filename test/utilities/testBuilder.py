# Pour plus tard
from src.ohce import OHCE


class OHCEBuilder:
    def __init__(self):
        self.language = ""

    def with_language(self, language):
        self.language = language
        return self

    def build(self):
        return OHCE(self.language)
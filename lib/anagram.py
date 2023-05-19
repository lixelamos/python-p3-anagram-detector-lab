# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        matches = []
        sorted_word = sorted(self.word.lower())
        for candidate in words:
            sorted_candidate = sorted(candidate.lower())
            if sorted_candidate == sorted_word and candidate.lower() != self.word.lower():
                matches.append(candidate)
        return matches

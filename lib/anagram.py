class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        possible_anagrams = []
        
        word_list = sorted([letter for letter in self.word])
        for word in list:
            if sorted([letter for letter in word]) == word_list:
                possible_anagrams.append(word)
        return possible_anagrams

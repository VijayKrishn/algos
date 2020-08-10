import collections

class Finder:

    def __init__(self, arr=None):
        self.dictionary = collections.defaultdict(list)
        self.build_anagrams(arr)

    def build_anagrams(self, arr):
        for ele in arr:
            sortele = sorted(ele)
            key = "".join(sortele)
            self.dictionary[key].append(ele)

    def find(self, input):
        sortinp = sorted(input)
        key = "".join(sortinp)
        return self.dictionary[key]

finder = Finder(['asd', 'asdd', 'rfre'])
print(finder.find('sad'))
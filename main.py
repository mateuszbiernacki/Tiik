class TextAnalyzer:
    def __init__(self, file_path: str):
        file = open(file_path, 'r', encoding='utf-8')
        self.input = file.read()
        file.close()
        self.char_dict = {}
        self.string_length = 0
        for char in self.input:
            self.string_length += 1
            if char in self.char_dict:
                self.char_dict[char] += 1
            else:
                self.char_dict[char] = 1
        self.char_dict = {
            key: value for key, value in sorted(self.char_dict.items(), key=lambda item: item[1], reverse=True)
        }

    def entropy(self):
        from math import log2
        sum_ = 0.0
        for char, cardinality in self.char_dict.items():
            probability = cardinality / self.string_length
            sum_ += probability * log2(1/probability)
        return sum_


if __name__ == '__main__':
    polish_literary = TextAnalyzer('pan-tadeusz.txt')
    print(f'Polski literacki\n '
          f'\tCzęstość występowywania znaków:\n '
          f'\tLiczba znaków = {polish_literary.string_length}\n'
          f'\t{polish_literary.char_dict}\n'
          f'\tEntropia = {polish_literary.entropy()}')
    polish_it = TextAnalyzer('tekst_informatyczny.txt')
    print(f'Polski informatyczny\n '
          f'\tCzęstość występowywania znaków:\n '
          f'\tLiczba znaków = {polish_it.string_length}\n'
          f'\t{polish_it.char_dict}\n'
          f'\tEntropia = {polish_it.entropy()}')
    english = TextAnalyzer('hamlet.txt')
    print(f'Angielski\n '
          f'\tCzęstość występowywania znaków:\n '
          f'\tLiczba znaków = {english.string_length}\n'
          f'\t{english.char_dict}\n'
          f'\tEntropia = {english.entropy()}')

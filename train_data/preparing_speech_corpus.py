# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# Import essential libraries
## Work with files and folders
import os
from pathlib import Path
## Encode text
import unicodedata
## Progress bar
from tqdm import tqdm

# Define dirs
PROJECT_DIR = Path(__file__).absolute().parents[1]
TRAIN_DIR = os.path.join(PROJECT_DIR, "train_data")

# Define classes
class Vietnamese:

    def __init__(self):
        # Define Vietnamese consonants, vowels, punctuations, alphabet and phonemes
        # Read more at: https://www.aclweb.org/anthology/W16-5207.pdf
        self._consonants = [
                            'ngh',
                            'ch', 'gh', 'gi', 'kh', 'ng', 'nh', 'ph', 'qu', 'tr', 'th',
                            'b', 'c', 'd', 'đ', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'x'
                            ]
        self._vowels = (
                        ['a', 'ă', 'â', 'e', 'ê', 'i', 'o', 'ô', 'ơ', 'u', 'ư', 'y'] +
                        ['á', 'ắ', 'ấ', 'é', 'ế', 'í', 'ó', 'ố', 'ớ', 'ú', 'ứ', 'ý'] +
                        ['à', 'ằ', 'ầ', 'è', 'ề', 'ì', 'ò', 'ồ', 'ờ', 'ù', 'ừ', 'ỳ'] +
                        ['ả', 'ẳ', 'ẩ', 'ẻ', 'ể', 'ỉ', 'ỏ', 'ổ', 'ở', 'ủ', 'ử', 'ỷ'] +
                        ['ã', 'ẵ', 'ẫ', 'ẽ', 'ễ', 'ĩ', 'õ', 'ỗ', 'ỡ', 'ũ', 'ữ', 'ỹ'] +
                        ['ạ', 'ặ', 'ậ', 'ẹ', 'ệ', 'ị', 'ọ', 'ộ', 'ợ', 'ụ', 'ự', 'ỵ']
                        )
        self._punctuations  = ['.', '?', '"', '\'', ',', '-', '–', '!', ':', ';', '(', ')', '[', ']', '\n' ]
        self._alphabet = sorted(set(''.join(self._consonants + self._vowels)))
        self._phonemes = self._consonants + self._vowels

    # Define methods
    def text_to_phonemes(self, text, keep_punctuation=False):
        """Function to convert text to phonemes"""
        # Normalize text using unicodedata
        text = unicodedata.normalize('NFKC', text.strip().lower())
        print("Finish normalizing")
        idx = 0
        # Create an empty list to store output
        out = []
        # Convert text to phonemes
        while idx < len(text):
            # length: 3, 2, 1
            for l in [3, 2, 1]:
                if idx + l <= len(text) and text[idx: (idx+l)] in self._phonemes:
                    out.append(text[idx: (idx+l)])
                    idx = idx + l
                    break
                else:
                    if idx < len(text):
                        if keep_punctuation and text[idx] in self._punctuations:
                            out.append(text[idx])
                    if text[idx] == ' ':
                        out.append(text[idx])
                    idx = idx + 1
        return out

    def create_phonemes(self):
        """Function to create phonemes.txt from words.txt"""
        lines = open(TRAIN_DIR + '/content/words.txt', 'r').readlines()
        with open(TRAIN_DIR + '/content/phonemes.txt', 'w') as f:
            for line in tqdm(lines, desc="Creating phonemes"):
                t = ' '.join(text_to_phonemes(line))
                f.write(t + '\n')
            f.close()
        print("Finish creating phonemes.txt")

    def create_dictionary(self):
        """Function to create dictionary.txt from phonemes.txt"""
        ws = open(TRAIN_DIR + '/content/words.txt').readlines()
        ps = open(TRAIN_DIR + '/content/phonemes.txt').readlines()
        with open(TRAIN_DIR + '/content/dictionary.txt', 'w') as f:
            for w, p in zip(ws, ps):
                w = w.strip()
                p = p.strip()

                # this is a hack to match phoneme set in the vietTTS repo
                p = p.split()
                p = [ " ".join(list(x)) for x in p]
                p = " ".join(p)
                # hack ends

                if w == "q":
                    p = "qu i"
                f.write(f'{w}\t{p}\n')
            f.close()
        print("Finish creating dictionary.txt")

    def create_corpus(self, script_csv):
        """Function to create speech corpus from scripts"""
        s = open(script_csv).readlines()
        for l in s:
            fn, txt, t = l.strip().split('|')
            fn = Path(fn).stem
            with open(TRAIN_DIR + f'/content/wavs/{fn}.txt', 'w') as f:
                f.write(txt + '\n')
                f.close()
        print("Finish creating speech corpus")

if __name__ == '__main__':
    # Calling classes
    vn = Vietnamese()
    # Create phonemes
    vn.create_phonemes()
    # Create dictionary
    vn.create_dictionary()
    # Create Corpus
    vn.create_corpus(PROJECT_DIR + '/assets/infore/scripts.csv')

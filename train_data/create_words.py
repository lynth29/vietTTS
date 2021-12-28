# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# Import essential libraries
## Work with files and folders
import os
from pathlib import Path
import re

# Define dirs
PROJECT_DIR = Path(__file__).absolute().parents[1]
ASSETS_DIR = os.path.join(PROJECT_DIR, "assets", "vietsoftpro", "fileThuAm")
TRAIN_DIR = os.path.join(PROJECT_DIR, "train_data")

#  Define class
class Convert:

    # Constructor
    def __init__(self):
        # Roman numeral dictionary
        self.rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
        'M': 1000}
        # Integer dictionary
        self.int_dict = { 0 : 'không', 1 : 'một', 2 : 'hai', 3 : 'ba', 4 : 'bốn', 5 : 'năm', 6 : 'sáu', 7 : 'bảy', 8 : 'tám', 9 : 'chín',
              10 : 'mười', 11 : 'mười một', 12 : 'mười hai', 13 : 'mười ba', 14 : 'mười bốn', 15 : 'mười lăm', 16 : 'mười sáu', 17 : 'mười bảy', 18 : 'mười tám', 19 : 'mười chín',
              20 : 'hai mươi', 30 : 'ba mươi', 40 : 'bốn mươi', 50 : 'năm mươi', 60 : 'sáu mơi', 70 : 'bảy mươi', 80 : 'tám mươi', 90 : 'chín mươi' }
        # Special dict
        self.tech_dict = {"4.0":"bốn chấm không",
                          "2G":"hai gờ", "3G":"ba gờ", "4G":"bốn gờ","5G":"năm gờ",
                          "CNTT":"công nghệ thông tin","GDĐT":"giao dịch điện tử","TW":"trung ương", "TT&TT":"thông tin và truyền thông"}
        self.pattern = re.compile(r'(?<!\w)(' + '|'.join(re.escape(key) for key in self.tech_dict.keys()) + r')(?!\w)')

    # Methods
    def roman_to_int(self, roman_num):
        """Funtion to convert roman numeral to int."""
        int_val = 0
        for i in range(len(roman_num)):
            if i > 0 and self.rom_val[roman_num[i]] > self.rom_val[roman_num[i - 1]]:
                int_val += self.rom_val[roman_num[i]] - 2 * self.rom_val[roman_num[i - 1]]
            else:
                int_val += self.rom_val[roman_num[i]]
        return int_val

    def int_to_vn(self, num):
        """Function to convert integer into Vietnamese words"""
        # Further numeral
        k = 1000
        m = k * 1000
        b = m * 1000

        assert(0 <= num)

        if (num < 20):
            return self.int_dict[num]

        if (num < 100):
            if num % 10 == 0:
                return self.int_dict[num]
            else:
                return self.int_dict[num // 10 * 10] + ' ' + self.int_dict[num % 10]

        if (num < k):
            if num % 100 == 0:
                return self.int_dict[num // 100] + ' trăm'
            else:
                return self.int_dict[num // 100] + ' trăm ' + self.int_to_vn(num % 100)

        if (num < m):
            if num % k == 0:
                return self.int_to_vn(num // k) + ' nghìn'
            else:
                return self.int_to_vn(num // k) + ' nghìn ' + self.int_to_vn(num % k)

        if (num < b):
            if (num % m) == 0:
                return self.int_to_vn(num // m) + ' triệu'
            else:
                return self.int_to_vn(num // m) + ' triệu ' + self.int_to_vn(num % m)

        if (num < t):
            if (num % b) == 0:
                return self.int_to_vn(num // b) + ' tỷ'
            else:
                return self.int_to_vn(num // b) + ' tỷ ' + self.int_to_vn(num % b)

        raise AssertionError('num is too large: %s' % str(num))

class VietSoftPro:

    def __init__(self, num_of_file: int):
        self.num_of_file = num_of_file

    def txt_to_words(self):
        """Import multiple txt files and make words list"""
        # Create an empty list to store output
        output = []
        # Go through each file
        for n in range(1,self.num_of_file):
            if n < 10:
                n = "0" + str(n)
            try:
                with open(ASSETS_DIR + '/' + str(n) + '.txt', 'r') as f:
                    print(f'Getting words from {n}.txt')
                    txt = f.read()
                    # Convert with tech_dict
                    txt = Convert().pattern.sub(lambda x: Convert().tech_dict[x.group()], txt)
                    # Remove punctuations
                    txt = re.sub("[^\w\s]", " ", txt)
                    # Replace \n with blank
                    txt = txt.replace("\n"," ")
                    # Split words
                    word_list = txt.split(' ')
                    # Add to output
                    output.extend(word_list)
            except FileNotFoundError:
                continue
        # Remove duplicates and sort
        output = sorted([*{*output}])
        return output[1:]

    def rom_to_words(self, words_list):
        """Convert words of list from integer"""
        # Create an empty list to store output
        output = []
        # Go through each word
        for word in words_list:
            # Convert roman num
            try:
                word = Convert().roman_to_int(word)
                output.append(str(word))
            except KeyError:
                # Not roman num
                output.append(word)
        return sorted([*{*output}])

    def num_to_words(self, words_list):
        """Convert words of list from integer"""
        # Create an empty list to store output
        output = []
        # Go through each word
        for word in words_list:
            # Convert int
            try:
                word = Convert().int_to_vn(int(word))
                output.extend(word.split(' '))
            except ValueError:
                # Not number
                output.append(word)
        return sorted([*{*output}])

if __name__ == '__main__':
    source = VietSoftPro(26)
    raw_words = source.txt_to_words()
    first = source.rom_to_words(raw_words)
    last = source.num_to_words(first)
    with open(TRAIN_DIR + '/contents/words.txt','w') as f:
        for word in last:
            if len(word) > 1:
                f.write(word + "\n")
        f.close()

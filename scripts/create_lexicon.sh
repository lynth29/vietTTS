#!/bin/bash

# Create dirs in train_data
echo "======="
echo "Preparing contents to align dataset..."
mkdir ./train_data/content
mkdir ./train_data/content/wavs
mkdir ./train_data/content/aligned

# Create words.txt file
python -m train_data.create_words
# Create lexicon.txt file
python -m train_data.preparing_speech_corpus

echo "Finish preparing contents to align dataset into pretrained dataset"
echo "======="

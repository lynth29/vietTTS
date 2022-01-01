#!/bin/bash

# A script to run Montreal Forced Aligner (MFA)
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
# activate MFA and align dataset
# echo "Activate MFA"
# source /miniconda3/bin/activate aligner
# echo "Denoising and aligning"
# mfa train --clean -C ./train_data/content/wavs ./train_data/content/lexicon.txt ./train_data/content/aligned
# echo "Finish aligning dataset"
# conda deactivate
# echo "Deactivate MFA"

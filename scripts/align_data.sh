#!/bin/bash

# A script to run Montreal Forced Aligner (MFA) installation file
echo "Install MFA"
bash ./scripts/install_mfa.sh $1

# Create dirs in train_data
echo "Preparing contents to align dataset..."
mkdir ./train_data/contents
mkdir ./train_data/contents/wavs
mkdir ./train_data/contents/test

# Create words.txt files
python -m train_data.create_words
python -m train_data.preparing_speech_corpus

echo "Finish preparing contents to align dataset into pretrained dataset"
echo "======="
# activate MFA
echo "Activate MFA and align dataset"
source $1/miniconda3/bin/activate aligner; mfa train --clean -C ./train_data/contents/wavs ./train_data/contents/dictionary.txt ./train_data/contents/test
echo "Finish aligning dataset"
conda deactivate
echo "Deactivate MFA"

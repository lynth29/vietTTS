#!/bin/bash

# A script to run Montreal Forced Aligner (MFA) installation file
echo "Install MFA"
bash ./scripts/install_mfa.sh $1

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
echo "Activate MFA and align dataset"
source $1/miniconda3/bin/activate aligner; mfa train --clean -C ./train_data/content/wavs ./train_data/content/lexicon.txt ./train_data/content/aligned
echo "Finish aligning dataset"
conda deactivate
echo "Deactivate MFA"

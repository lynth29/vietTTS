#!/bin/bash

## a script to run Montreal Forced Aligner (MFA) installation file
echo "Install MFA"
bash ./scripts/install_mfa.sh $1

# Prepare contents to align data
echo "Preparing contents to align dataset..."
mkdir ./train_data/content
mkdir ./train_data/content/wavs
mkdir ./train_data/content/test
cat ./assets/infore/lexicon.txt | cut -f 1 > ./train_data/content/words.txt
python -m train_data.preparing_speech_corpus

echo "Finish preparing contents to align dataset into pretrained dataset"
echo "======="
# activate MFA
echo "Activate MFA and align dataset"
source $1/miniconda3/bin/activate aligner; mfa train --clean -C ./train_data/content/wavs ./train_data/content/dictionary.txt ./train_data/content/test
echo "Finish aligning dataset"
conda deactivate
echo "Deactivate MFA"

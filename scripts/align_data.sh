#!/bin/bash

## a script to run Montreal Forced Aligner (MFA) installation file
echo "Install MFA"
bash ./scripts/install_mfa.sh $1

## Prepare contents to align data
echo "Preparing contents to align dataset..."
mkdir ./train_data/content
mkdir ./train_data/content/wavs
cat ./assets/infore/lexicon.txt | cut -f 1 > ./train_data/content/words.txt
python -m train_data.preparing_speech_corpus

echo "Finish preparing contents to align dataset into pretrained dataset"
echo "======="
## activate MFA
echo "Activate MFA"
source $1/miniconda3/bin/activate aligner
echo "Using MFA to align dataset"
mkdir ./train_data/content/test
mfa train --clean -C /content/wavs /content/dictionary.txt /content/test
echo "Finish aligning dataset"
conda deactivate
echo "Deactivate MFA"

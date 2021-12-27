#!/bin/bash

## a script to run Montreal Forced Aligner (MFA) installation file
echo "Install MFA"
bash ./scripts/install_mfa.sh $1

## activate MFA
echo "Activate MFA"
source $1/miniconda3/bin/activate aligner

## Prepare contents to align data
echo "Preparing contents to align dataset..."
mkdir ./train_data/content
cat ./train_data/lexicon.txt | cut -f 1 > ./train_data/content/words.txt
python -m train_data.convert_dataset

echo -e "\nFinish preparing contents to align dataset into pretrained dataset"

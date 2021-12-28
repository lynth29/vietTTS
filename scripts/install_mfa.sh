#!/bin/bash

## a script to install Montreal Forced Aligner (MFA)

root_dir=$1
mkdir -p $root_dir
cd $root_dir

# download miniconda3
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  link="https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
  filename="Miniconda3-latest-Linux-x86_64.sh"
elif [[ "$OSTYPE" == "darwin"* ]]; then
  link="https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh"
  filename="Miniconda3-latest-MacOSX-x86_64.sh"
elif [[ "$OSTYPE" == "cygwin" ]]; then
  link="https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe"
  filename="Miniconda3-latest-Windows-x86_64.exe"
fi
wget -q --show-progress $link
bash $filename -b -p $root_dir/miniconda3 -f
rm $filename

# create env and install mfa
$root_dir/miniconda3/bin/conda create -n aligner -c conda-forge montreal-forced-aligner python=3.8 openfst pynini ngram baumwelch -y

echo -e "\n======== DONE =========="
echo -e "\nTo activate MFA, run: source $root_dir/miniconda3/bin/activate aligner"
echo -e "\nTo deactivate MFA, run: conda deactivate"
echo -e "\nTo delete MFA, run: rm -rf $root_dir"
echo -e "\nSee: https://montreal-forced-aligner.readthedocs.io/en/latest/first_steps/index.html#first-steps to know how to use MFA"

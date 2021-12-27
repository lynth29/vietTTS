#!/bin/bash

## a script to install Montreal Forced Aligner (MFA)

root_dir=$1
mkdir -p $root_dir
cd $root_dir

# download miniconda3
wget -q --show-progress https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
bash Miniconda3-latest-MacOSX-x86_64.sh -b -p $root_dir/miniconda3 -f
rm Miniconda3-latest-MacOSX-x86_64.sh

# create env and install mfa
$root_dir/miniconda3/bin/conda create -n aligner -c conda-forge montreal-forced-aligner python=3.8 openfst pynini ngram baumwelch -y

echo -e "\n======== DONE =========="
echo -e "\nTo activate MFA, run: source $root_dir/miniconda3/bin/activate aligner"
echo -e "\nTo deactivate MFA, run: conda deactivate"
echo -e "\nTo delete MFA, run: rm -rf $root_dir"
echo -e "\nSee: https://montreal-forced-aligner.readthedocs.io/en/latest/aligning.html to know how to use MFA"

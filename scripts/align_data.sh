echo "Validating dataset"
source /miniconda3/bin/activate aligner; mfa validate ./train_data/content/wavs ./train_data/content/lexicon.txt
echo "Denoising and aligning"
mfa train --clean ./train_data/content/wavs ./train_data/content/lexicon.txt ./train_data/content/aligned
echo "Finish aligning dataset"
conda deactivate
echo "Deactivate MFA"

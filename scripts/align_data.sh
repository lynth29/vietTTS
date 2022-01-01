# activate MFA and align dataset
echo "Activate MFA"
source /miniconda3/bin/activate aligner
echo "Validating dataset"
mfa validate ./train_data/content/wavs ./train_data/content/lexicon.txt
echo "Denoising and aligning"
mfa train --clean -C ./train_data/content/wavs ./train_data/content/lexicon.txt ./train_data/content/aligned
echo "Finish aligning dataset"
conda deactivate
echo "Deactivate MFA"

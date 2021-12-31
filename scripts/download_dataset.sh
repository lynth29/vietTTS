# deactivate mfa
conda deactivate
# train_data dir
data_root="./train_data/content/wavs" # modify this if change dir
# GGdrive id
ggdrive_id=$1
# Make dir
pushd .
mkdir -p $data_root
cd $data_root
# Download
echo "Downloading dataset..."
gdown --id $1
unzip -q fileThuAm.zip
echo "Unzipped dataset"
popd
# Move all files to wavs
mv $data_root/fileThuAm/textBoTruong/*.txt $data_root
mv $data_root/fileThuAm/*.wav $data_root
rm -r $data_root/fileThuAm

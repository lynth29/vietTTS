# train_data dir
data_root="./train_data/content/wavs" # modify this if change dir
# Make dir
pushd .
mkdir -p $data_root
# Download
echo "Downloading dataset..."
python ./scripts/download_fileThuAm.py
mv ./fileThuAm.zip $data_root
cd $data_root
unzip -q fileThuAm.zip
echo "Unzipped dataset"
popd
# Move all files to wavs
mv $data_root/fileThuAm/textBoTruong/*.txt $data_root
mv $data_root/fileThuAm/*.wav $data_root
rm -r $data_root/fileThuAm

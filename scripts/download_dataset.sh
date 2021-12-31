# train_data dir
data_root="./train_data/wavs" # modify this if change dir
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

# train_data dir
data_root="./assets/vietsoftpro" # modify this
# GGdrive id
ggdrive_id=$1
# Make dir
pushd .
mkdir -p $data_root
cd $data_root
# Download
gdown --id $1 -O fileThuAm.zip
unzip -q fileThuAm.zip
popd

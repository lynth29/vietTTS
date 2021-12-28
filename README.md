# Hướng dẫn sử dụng vietTTS
*Updated: 28/12/2021*

#### Yêu cầu cơ bản:
- Python >= 3.8
- Git
- Bash

### 1. Clone các project cần thiết
#### a. Clone vietTTS-modified để lấy các scripts hỗ trợ
```sh
git clone https://github.com/lynth29/vietTTS-modified.git
```
#### b. Clone vietTTS từ NTT123
```sh
git clone https://github.com/NTT123/vietTTS.git
```
### 2. Copy các scripts hỗ trợ từ vietTTS-modified sang vietTTS
#### a. Các scripts từ folder `./scripts`
```sh
cp vietTTS-modified/scripts/align_data.sh vietTTS/scripts
cp vietTTS-modified/scripts/install_mfa.sh vietTTS/scripts
cp vietTTS-modified/scripts/download_dataset.sh vietTTS/scripts
```
#### b. Các scripts từ folder `./train_data`
```sh
mkdir vietTTS/train_data
cp vietTTS-modified/train_data/preparing_speech_corpus.py vietTTS/train_data/preparing_speech_corpus.py
cp vietTTS-modified/train_data/create_words.py vietTTS/train_data/create_words.py
```
#### c. Các scripts từ folder `./vietTTS`
```sh
cp vietTTS-modified/nat/config.py vietTTS/nat/config.py
```
File `config.py` đã thay đổi đường dẫn của `ckpt_dir` và `data_dir` để phù hợp với dataset từ `fileThuAm.zip`.
- Đường dẫn cũ:
```sh
ckpt_dir = Path("assets/infore/nat")
data_dir = Path("assets/infore/data")
```
- Đường dẫn mới:
```sh
ckpt_dir = Path("assets/vietsoftpro/nat")
data_dir = Path("assets/vietsoftpro/data")
```

### 3. Chạy file setup từ project vietTTS
```sh
cd vietTTS
pip3 install -e .
```
### 4. Tải dataset
Dataset sau khi tải được unzip tại folder `./train_data/wavs`.
```sh
bash ./scripts/download_dataset.sh [id] # [id] là id của link google drive
```
**Lưu ý**: Sau khi tải dataset, kiểm tra chính tả trong các file `.txt` để tạo được file `lexicon.txt` tốt nhất.
### 5. Tạo lexicon, dùng MFA để khử nhiễu và tạo các file .TextGrid
Script `align_data.sh` được viết riêng cho dataset từ `fileThuAm.zip`.
```sh
bash ./scripts/align_data.sh [~] # [~] là đường dẫn cài đặt MFA
```
Quy trình xử lý của script được diễn ra như sau:
```flow
1. Tải miniconda3, MFA
2. Cài MFA
3. Tạo file `words.txt` và `lexicon.txt`
4. Khử nhiễu và tạo file `.TextGrid`
```
### 6. Train duration model và train acoustic model
#### a. Train duration model
```sh
python3 -m vietTTS.nat.duration_trainer
```
#### b. Train acoustic model
```sh
python3 -m vietTTS.nat.acoustic_trainer
```
### 7. Train HiFiGAN vocoder
#### a. Clone project hifi-gan về trong folder project vietTTS
```sh
git clone https://github.com/jik876/hifi-gan.git
```
#### b. Chuyển các file `.TextGrid` sang dạng hifi-gan
```sh
ln -sf ./train_data ./hifi-gan/data
cd ./hifi-gan/data
ls -1 *.TextGrid | sed -e 's/\.TextGrid$//' > ./hifi-gan/files.txt
cd ..
head -n 100 ./hifi-gan/files.txt > val_files.txt
tail -n +101 ./hifi-gan/files.txt > train_files.txt
rm data/files.txt
```
#### c. Copy file `config.json` trong folder `/assets` sang folder `/higi-gan`
```sh
cp ./assets/hifigan/config.json ./config.json
```
#### d. Chạy script để train HiFiGAN
```sh
python3 train.py --config config.json --input_wavs_dir=data  --input_training_file=train_files.txt  --input_validation_file=val_files.txt
```

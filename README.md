# Hướng dẫn sử dụng vietTTS
*Updated: 27/12/2021*

### B1. Clone các project cần thiết
#### a. Clone vietTTS-modified để lấy các scripts hỗ trợ
```sh
git clone https://github.com/lynth29/vietTTS-modified.git
```
#### b. Clone vietTTS từ NTT123
```sh
git clone https://github.com/NTT123/vietTTS.git
```
### B2. Copy các scripts hỗ trợ từ vietTTS-modified sang vietTTS
```sh
cp vietTTS-modified/scripts/align_data.sh vietTTS/scripts
cp vietTTS-modified/scripts/install_mfa.sh vietTTS/scripts
cp vietTTS-modified/scripts/download_dataset.sh vietTTS/scripts
mkdir vietTTS/train_data
cp vietTTS-modified/train_data/preparing_speech_corpus.py vietTTS/train_data/preparing_speech_corpus.py
cp vietTTS-modified/train_data/create_words.py vietTTS/train_data/create_words.py
```
### B3. Chạy file setup từ vietTTS
```sh
cd vietTTS
pip3 install -e .
```
### B4. Tải dataset
```sh
bash ./scripts/download_dataset.sh [id] # [id] là id của link google drive
```
### B4. Dùng MFA để chuyển hóa dataset
```sh
bash ./scripts/align_data.sh [~] # [~] là đường dẫn cài đặt MFA
```

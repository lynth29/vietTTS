# Hướng dẫn sử dụng vietTTS
Updated: 27/12/2021

## B1. Clone các project cần thiết
### a. Clone vietTTS-modified để lấy các scripts hỗ trợ
```sh
git clone https://github.com/lynth29/vietTTS-modified.git
```
### b. Clone vietTTS từ NTT123
```sh
git clone https://github.com/NTT123/vietTTS.git
```
## B2. Copy các scripts hỗ trợ từ vietTTS-modified sang vietTTS
```sh
cp vietTTS-modified/scripts vietTTS/scripts
cp vietTTS-modified/assets/infore vietTTS/assets/infore
cp vietTTS-modified/train_data/preparing_speech_corpus.py vietTTS/train_data/preparing_speech_corpus.py
```
## B3. Chạy file setup từ vietTTS
```sh
cd vietTTS
pip3 install -e .
```
## B4. Convert dataset
```sh
bash ./scripts/align_data.sh
```

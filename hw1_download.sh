#!/bin/bash

export field=1mdEVRcvKfUc4IGXXMfJHQZRybzWazIkx
export filename=./ultralytics/yolocheckpoint.pt

wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1mdEVRcvKfUc4IGXXMfJHQZRybzWazIkx' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1mdEVRcvKfUc4IGXXMfJHQZRybzWazIkx" -O ./ultralytics/yolocheckpoint.pt && rm -rf /tmp/cookies.txt

export field=1KOD5Nnp9H90a_W_X2Y9HUAM2KYVh2DAT
export filename=./ultralytics/yolopretrain.pt
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1KOD5Nnp9H90a_W_X2Y9HUAM2KYVh2DAT' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1KOD5Nnp9H90a_W_X2Y9HUAM2KYVh2DAT" -O ./ultralytics/yolopretrain.pt && rm -rf /tmp/cookies.txt

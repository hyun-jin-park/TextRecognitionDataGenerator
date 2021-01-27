#!/bin/bash
#common 80만장
./common.sh common 8 &
#digits 120만장
./common.sh digits 12 &
#eng_name 400만장
./common.sh eng_name 40 & 
#Kor_random.100만장
./common.sh kor_random 10 & 
#kor_wiki.300만장
./common.sh kor_from_wiki 30 &
#kor_name.500만장
./common.sh kor_name 50 &
#kor_address.500만장
./common.sh kor_address 50 &
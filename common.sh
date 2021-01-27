#!/bin/bash
#common 80만장
./run-k-d-b3.sh ${1} ${2} /home/embian/hjpark/TextRecognitionDataGenerator/data/final/${1}.txt ./trdg/fonts/kr/ ./raw_data/${1}/kdb &> log1.txt 
./run-b-k-b3.sh ${1} ${2} /home/embian/hjpark/TextRecognitionDataGenerator/data/final/${1}.txt ./trdg/fonts/kr/ ./raw_data/${1}/bk &> log2.txt 
./run-k-b-d-b3.sh ${1} ${2} /home/embian/hjpark/TextRecognitionDataGenerator/data/final/${1}.txt ./trdg/fonts/kr/ ./raw_data/${1}/kb &> log3.txt 
./run-b-d-b3.sh ${1} ${2} /home/embian/hjpark/TextRecognitionDataGenerator/data/final/${1}.txt ./trdg/fonts/kr/ ./raw_data/${1}/db  &> log4.txt 
./run-b3-m0.sh ${1} ${2} /home/embian/hjpark/TextRecognitionDataGenerator/data/final/${1}.txt ./trdg/fonts/kr/ ./raw_data/${1}/m0 &> log5.txt 
./run-b3-m1.sh ${1} ${2} /home/embian/hjpark/TextRecognitionDataGenerator/data/final/${1}.txt ./trdg/fonts/kr/ ./raw_data/${1}/m1 &> log6.txt 
./run-b3-m2.sh ${1} ${2} /home/embian/hjpark/TextRecognitionDataGenerator/data/final/${1}.txt ./trdg/fonts/kr/ ./raw_data/${1}/m2 &> log7.txt 
./run-k2-b3.sh ${1} ${2} /home/embian/hjpark/TextRecognitionDataGenerator/data/final/${1}.txt ./trdg/fonts/kr/ ./raw_data/${1}/k2b3 &> log8.txt 
./run-bl2-b3-m2.sh ${1} ${2} /home/embian/hjpark/TextRecognitionDataGenerator/data/final/${1}.txt ./trdg/fonts/kr/ ./raw_data/${1}/bl2m2 &> log9.txt 
./run-cs3-m2.sh ${1} ${2} /home/embian/hjpark/TextRecognitionDataGenerator/data/final/${1}.txt ./trdg/fonts/kr/ ./raw_data/${1}/cs3m2 &> log0.txt 
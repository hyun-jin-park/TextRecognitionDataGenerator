#!/bin/bash
LANG=$1
COUNT_B3=$((80 * $2))
COUNT_BO=$((40 * $2))
DICT_DIR=$3
FONT_DIR=$4
OUTPUT_DIR=$5 

echo "Generate Patch $COUNT_B3 dict: $DICT_DIR font: $FONT_DIR output: $OUTPUT_DIR"
for ((i=11; i<=60; i++))
do 
    python ./trdg/run.py -l $LANG -w 1 -c ${COUNT_B3} -f ${i} -cs 3 -b 3 --fit --margins 2,2,2,2 -tc '#000000,#888888' --dict $DICT_DIR -fd $FONT_DIR   --output_dir $OUTPUT_DIR/${i}_m2_b3
    python ./trdg/run.py -l $LANG -w 1 -c ${COUNT_BO} -f ${i} -cs 3 -b 2 --fit --margins 2,2,2,2 -tc '#000000,#888888' --dict $DICT_DIR -fd $FONT_DIR   --output_dir $OUTPUT_DIR/${i}_m2_b2
    python ./trdg/run.py -l $LANG -w 1 -c ${COUNT_BO} -f ${i} -cs 3 -b 1 --fit --margins 2,2,2,2 -tc '#000000,#888888' --dict $DICT_DIR -fd $FONT_DIR   --output_dir $OUTPUT_DIR/${i}_m2_b1
    python ./trdg/run.py -l $LANG -w 1 -c ${COUNT_BO} -f ${i} -cs 3 -b 0 --fit --margins 2,2,2,2 -tc '#000000,#888888' --dict $DICT_DIR -fd $FONT_DIR   --output_dir $OUTPUT_DIR/${i}_m2_b0
done 


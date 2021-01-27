#!/bin/bash
LANG=$1
COUNT_B3=$((80 * $2))
COUNT_BO=$((40 * $2))
DICT_DIR=$3
FONT_DIR=$4
OUTPUT_DIR=$5 

echo "Generate Patch ${COUNT_B3} dict: ${DICT_DIR} font: ${FONT_DIR} output: ${OUTPUT_DIR}"

for ((i=11; i<=60; i++))
do 
    python ./trdg/run.py -l $LANG -w 1 -c $COUNT_B3 -f ${i}  -b 3 --margins 0,0,0,0 -tc '#000000,#888888' --dict $DICT_DIR -fd $FONT_DIR  --output_dir $OUTPUT_DIR/f${i}_m0_b3 
    python ./trdg/run.py -l $LANG -w 1 -c $COUNT_BO -f ${i}  -b 2 --margins 0,0,0,0 -tc '#000000,#888888' --dict $DICT_DIR -fd $FONT_DIR  --output_dir $OUTPUT_DIR/f${i}_m0_b2 
    python ./trdg/run.py -l $LANG -w 1 -c $COUNT_BO -f ${i}  -b 1 --margins 0,0,0,0 -tc '#000000,#888888' --dict $DICT_DIR -fd $FONT_DIR  --output_dir $OUTPUT_DIR/f${i}_m0_b1 
    python ./trdg/run.py -l $LANG -w 1 -c $COUNT_BO -f ${i}  -b 3 --margins 0,0,0,0 -tc '#000000,#888888' --dict $DICT_DIR -fd $FONT_DIR  --output_dir $OUTPUT_DIR/f${i}_m0_b0 
done 
#!/bin/bash
LANG=$1
COUNT_B3=$((80 * $2))
COUNT_BO=$((40 * $2))
DICT_DIR=$3
FONT_DIR=$4
OUTPUT_DIR=$5 

echo "Generate Patch $COUNT_B3 dict: $DICT_DIR font: $FONT_DIR output: $OUTPUT_DIR"

for ((i=16; i <= 20;i++))
do  
    python ./trdg/run.py -l $LANG -w 1 -c $COUNT_B3 -f ${i} -d 3 -b 3 --margins 1,1,1,1 -tc '#000000,#888888' --dict $DICT_DIR -fd $FONT_DIR   --output_dir $OUTPUT_DIR/f${i}_m1_b3
    python ./trdg/run.py -l $LANG -w 1 -c $COUNT_BO -f ${i} -d 3 -b 2 --margins 1,1,1,1 -tc '#000000,#888888' --dict $DICT_DIR -fd $FONT_DIR   --output_dir $OUTPUT_DIR/f${i}_m1_b2
    python ./trdg/run.py -l $LANG -w 1 -c $COUNT_BO -f ${i} -d 3 -b 1 --margins 1,1,1,1 -tc '#000000,#888888' --dict $DICT_DIR -fd $FONT_DIR   --output_dir $OUTPUT_DIR/f${i}_m1_b1
    python ./trdg/run.py -l $LANG -w 1 -c $COUNT_BO -f ${i} -d 3 -b 0 --margins 1,1,1,1 -tc '#000000,#888888' --dict $DICT_DIR -fd $FONT_DIR   --output_dir $OUTPUT_DIR/f${i}_m1_b0
done

for ((i=21; i <= 65;i++))
do  
    python ./trdg/run.py -l $LANG -w 1 -c $COUNT_B3 -f ${i} -bl 1 -d 3  -b 3 --margins 1,1,1,1 -tc '#000000,#888888' --dict $DICT_DIR -fd $FONT_DIR   --output_dir $OUTPUT_DIR/f${i}}_m1_b3 
    python ./trdg/run.py -l $LANG -w 1 -c $COUNT_BO -f ${i} -bl 1 -d 3  -b 2 --margins 1,1,1,1 -tc '#000000,#888888' --dict $DICT_DIR -fd $FONT_DIR   --output_dir $OUTPUT_DIR/f${i}}_m1_b2 
    python ./trdg/run.py -l $LANG -w 1 -c $COUNT_BO -f ${i} -bl 1 -d 3  -b 1 --margins 1,1,1,1 -tc '#000000,#888888' --dict $DICT_DIR -fd $FONT_DIR   --output_dir $OUTPUT_DIR/f${i}}_m1_b1 
    python ./trdg/run.py -l $LANG -w 1 -c $COUNT_BO -f ${i} -bl 1 -d 3  -b 0 --margins 1,1,1,1 -tc '#000000,#888888' --dict $DICT_DIR -fd $FONT_DIR   --output_dir $OUTPUT_DIR/f${i}}_m1_b0 

done
#!/bin/bash
LANG=$1
COUNT_B3=$((80 * $2))
COUNT_BO=$((40 * $2))
DICT_DIR=$3
FONT_DIR=$4
OUTPUT_DIR=$5 

echo "Generate Patch ${COUNT_B3} dict: ${DICT_DIR} font: ${FONT_DIR} output: ${OUTPUT_DIR}"
for ((i=21; i<=70; i++))
do 
    python ./trdg/run.py -l $LANG -w 1 -c ${COUNT_B3} -f ${i}  -d 3 -k 1 -rk  -bl 1 -rbl  -b 3 --margins 2,2,2,2 -tc '#000000,#888888' --dict ${DICT_DIR} -fd ${FONT_DIR}   --output_dir ${OUTPUT_DIR}/f${i}_m2_b3 
    python ./trdg/run.py -l $LANG -w 1 -c ${COUNT_BO} -f ${i}  -d 3 -k 1 -rk  -bl 1 -rbl  -b 2 --margins 2,2,2,2 -tc '#000000,#888888' --dict ${DICT_DIR} -fd ${FONT_DIR}   --output_dir ${OUTPUT_DIR}/f${i}_m2_b2
    python ./trdg/run.py -l $LANG -w 1 -c ${COUNT_BO} -f ${i}  -d 3 -k 1 -rk  -bl 1 -rbl  -b 1 --margins 2,2,2,2 -tc '#000000,#888888' --dict ${DICT_DIR} -fd ${FONT_DIR}   --output_dir ${OUTPUT_DIR}/f${i}_m2_b1
    python ./trdg/run.py -l $LANG -w 1 -c ${COUNT_BO} -f ${i}  -d 3 -k 1 -rk  -bl 1 -rbl  -b 0 --margins 2,2,2,2 -tc '#000000,#888888' --dict ${DICT_DIR} -fd ${FONT_DIR}   --output_dir ${OUTPUT_DIR}/f${i}_m2_b0
done
    

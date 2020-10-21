#!/bin/bash

N_INPUT_FOLDERS=10

for folder in {1..10}
do
    INPUT=/Users/romanzhydyk/Desktop/MEI/projeto/newdata/inputs/input$folder/*
    OUTPUT=/Users/romanzhydyk/Desktop/MEI/projeto/newdata/outputs/
    PROBABILITY_VARIATION=0.1
    PROBABILITY_MAX=0.95
    
    for file in $INPUT
    do
        var=$(echo $file | cut -d"_" -f2 | cut -d"." -f1)
        line=$(head -n 1 $file)
        probability=$(echo $line | cut -d" " -f1)
        while  [ "$(bc <<< "$probability < $PROBABILITY_MAX")" == "1" ]
        do
            mkdir -p ${OUTPUT}bubble/${probability}/output$folder/
            ./bubble <<< $line > "${OUTPUT}bubble/${probability}/output$folder/data_${var}.out"
            mkdir -p ${OUTPUT}insertion/${probability}/output$folder/
            ./insertion <<< $line >  "${OUTPUT}insertion/${probability}/output$folder/data_${var}.out"
            mkdir -p ${OUTPUT}merge/${probability}/output$folder/
            ./merge <<< $line >  "${OUTPUT}merge/${probability}/output$folder/data_${var}.out"
            mkdir -p ${OUTPUT}quick/${probability}/output$folder/
            ./quick <<< $line >  "${OUTPUT}quick/${probability}/output$folder/data_${var}.out"
            last_prob=$probability
            probability=`echo $probability + $PROBABILITY_VARIATION | bc | awk '{printf "%f", $0}'`
            line=${line/$last_prob/$probability}
        done
    done
done
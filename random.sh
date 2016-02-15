#!/bin/bash
ranwd="usr/share/dict/words"
ranwd1=$(cat $ranwd | wc -l)
ranwd2=$((RANDOM %$ranwd1))
ranwd3=$(sed ''$ranwd2'q;d' $ranwd)











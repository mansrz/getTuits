#!/bin/bash

HT=$1
SINCE=$2
UNTIL=$3
MAX_RESULTS=$4

snscrape --jsonl --progress --max-results $MAX_RESULTS --since $SINCE twitter-search "$HT until:$UNTIL" > $HT.json
python parse_json.py $HT.json

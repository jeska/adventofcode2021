#!/bin/zsh

DAY=$1
DAY_STR=day${1}

cp -R template/dayN "${DAY_STR}"
cd "${DAY_STR}"
mv dayN-sample.txt "${DAY_STR}"-sample.txt
mv dayN-full.txt "${DAY_STR}"-full.txt
mv dayN-pt1.py "${DAY_STR}"-pt1.py
mv dayN-pt2.py "${DAY_STR}"-pt2.py

sed -i '' "s/dayN/${DAY_STR}/g" "${DAY_STR}"-pt*.py
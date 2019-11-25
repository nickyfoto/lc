#!/bin/bash

inputs=('[1,2,3,1]' '[2,7,9,3,1]' '[2,1,1,2]')
# leetcode test 198.house-robber.py -t '[1,2,3,1]'
# sleep 5
# leetcode test 198.house-robber.py -t '[2,7,9,3,1]'
# sleep 5
# leetcode test 198.house-robber.py -t '[2,1,1,2]'

for i in "${inputs[@]}"
do
    leetcode test 198.house-robber.py -t $i
    sleep 5
done
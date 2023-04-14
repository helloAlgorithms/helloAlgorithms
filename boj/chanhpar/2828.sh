#!/bin/bash

declare -i width
declare -i basketWidth
declare -i basketPos
declare -i totalDist
declare -i dist
declare -i appleNum
declare -i applePos

read -r width basketWidth
read -r appleNum

totalDist=0
basketPos=1
while [ $appleNum -gt 0 ]
do
    read -r applePos
    appleNum=--appleNum
    if [ $(( $basketPos + $basketWidth - 1 )) -lt $applePos ]
    then
        dist=$(( $applePos - $basketPos - $basketWidth + 1 ))
        totalDist+=$dist
        basketPos+=$dist
    elif [ $basketPos -gt $applePos ]
    then
        dist=$(( $basketPos - $applePos ))
        totalDist+=$dist
        basketPos=$(( $basketPos - $dist ))
    fi
done

echo $totalDist

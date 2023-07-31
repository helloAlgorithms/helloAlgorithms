IFS= ; read -r a; b=1; while [ $b -le $a ]; do read -r c; echo "$b. $c"; b=$((b+1)); done

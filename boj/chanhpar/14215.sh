read -r a b c

if [ $a -gt $b ];
then
    t=$a
    a=$b
    b=$t
fi
if [ $a -gt $c ];
then
    t=$a
    a=$c
    c=$t
fi
if [ $b -gt $c ];
then
    t=$b
    b=$c
    c=$t
fi

if [ $((a + b)) -gt $c ];
then
    echo $((a + b + c))
else
    echo $((2 * (a + b) - 1))
fi

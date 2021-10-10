#!/bin/bash
src=$1
dst=$2

if [ $# != 2 ]; then
    echo "Need two inputs, in the form: ./move.sh source destination"; exit 1
fi

if [[ "$src" != /* ]]; then
    fullsrc=$(readlink -f $src)
fi
if [[ "$dst" != /* ]]; then
    fulldst=$(readlink -f $dst)
fi


if [ ! -d $fullsrc ]; then
    echo "Source directory does not exists."; exit 1
elif [ ! -d $fulldst ]; then
    echo "Destination directory does not exists."; exit 1
fi


cp -r $src $dst
rm -i -r $src
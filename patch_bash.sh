#!/bin/bash


#get version number
one=$(bash --version | grep 'version [0-9]\.' | awk '{print $4}' | awk -F'.' '{print $1}')
tow=$(bash --version | grep 'version [0-9]\.' | awk '{print $4}' | awk -F'.' '{print $2}')

wget http://ftp.gnu.org/gnu/bash/bash-${one}.${tow}.tar.gz

#get now
curl -o bash.html http://ftp.gnu.org/gnu/bash/bash-${one}.${tow}-patches/
max=$(cat bash.html |grep '<a href=\"bash[[:alnum:]]' | awk -F'=' '{print $4}' | awk -F'>' '{print $1}' | grep -v 'sig' | wc -l)



for i in $(seq -f "%03g" 1 $max );
do
echo "Getting ... http://ftp.gnu.org/gnu/bash/bash-${one}.${tow}-patches/bash${one}${tow}-$i";
curl "http://ftp.gnu.org/gnu/bash/bash-${one}.${tow}-patches/bash${one}${tow}-$i"
#| patch -p0 ;

done

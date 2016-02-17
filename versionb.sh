b=$1
date=$(date +"%y-%m-%d")
file=$(echo $b | cut -d'.' -f1)
ext=$(echo $b | cut -d'.' -f2)
vijay="$file""_"$date".""$ext"
cp $b $vijay


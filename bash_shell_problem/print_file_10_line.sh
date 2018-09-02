#three methods
sed -n 10p file.txt
awk '{if(NR==10){print $0}}' file.txt
tail -n +10 file.txt | head -n 1

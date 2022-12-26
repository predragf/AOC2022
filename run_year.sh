clear;
echo "***Advent of Code 2022 solutions by Predrag Filipovikj***"
echo ""
for i in $(ls -d */); do
    cd ./"$i"    
    time python ./solution.py
    echo ""
    cd ..
done
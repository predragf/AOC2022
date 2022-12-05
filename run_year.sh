clear;
echo "***Advent of Code 2022 solutions by Predrag Filipovikj***"
echo ""
for i in $(ls -d */); do
    cd ./"$i"    
    python ./solution.py
    cd ..
done
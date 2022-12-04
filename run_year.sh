clear;
for i in $(ls -d */); do
    cd ./"$i"    
    python ./solution.py
    cd ..
done
for i in $(ls -d */); do
    cd ./"$i"
    echo $(pwd)
    python ./solution.py
    cd ..
done
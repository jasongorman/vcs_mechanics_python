git add .
python -m unittest discover test && git commit -m %1% || git reset --hard
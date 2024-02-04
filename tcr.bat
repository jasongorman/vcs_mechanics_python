echo %1
git add .
python -m unittest discover test && git commit -a -m %1% || git reset --hard
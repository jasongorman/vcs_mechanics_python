set message = %1
git add .
echo %message%
python -m unittest discover test && git commit -a -m "Passes!" || git reset --hard
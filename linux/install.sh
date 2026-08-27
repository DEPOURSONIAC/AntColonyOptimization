#!/bin/bash


cd ../..

pip3 install pyinstaller
python3 -m PyInstaller --onefile --name ACO --icon=assets/logo.png --distpath releases/linux --workpath build/linux --specpath build main.py

chmod +x releases/linux/ACO

rm -rf build

echo "ACO a été installé avec succès."
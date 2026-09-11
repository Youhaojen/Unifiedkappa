#!/bin/bash
set -e # Exit immediately if a command exits with a non-zero status.

conda create -n unifiedkappa python=3.10 -y
conda activate unifiedkappa

if [ -f "revised-phonopy.zip" ]; then
    unzip -o revised-phonopy.zip
    cd revised-phonopy
    pip install .
    cd ..
else
    echo "Can not find revised-phonopy.zip"
    exit 1
fi

echo ">>> Installing unifiedkappa..."
pip install .

echo ">>> Installation complete!"
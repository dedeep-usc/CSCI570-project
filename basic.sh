# Shell script to run inefficient version of the algorithm

set -e

export PYTHONPATH=$PYTHONPATH:$(pwd)
python3 final_basic.py input.txt

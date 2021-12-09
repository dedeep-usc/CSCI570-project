# Shell script to run efficient version of the algorithm

set -e

export PYTHONPATH=$PYTHONPATH:$(pwd)
python3 final_efficient.py input.txt
# Shell script to run inefficient version of the algorithm

set -e
default_input_filename="input.txt"
if [ "$#" -eq 0 ]; then
  echo "Using input.txt as the input file"
  echo "To give custom input file run: ./basic.sh <filename.txt>"
else
  echo "Using " $1 "as the input file"
fi
  export PYTHONPATH=$PYTHONPATH:$(pwd)
  python3 final_basic.py ${1:-$default_input_filename}

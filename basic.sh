# Shell script to run inefficient version of the algorithm

set -e
if [ "$#" -ne 1 ]; then
  echo "Usage: ./basic.sh input.txt" 
  exit 1
fi
  export PYTHONPATH=$PYTHONPATH:$(pwd)
  python3 final_basic.py $1

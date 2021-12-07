# Shell script to run efficient version of the algorithm

set -e
if [ "$#" -ne 1 ]; then
  echo "Usage: ./efficient.sh input.txt" 
  exit 1
fi
  export PYTHONPATH=$PYTHONPATH:$(pwd)
  python3 final_efficient.py $1
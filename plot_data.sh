# Shell script to run data plotter

set -e

export PYTHONPATH=$PYTHONPATH:$(pwd)
python3 plot_data.py
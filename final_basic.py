from inefficient import InefficientSeqAlignment
from input_generator import input_generator
import argparse
import time
import tracemalloc

parser = argparse.ArgumentParser() 
parser.add_argument("--file", "-f", type=str, required=True)
args = parser.parse_args()

str1, str2 = input_generator(args.file)

ineff = InefficientSeqAlignment()

ineff_time_start = time.time()
tracemalloc.start()
first_seq_ineff, second_seq_ineff, cost_ineff = ineff.find_min_cost(str1, str2)
ineff_current, ineff_peak = tracemalloc.get_traced_memory()
ineff_time_end = time.time()
ineff_time = ineff_time_end - ineff_time_start
ineff_max_mem = ineff_peak / 10**3
tracemalloc.stop()

op_string1 = first_seq_ineff if len(first_seq_ineff)<=50 else first_seq_ineff[:50] + " " + first_seq_ineff[-50:]
op_string2 = second_seq_ineff if len(second_seq_ineff)<=50 else second_seq_ineff[:50] + " " + second_seq_ineff[-50:]

INEFF_OP = """{}
{}
{}
{}
{}
"""

INEFF_OP = INEFF_OP.format(
		op_string1,
		op_string2,
		float(cost_ineff),
		float(ineff_time),
		float(ineff_max_mem)
	)

f = open("output_ineff.txt", "w")

f.write(INEFF_OP)

f.close()

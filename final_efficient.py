from main.divide_conquer import DivideConquerSeqAlignment
from main.inefficient import InefficientSeqAlignment
from main.efficient import EfficientSeqAlignment
from main.input_generator import input_generator
import argparse
import time
import tracemalloc

parser = argparse.ArgumentParser() 
parser.add_argument("file", type=str)
args = parser.parse_args()

str1, str2 = input_generator(args.file)

eff = EfficientSeqAlignment()
ineff = InefficientSeqAlignment()
div_conq = DivideConquerSeqAlignment(eff, ineff)

ineff_start = time.time()
div_conq_time_start = time.time()
tracemalloc.start()
first_seq_div, second_seq_div, cost_div = div_conq.div_conq_alignment(str1, str2)
div_current, div_peak = tracemalloc.get_traced_memory()
div_conq_time_end = time.time()
div_conq_time = div_conq_time_end - div_conq_time_start
div_conq_max_mem = div_peak / 10**3
tracemalloc.stop()

DIV_CONQ_OP = """{}
{}
{}
{}
{}
"""

op_string1 = first_seq_div + ' ' + first_seq_div if len(first_seq_div)<=50 else first_seq_div[:50] + " " + first_seq_div[-50:]
op_string2 = second_seq_div + ' ' + second_seq_div if len(second_seq_div)<=50 else second_seq_div[:50] + " " + second_seq_div[-50:]

DIV_CONQ_OP = DIV_CONQ_OP.format(
		op_string1,
		op_string2,
		float(cost_div),
		float(div_conq_time),
		float(div_conq_max_mem)
	)

f = open("output_eff.txt", "w")

f.write(DIV_CONQ_OP)

f.close()

f = open("./data/data_efficient.txt", "a")

data_str = "{},{},{}\n".format(len(first_seq_div)*len(second_seq_div), div_conq_time, div_conq_max_mem)

f.write(data_str)

f.close()

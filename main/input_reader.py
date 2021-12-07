from divide_conquer import DivideConquerSeqAlignment
from inefficient import InefficientSeqAlignment
from efficient import EfficientSeqAlignment
from input_generator import input_generator
import argparse
import csv 
import time

parser = argparse.ArgumentParser() 
parser.add_argument("--file", "-f", type=str, required=True)
args = parser.parse_args()

str1, str2 = input_generator(args.file)

print("str1: {}".format(str1))
print("str2: {}".format(str2))

eff = EfficientSeqAlignment()
ineff = InefficientSeqAlignment()
div_conq = DivideConquerSeqAlignment(eff, ineff)

ineff_time_start = time.time()
tracemalloc.start()
first_seq_ineff, second_seq_ineff, cost_ineff = ineff.find_min_cost(str1, str2)
ineff_current, ineff_peak = tracemalloc.get_traced_memory()
ineff_time_end = time.time()
ineff_time = ineff_time_end - ineff_time_start
ineff_max_mem = ineff_peak / 10**3
tracemalloc.stop()

ineff_start = time.time()
div_conq_time_start = time.time()
tracemalloc.start()
first_seq_div, second_seq_div, cost_div = div_conq.div_conq_alignment(str1, str2)
div_current, div_peak = tracemalloc.get_traced_memory()
div_conq_time_end = time.time()
div_conq_time = div_conq_time_end - div_conq_time_start
div_conq_max_mem = div_peak / 10**3
tracemalloc.stop()


DIV_CONQ_OP = """
{}
{}
{}
{}
"""

op_string1 = first_seq_div if len(first_seq_div)<=50 else first_seq_div[:50] + " " + first_seq_div[-50:]
op_string2 = second_seq_div if len(second_seq_div)<=50 else second_seq_div[:50] + " " + second_seq_div[-50:]

DIV_CONQ_OP = DIV_CONQ_OP.format(
		op_string1,
		op_string2,
		div_conq_time,
		div_conq_max_mem
	)

INEFF_OP = """
{}
{}
{}
{}
"""



op_string1 = first_seq_ineff if len(first_seq_ineff)<=50 else first_seq_ineff[:50] + " " + first_seq_ineff[-50:]
op_string2 = second_seq_ineff if len(second_seq_ineff)<=50 else second_seq_ineff[:50] + " " + second_seq_ineff[-50:]

INEFF_OP = INEFF_OP.format(
		op_string1,
		op_string2,
		ineff_time,
		ineff_max_mem
	)


print("divide_conquer: {}".format(DIV_CONQ_OP))

print("ineff: {}".format(INEFF_OP))

print("cost: {}".format(cost_ineff))


f = open("output_ineff.txt", "w")

f.write(INEFF_OP)

f.close()

f = open("output_eff.txt", "w")

f.write(DIV_CONQ_OP)

f.close()







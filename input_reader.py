from divide_conquer import DivideConquerSeqAlignment
from inefficient import InefficientSeqAlignment
from efficient import EfficientSeqAlignment
from input_generator import input_generator
import argparse
import csv 
import time
from memory_profiler import memory_usage

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
first_seq_ineff, second_seq_ineff, cost_ineff = ineff.find_min_cost(str1, str2)
ineff_time_end = time.time()
ineff_time = ineff_time_end - ineff_time_start


div_conq_time_start = time.time()
first_seq_div, second_seq_div, cost_div = div_conq.div_conq_alignment(str1, str2)
div_conq_time_end = time.time()
div_conq_time = div_conq_time_end - div_conq_time_start

div_conq_max_mem = 0
ineff_max_mem = 0



DIV_CONQ_OP = """
{}
{}
{}
{}
"""

op_string1 = first_seq_div if len(first_seq_div)<=100 else first_seq_div[:50] + first_seq_div[-50:]
op_string2 = second_seq_div if len(second_seq_div)<=100 else second_seq_div[:50] + second_seq_div[-50:]

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

if __name__ == "__main__":
	div_conq_max_mem = max(memory_usage((div_conq.div_conq_alignment, (str1, str2,))))
	ineff_max_mem = max(memory_usage((ineff.find_min_cost, (str1, str2,))))

op_string1 = first_seq_ineff[:50] + " space " + first_seq_ineff[-50:]
op_string2 = second_seq_ineff[:50] + " space " + second_seq_ineff[-50:]

INEFF_OP = INEFF_OP.format(
		op_string1,
		op_string2,
		ineff_time,
		ineff_max_mem
	)


print("divide_conquer: {}".format(DIV_CONQ_OP))

print("ineff: {}".format(INEFF_OP))

print("cost: {}".format(cost_ineff))


f = open("output.txt", "w")

f.write(INEFF_OP)

f.close()









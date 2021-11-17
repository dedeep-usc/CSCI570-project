from divide_conquer import DivideConquerSeqAlignment
from inefficient import InefficientSeqAlignment
from efficient import EfficientSeqAlignment
from input_generator import input_generator
import argparse
import csv  

parser = argparse.ArgumentParser() 
parser.add_argument("--file", "-f", type=str, required=True)
args = parser.parse_args()

str1, str2 = input_generator(args.file)

eff = EfficientSeqAlignment()
ineff = InefficientSeqAlignment()
div_conq = DivideConquerSeqAlignment(eff, ineff)

first_seq_ineff, second_seq_ineff, cost_ineff = ineff.find_min_cost(str1, str2)
first_seq_div, second_seq_div, cost_div = div_conq.div_conq_alignment(str1, str2)


print("_____________________")

print('first sequence: \n inefficient_solution: {} \n divide_conquer: {}'.format(first_seq_ineff, first_seq_div))
print('Second sequence: \n inefficient_solution: {} \n divide_conquer: {}'.format(second_seq_ineff, second_seq_div))

print('Cost equality: {}'.format(cost_ineff == cost_div))
print('first sequence: equality: {}'.format(first_seq_ineff == first_seq_div))
print('second sequence: equality: {}'.format(second_seq_ineff == second_seq_div))

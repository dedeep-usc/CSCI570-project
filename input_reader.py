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

inefficient_solution = ineff.find_min_cost(str1, str2)
divide_conquer_solution = div_conq.div_conq_alignment(str1, str2)

print(inefficient_solution)
print(divide_conquer_solution)
print(inefficient_solution == divide_conquer_solution)
import random

from inefficient import InefficientSeqAlignment
from efficient import EfficientSeqAlignment
from divide_conquer import DivideConquerSeqAlignment

a = ["A", "C", "G", "T"]
str1 = ""
str2 = ""
for i in range(200):
	str1 += a[random.randint(0, 3)]

for i in range(200):
	str2 += a[random.randint(0, 3)]

ineff = InefficientSeqAlignment()
eff = EfficientSeqAlignment()

div_conq_alignment = DivideConquerSeqAlignment(eff=eff, ineff=ineff)

first_seq_div, second_seq_div, cost_div = div_conq_alignment.div_conq_alignment(str1, str2)
first_seq_ineff, second_seq_ineff, cost_ineff = ineff.find_min_cost(str1, str2)

print("div_score: {}, ineff_score: {}, same: {}".format(cost_div, cost_ineff, cost_div == cost_ineff))

print("first_seq same: {}".format(first_seq_div == first_seq_ineff))

print("second_seq_same: {}".format(second_seq_div == second_seq_ineff))


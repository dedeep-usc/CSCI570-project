import random

from inefficient import InefficientSeqAlignment
from efficient import EfficientSeqAlignment
from divide_conquer import DivideConquerSeqAlignment

a = ["A", "C", "G", "T"]
str1 = ""
str2 = ""
for i in range(10):
	str1 += a[random.randint(0, 3)]

for i in range(10):
	str2 += a[random.randint(0, 3)]

ineff = InefficientSeqAlignment()
eff = EfficientSeqAlignment()

div_conq_alignment = DivideConquerSeqAlignment(eff=eff, ineff=ineff)

div_ans = div_conq_alignment.div_conq_alignment(str1, str2)
ineff_ans = ineff.find_min_cost(str1, str2)

print("div_ans: {}".format(div_ans))
print("ineff_ans: {}".format(ineff_ans))

print("ans: {}".format(ineff_ans == div_ans))




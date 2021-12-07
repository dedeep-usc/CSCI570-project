import random
import tracemalloc

from inefficient import InefficientSeqAlignment
from efficient import EfficientSeqAlignment
from divide_conquer import DivideConquerSeqAlignment

a = ["A", "C", "G", "T"]
str1 = ""
str2 = ""
for i in range(500):
	str1 += a[random.randint(0, 3)]

for i in range(500):
	str2 += a[random.randint(0, 3)]


# str1 = "ACACTGACTACTGACTGGTGACTACTGACTGGGGGGCCATAT"
# str2 = "TATTATACGCTATTATACGCGACGCGGACGCG"
ineff = InefficientSeqAlignment()
eff = EfficientSeqAlignment()

div_conq_alignment = DivideConquerSeqAlignment(eff=eff, ineff=ineff)

tracemalloc.start()
first_seq_div, second_seq_div, cost_div = div_conq_alignment.div_conq_alignment(str1, str2)
current, peak = tracemalloc.get_traced_memory()
print(f"Peak for divide conquer was {peak / 10**6}MB")
tracemalloc.stop()


tracemalloc.start()
first_seq_ineff, second_seq_ineff, cost_ineff = ineff.find_min_cost(str1, str2)
current, peak = tracemalloc.get_traced_memory()
print(f"Peak for inefficient was {peak / 10**6}MB")
tracemalloc.stop()



print("div_score: {}, ineff_score: {}, same: {}".format(cost_div, cost_ineff, cost_div == cost_ineff))

print("first_seq same: {}".format(first_seq_div == first_seq_ineff))

print("second_seq_same: {}".format(second_seq_div == second_seq_ineff))

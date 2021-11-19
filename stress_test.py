import random

from inefficient import InefficientSeqAlignment
from efficient import EfficientSeqAlignment
from divide_conquer import DivideConquerSeqAlignment


ineff = InefficientSeqAlignment()
eff = EfficientSeqAlignment()
div_conq_alignment = DivideConquerSeqAlignment(eff=eff, ineff=ineff)

same_cost = 0
diff_cost = 0

first_seq_same = 0
first_seq_not_same = 0

second_seq_same = 0
second_seq_not_same = 0

def test_the_fuck_out_of_it(str1_len, str2_len):
	global same_cost
	global diff_cost
	global first_seq_same
	global first_seq_not_same
	global second_seq_same
	global second_seq_not_same

	a = ["A", "C", "G", "T"]
	str1 = ""
	str2 = ""

	for i in range(str1_len):
		str1 += a[random.randint(0, 3)]

	for i in range(str2_len):
		str2 += a[random.randint(0, 3)]

	first_seq_div, second_seq_div, cost_div = div_conq_alignment.div_conq_alignment(str1, str2)
	first_seq_ineff, second_seq_ineff, cost_ineff = ineff.find_min_cost(str1, str2)
	# cost_eff = eff.find_min_cost(str1, str2, return_cost=True)

	if cost_div == cost_ineff:
		same_cost += 1
	else:
		diff_cost += 1

	if len(first_seq_div) == len(first_seq_ineff):
		first_seq_same += 1
	else:
		first_seq_not_same += 1

	if len(second_seq_div) == len(second_seq_ineff):
		second_seq_same += 1
	else:
		second_seq_not_same += 1

n = 1000

for i in range(n):
	str1_len = random.randint(0, 500)
	str2_len = random.randint(0, 500)
	test_the_fuck_out_of_it(str1_len, str2_len)

same_cost_perc = same_cost / n * 100
diff_cost_perc = diff_cost / n * 100

same_first_seq_perc = first_seq_same / n * 100
diff_first_seq_perc = first_seq_not_same / n * 100

same_second_seq_perc = second_seq_same / n * 100
diff_second_seq_perc = second_seq_not_same / n * 100

print("total no of test cases: {}".format(n))
print("--------------------------------------------------")
print("same cost count: {}, same cost perc: {}".format(same_cost, same_cost_perc))
print("diff cost count: {}, diff cost perc: {}".format(diff_cost, diff_cost_perc))
print("--------------------------------------------------")
print("same first seq count: {}, same first seq perc: {}".format(first_seq_same, same_first_seq_perc))
print("diff first seq count: {}, diff first seq perc: {}".format(first_seq_not_same, diff_first_seq_perc))
print("--------------------------------------------------")
print("same second seq count: {}, same second seq perc: {}".format(second_seq_same, same_second_seq_perc))
print("diff second seq count: {}, diff second seq perc: {}".format(second_seq_not_same, diff_second_seq_perc))






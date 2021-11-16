import random

import inefficient as in_eff
import efficient as eff
import divide_conquer as div_con


a = ["A", "C", "G", "T"]
str1 = ""
str2 = ""
for i in range(2000):
	str1 += a[random.randint(0, 3)]

for i in range(2000):
	str2 += a[random.randint(0, 3)]

# print("divide_conquer: {}".format(div_con.div_conq_alignment("ACGT", "TGCA")))

# print("inefficient: {}".format(in_eff.find_min_cost("ACGT", "TGCA")))


print("str1: {}, str2: {}".format(str1, str2))
div_ans = div_con.div_conq_alignment(str1, str2)
print("divide_conquer: {}".format(div_ans))


ineff_ans = in_eff.find_min_cost(str1, str2)
print("inefficient: {}".format(ineff_ans))

print("ans: {}".format(ineff_ans == div_ans))

# in_eff.find_min_cost(str1, str2)
# print("------------")
# eff.find_min_cost(str1, str2)

from inefficient import *

ineff = InefficientSeqAlignment()


first_seq, second_seq, cost = ineff.find_min_cost("AGGCGCTATATAT", "TCGCGAGAGAGACTC")

print("first_seq: {}".format(first_seq))
print("second_seq: {}".format(second_seq))
print("cost: {}".format(cost))
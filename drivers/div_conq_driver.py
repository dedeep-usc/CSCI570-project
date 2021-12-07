from main.inefficient import InefficientSeqAlignment
from main.efficient import EfficientSeqAlignment
from main.divide_conquer import DivideConquerSeqAlignment

ineff = InefficientSeqAlignment()
eff = EfficientSeqAlignment()

div_conq_alignment = DivideConquerSeqAlignment(eff=eff, ineff=ineff)

str1 = "AGGCGCTATATAT"
str2 = "TCGCGAGAGAGACTC"

first_seq_div, second_seq_div, cost_div = div_conq_alignment.div_conq_alignment(str1, str2)

if __name__ ==  '__main__':
	pass
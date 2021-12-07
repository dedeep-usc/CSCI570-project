from inefficient import InefficientSeqAlignment
from efficient import EfficientSeqAlignment
from divide_conquer import DivideConquerSeqAlignment

from memory_profiler import memory_usage

mem_str1 = ""
mem_str2 = ""

ineff = InefficientSeqAlignment()
eff = EfficientSeqAlignment()

div_conq_alignment = DivideConquerSeqAlignment(eff=eff, ineff=ineff)

if __name__ ==  '__main__':
	
	main()

def test(mem_usage):
	print(max(mem_usage((div_conq_alignment.div_conq_alignment, (mem_str1, mem_str2,)))))
	print(max(mem_usage((ineff.find_min_cost, (mem_str1, mem_str2,)))))

# def get_memory(str1, str2):
# 	print(max(memory_usage((div_conq_alignment.div_conq_alignment, (str1, str2,)))))
# 	print(max(memory_usage((ineff.find_min_cost, (str1, str2,)))))

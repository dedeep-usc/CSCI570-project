import random
import time
from memory_profiler import memory_usage
import matplotlib.pyplot as plt
import tracemalloc

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

def test_the_fuck_out_of_it(str1_len, str2_len, df):
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

	# breakpoint()
	tracemalloc.start()
	div_start = time.time()
	first_seq_div, second_seq_div, cost_div = div_conq_alignment.div_conq_alignment(str1, str2)
	div_end = time.time()
	div_current, div_peak = tracemalloc.get_traced_memory()
	div_conq_max_mem = div_peak / 10**6
	div_time = div_end - div_start
	# breakpoint()
	tracemalloc.stop()

	tracemalloc.start()
	ineff_start = time.time()
	first_seq_ineff, second_seq_ineff, cost_ineff = ineff.find_min_cost(str1, str2)
	ineff_end = time.time()
	ineff_current, ineff_peak = tracemalloc.get_traced_memory()
	ineff_max_mem = ineff_peak / 10**6
	ineff_time = ineff_end - ineff_start
	tracemalloc.stop()

	df['size'].append(str1_len+str2_len)
	df['ineff_time'].append(ineff_time)
	df['div_time'].append(div_time)
	df['ineff_memory_usage'].append(ineff_max_mem)
	df['div_memory_usage'].append(div_conq_max_mem)


n = 500
df = {'size':[], 'ineff_time': [], 'div_time':[], 'ineff_memory_usage':[], 'div_memory_usage':[]}


for i in range(1, 5001, 10 ):
	str1_len = str2_len = i

	test_the_fuck_out_of_it(str1_len, str2_len, df)

# test_the_fuck_out_of_it(100, 100, df)
# test_the_fuck_out_of_it(500, 500, df)

print(len(df['size']))

print(df)

def plot_dict(df, x, y):
	plt.plot(df[x], df[y], linestyle='solid',)
	plt.title(x.split('_', 1)[0])
	plt.xlabel(x.split('_', 1)[1])
	plt.ylabel(y)

	plt.savefig('{}-{}.png'.format(x, y))
	plt.clf()



plot_dict(df, 'ineff_time', 'size')
plot_dict(df,  'ineff_memory_usage','size')
plot_dict(df, 'div_time', 'size')
plot_dict(df, 'div_memory_usage', 'size')


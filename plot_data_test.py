import random
import time
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

def generate_data(str1_len, str2_len, df):
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
	div_conq_max_mem = div_peak / 10**3
	div_time = div_end - div_start
	# breakpoint()
	tracemalloc.stop()

	tracemalloc.start()
	ineff_start = time.time()
	first_seq_ineff, second_seq_ineff, cost_ineff = ineff.find_min_cost(str1, str2)
	ineff_end = time.time()
	ineff_current, ineff_peak = tracemalloc.get_traced_memory()
	ineff_max_mem = ineff_peak / 10**3
	ineff_time = ineff_end - ineff_start
	tracemalloc.stop()

	df['size'].append(len(first_seq_ineff)*len(second_seq_ineff))
	# df['size'].append(len(str1)+len(str2))
	df['ineff_time'].append(ineff_time)
	df['div_time'].append(div_time)
	df['ineff_memory_usage'].append(ineff_max_mem)
	df['div_memory_usage'].append(div_conq_max_mem)


n = 500
df = {'size':[], 'ineff_time': [], 'div_time':[], 'ineff_memory_usage':[], 'div_memory_usage':[]}


for i in range(1, 1001, 100):
	str1_len = str2_len = i

	generate_data(str1_len, str2_len, df)


print(len(df['size']))

print(df)

def plot_time(df):
	plt.plot(df['size'], df["ineff_time"], linestyle='solid', label="ineff_time")
	plt.plot(df['size'], df["div_time"], linestyle='solid', label="eff_time")
	# plt.xticks(df['size'], df["ineff_time"], linestyle='solid', label="ineff_time")
	# plt.yticks(df['size'], df["div_time"], linestyle='solid', label="eff_time")
	plt.legend()
	plt.title("size vs time")
	plt.xlabel("size")
	plt.ylabel("time")

	plt.savefig('size_vs_time.png')
	plt.clf()


def plot_memory_usage(df):
	plt.plot(df['size'], df["ineff_memory_usage"], linestyle='solid', label="ineff_memory")
	plt.plot(df['size'], df["div_memory_usage"], linestyle='solid', label="eff_memory")
	# plt.xticks(df['size'], df["ineff_memory_usage"], linestyle='solid', label="ineff_memory")
	# plt.yticks(df['size'], df["div_memory_usage"], linestyle='solid', label="eff_memory")
	plt.legend()
	plt.title("size vs memory")
	plt.xlabel("size")
	plt.ylabel("memory")
	plt.yscale("log")
	# plt.xscale("log")

	plt.savefig('size_vs_memory.png')
	plt.clf()

plot_time(df)

plot_memory_usage(df)

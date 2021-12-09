import sys
import matplotlib.pyplot as plt
import logging
logging.basicConfig(filename="plot_data.log", level=logging.INFO)

sys.stdout = open("./data/plot_data_op.txt", "w")

try:
	ineff_f = open("./data/data_inefficient.txt", "r")
	ineff_data = ineff_f.read()
	eff_f = open("./data/data_efficient.txt", "r")
	eff_data = eff_f.read()
except Exception as e:
	logging.info("Reading data files for plotting files failed. Please rerun the programs(basic, ineff) and then run the script to generate plot.")
	exit()

ineff_data = ineff_data.split("\n")
eff_data = eff_data.split("\n")

logging.info("len of ineff_data before processing: {}".format(len(ineff_data)))
logging.info("len of eff_data before processing: {}".format(len(eff_data)))

ineff_df = {
	"size": [],
	"ineff_time": [],
	"ineff_memory_usage": []
}

processed_ineff_data = []

for data in ineff_data:
	data = data.strip()
	split_data = data.split(",")
	if len(split_data) != 3:
		continue

	split_data[0] = int(split_data[0])
	split_data[1] = float(split_data[1])
	split_data[2] = float(split_data[2])

	processed_ineff_data.append(split_data)

processed_eff_data = []

for data in eff_data:
	data = data.strip()
	split_data = data.split(",")
	if len(split_data) != 3:
		continue

	split_data[0] = int(split_data[0])
	split_data[1] = float(split_data[1])
	split_data[2] = float(split_data[2])

	processed_eff_data.append(split_data)

processed_ineff_data = sorted(processed_ineff_data, key= lambda x: x[0])
processed_eff_data = sorted(processed_eff_data, key = lambda x: x[0])

for data in processed_ineff_data:
	ineff_df["size"].append(data[0])
	ineff_df["ineff_time"].append(data[1])
	ineff_df["ineff_memory_usage"].append(data[2])

eff_df = {
	"size": [],
	"eff_time": [],
	"eff_memory_usage": []
}

for data in processed_eff_data:
	eff_df["size"].append(data[0])
	eff_df["eff_time"].append(data[1])
	eff_df["eff_memory_usage"].append(data[2])

logging.info("len of ineff_data before processing: {}".format(len(ineff_df["size"])))
logging.info("len of eff_data before processing: {}".format(len(eff_df["size"])))

def plot_time(ineff_df, eff_df):
	plt.plot(ineff_df['size'], ineff_df["ineff_time"], linestyle='solid', label="ineff_time")
	plt.plot(eff_df['size'], eff_df["eff_time"], linestyle='solid', label="eff_time")
	plt.legend()
	plt.title("size vs time in seconds")
	plt.xlabel("size")
	plt.ylabel("time")

	plt.savefig('size_vs_time.png')
	plt.clf()


def plot_memory_usage(ineff_df, eff_df):
	plt.plot(ineff_df['size'], ineff_df["ineff_memory_usage"], linestyle='solid', label="ineff_memory")
	plt.plot(eff_df['size'], eff_df["eff_memory_usage"], linestyle='solid', label="eff_memory")
	plt.legend()
	plt.title("size vs memory in KB")
	plt.xlabel("size")
	plt.ylabel("memory")

	plt.savefig('size_vs_memory.png')
	plt.clf()

plot_time(ineff_df, eff_df)

plot_memory_usage(ineff_df, eff_df)


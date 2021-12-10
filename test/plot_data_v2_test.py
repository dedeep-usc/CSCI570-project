import random
import time
import matplotlib.pyplot as plt
import tracemalloc
import sys
import logging
logging.basicConfig(filename="test.log")

from main.inefficient import InefficientSeqAlignment
from main.efficient import EfficientSeqAlignment
from main.divide_conquer import DivideConquerSeqAlignment

sys.stdout = open("plot_data_op.txt", "w")

ineff = InefficientSeqAlignment()
eff = EfficientSeqAlignment()
div_conq_alignment = DivideConquerSeqAlignment(eff=eff, ineff=ineff)


def generate_data(str1_len, str2_len):
    a = ["A", "C", "G", "T"]
    str1 = ""
    str2 = ""

    for i in range(str1_len):
        str1 += a[random.randint(0, 3)]

    for i in range(str2_len):
        str2 += a[random.randint(0, 3)]

    tracemalloc.start()
    div_start = time.time()
    first_seq_div, second_seq_div, cost_div = div_conq_alignment.div_conq_alignment(str1, str2)
    div_end = time.time()
    div_current, div_peak = tracemalloc.get_traced_memory()
    div_conq_max_mem = div_peak / 10 ** 3
    div_time = div_end - div_start
    tracemalloc.stop()

    tracemalloc.start()
    ineff_start = time.time()
    first_seq_ineff, second_seq_ineff, cost_ineff = ineff.find_min_cost(str1, str2)
    ineff_end = time.time()
    ineff_current, ineff_peak = tracemalloc.get_traced_memory()
    ineff_max_mem = ineff_peak / 10 ** 3
    ineff_time = ineff_end - ineff_start
    tracemalloc.stop()

    f = open("data/data_efficient.txt", "a")

    data_str = "{},{},{}\n".format(str1_len + str2_len, div_time, div_conq_max_mem)

    f.write(data_str)

    f.close()

    f = open("data/data_inefficient.txt", "a")

    data_str = "{},{},{}\n".format(str1_len + str2_len, ineff_time, ineff_max_mem)

    f.write(data_str)

    f.close()


n = 500

for i in range(1, 1001, 50):
    str1_len = str2_len = i

    generate_data(str1_len, str2_len)

# Read data and plot it

try:
    ineff_f = open("data/data_inefficient.txt", "r")
    ineff_data = ineff_f.read()
    eff_f = open("data/data_efficient.txt", "r")
    eff_data = eff_f.read()
except Exception as e:
    logging.info(
        "Reading data files for plotting files failed. Please rerun the programs(basic, ineff) and then run the script to generate plot.")
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

processed_ineff_data = sorted(processed_ineff_data, key=lambda x: x[0])
processed_eff_data = sorted(processed_eff_data, key=lambda x: x[0])

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
    plt.title("size vs time")
    plt.xlabel("size")
    plt.ylabel("time")

    plt.savefig('size_vs_time.png')
    plt.clf()


def plot_memory_usage(ineff_df, eff_df):
    plt.plot(ineff_df['size'], ineff_df["ineff_memory_usage"], linestyle='solid', label="ineff_memory")
    plt.plot(eff_df['size'], eff_df["eff_memory_usage"], linestyle='solid', label="eff_memory")
    plt.legend()
    plt.title("size vs memory")
    plt.xlabel("size")
    plt.ylabel("memory")
    plt.yscale("log")

    plt.savefig('size_vs_memory.png')
    plt.clf()


plot_time(ineff_df, eff_df)

plot_memory_usage(ineff_df, eff_df)

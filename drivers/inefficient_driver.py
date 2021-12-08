import logging
logging.basicConfig(filename="inefficient_driver.log", level=logging.INFO)

from main.inefficient import *

ineff = InefficientSeqAlignment()

first_seq, second_seq, cost = ineff.find_min_cost("ACGT", "TCAG")

logging.info("first_seq: {}".format(first_seq))
logging.info("second_seq: {}".format(second_seq))
logging.info("cost: {}".format(cost))
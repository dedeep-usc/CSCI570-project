import logging
logging.basicConfig(filename="efficient_driver.log", level=logging.INFO)

from main.efficient import *

eff = EfficientSeqAlignment()

logging.info(eff.find_min_cost("AGGCGCTATATAT", "TCGCGAGAGAGACTC"))

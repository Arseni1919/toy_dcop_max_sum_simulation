import itertools
import operator
import collections
from prettytable import PrettyTable
from termcolor import colored
import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
import pickle
from pprint import pprint
from table_ploter import TablePlotter

ITERATIONS = 40
# A, B, C, D = 0.76, 0.86, 1.29, 1.14
# A, B, C, D = 0, 2, 2.05, 0
A, B, C, D = 1.98, 1.82, 2.73, 0.97
MINUS_INF = -500000
REQ = 100
CRED = 30
RANDOM_FUNCS = True
from_c_to_r = (2, 1)

# FLATTEN = False
FLATTEN = True
file_name = "last_weights.txt"
# LOAD_PREVIOUS_WEIGHTS = True
LOAD_PREVIOUS_WEIGHTS = False
# SAVE_WEIGHTS = True
SAVE_WEIGHTS = False

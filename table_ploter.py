import itertools
import collections
from prettytable import PrettyTable
from termcolor import colored
import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


class TablePlotter:
    def __init__(self):
        self.last_table = None

    def plot_cell_messages(self, all_agents, iteration):
        # headers = ["to \ from", ]
        headers = []
        raws = [[], []]
        colors = [["#56b5fd", "w", "w", "w", "w"], ["#1ac3f5", "w", "w", "w", "w"]]

        for agent in all_agents:
            if 'robot' in agent.name:
                for sender, message in agent.message_box[iteration].items():
                    headers.append(f'{sender}->{agent.name}')
                    raws[0].append(round(message[1], 2))
                    raws[1].append(round(message[2], 2))

        fig, axs = plt.subplots(2, 1, figsize=(8.4, 4.8))  # (w, h)
        fig.canvas.set_window_title(f'Iteration: {iteration + 1}')
        # collabel = ("col 1", "col 2", "col 3")
        rawlabel = (1, 2)
        axs[0].axis('tight')
        axs[0].axis('off')
        the_table = axs[0].table(cellText=raws, colLabels=headers, rowLabels=rawlabel, loc='center')

        if self.last_table:
            for r in range(len(raws)):
                for h in range(len(raws[r])):
                    if self.last_table[r][h] != raws[r][h]:
                        the_table[(r + 1, h)].set_facecolor("red")  # "#56b5fd"
        self.last_table = raws

        x = np.arange(len(headers))
        differences = []
        for i in range(len(headers)):
            differences.append(abs(raws[0][i] - raws[1][i]))
        # fig, ax = plt.subplots()
        axs[1].bar(x, differences)
        axs[1].set_xticks(x)
        axs[1].set_yticks(range(33))
        axs[1].set_xticklabels(headers)
        plt.show()


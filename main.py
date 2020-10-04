from pprint import pprint
import operator
import itertools
import collections
from prettytable import PrettyTable
from termcolor import colored
import random
ITERATIONS = 12


class FunctionNode:
    def __init__(self, name, func, num):
        self.name = name
        self.func = func
        self.num = num
        self.neighbours = []
        self.message_box = {}

    def _create_message(self, var_node):
        message = {}
        for d in var_node.domain:
            message[d] = -9999999
            # message[d] = 0
        return message

    def _create_list_of_domains(self, var_node):
        list_of_domains = [var_node.domain]
        order_of_nei = [var_node]
        for nei in self.neighbours:
            if nei.name != var_node.name:
                list_of_domains.append(nei.domain)
                order_of_nei.append(nei)
        return list_of_domains, order_of_nei

    def _prev_iter_brings(self, i, order_of_nei, iteration):
        curr_sum = 0
        if iteration > 0:
            for order, nei in enumerate(order_of_nei):
                if order > 0:
                    curr_sum += self.message_box[iteration-1][nei.name][i[order]]
        return curr_sum

    def send_message_to(self, var_node, iteration):
        message = self._create_message(var_node)

        list_of_domains, order_of_nei = self._create_list_of_domains(var_node)
        # print(list_of_domains)
        for i in itertools.product(*list_of_domains):
            # print(f'{self.name}: for {i[0]} option: {self.func(self, i, order_of_nei) + self._prev_iter_brings(i, order_of_nei, iteration)}')
            # print(f'{self.name} -> {var_node.name}: with comb:{i} the func value: {self.func(self, i, order_of_nei)}, the added value:{self._prev_iter_brings(i, order_of_nei, iteration)}')
            message[i[0]] = max(message[i[0]],
                                (self.func(self, i, order_of_nei) +
                                self._prev_iter_brings(i, order_of_nei, iteration)))
        flatten_message(message)
        var_node.message_box[iteration][self.name] = message


class VariableNode:
    def __init__(self, name, domain):
        self.name = name
        self.num = int(name[len('robot'):])
        # print(f'{self.name}: {self.num}')
        self.domain = domain
        self.neighbours = []
        self.message_box = {}

    def _create_message(self):
        message = {}
        for d in self.domain:
            message[d] = 0
        return message

    def send_message_to(self, func_node, iteration):
        message = self._create_message()

        if iteration > 0:
            for nei in self.neighbours:
                if nei.name != func_node.name:
                    past_message = self.message_box[iteration-1][nei.name]
                    for d in self.domain:
                        message[d] += past_message[d]
        flatten_message(message)
        func_node.message_box[iteration][self.name] = message


def init_message_boxes(agents):
    for agent in agents:
        for itr in range(ITERATIONS):
            agent.message_box[itr] = {}
            for nei in agent.neighbours:
                agent.message_box[itr][nei.name] = 0


def send_message(agents, iteration):
    for agent in agents:
        # print(agent.name)
        for nei in agent.neighbours:
            agent.send_message_to(nei, iteration)


def create_func_target(cells_near_me):
    def func_target(self, combination, order_of_nei):
        count = 0
        domain_choice_of_var = combination[0]
        # if domain_choice_of_var in cells_near_me:
        # others = combination[1:]
        others = combination
        # if len(set(others)) < len(others):
        #     return 0
        for i in others:
            if i in cells_near_me:
                count += 1
        if count == 0:
            return 0
        return max(0, min(100, 30 * count))
        # return 0
    return func_target


def func_cell(self, combination, order_of_nei):
    counter = 0

    for item_and_how_many_of_it in collections.Counter(combination).items():
        # looking only on one item and it th cell itself
        if item_and_how_many_of_it[0] == self.num:
            counter = max(counter, item_and_how_many_of_it[1])
    if counter > 1:
        return -30 * counter  # + (0.5 - random.random())

    if self.num in combination:
        i = combination.index(self.num)
        if len(order_of_nei) <= 1:
            return 0
            # return order_of_nei[i].num * 2
        aaa = order_of_nei[i].num / 10 * self.num
        return order_of_nei[i].num / 10 * self.num

    return 0


def func_cell1(self, combination, order_of_nei):
    comb = []
    for t in order_of_nei:
        comb.append(combination[t.num - 1])

    my_dict = {
        (1, 1): -30,
        (1, 2): 0.1,
        (2, 1): 0.2,
        (2, 2): 0
    }
    return my_dict[tuple(comb)]


def func_cell2(self, combination, order_of_nei):
    comb = []
    for t in order_of_nei:
        comb.append(combination[t.num - 1])

    my_dict = {
        (1, 1): 0,
        (1, 2): 0.3,
        (2, 1): 0.4,
        (2, 2): -30
    }
    return my_dict[tuple(comb)]



def func_cell3(self, combination, order_of_nei):
    comb = []
    for t in order_of_nei:
        comb.append(combination[t.num - 1])

    my_dict = {
        (3, 3): -30,
        (3, 9): 0.1,
        (8, 3): 0.3,
        (8, 9): 0
    }
    return my_dict[tuple(comb)]

def flatten_message(message):
    min_value = 99999
    for v in message.values():
        min_value = min(min_value, v)

    for k in message.keys():
        message[k] = message[k] - min_value


def print_table_of_messages(all_agents, iteration):
    headers = ["to \ from", ]
    for a in all_agents:
        headers.append(a.name)
    # table = PrettyTable(["from \ to","message box"])
    table = PrettyTable(headers)
    for a in all_agents:
        raw = [a.name]
        for b in all_agents:
            if b.name in a.message_box[iteration]:
                cell_to_print = ''
                for k, v in a.message_box[iteration][b.name].items():
                    cell_to_print = cell_to_print + str(k) + '->' + str(round(v, 2)) + '\n'
                raw.append(cell_to_print)
            else:
                raw.append('')
        table.add_row(raw)

    print('---')
    print('### ITERATION: %s ###' % (iteration + 1))
    print(table)

    for a in all_agents:
        if 'robot' in a.name:
            counter_dict = {}
            for d in a.domain:
                counter_dict[d] = 0
            for b in all_agents:
                if b.name in a.message_box[iteration]:
                    for k, v in a.message_box[iteration][b.name].items():
                        counter_dict[k] += v

            max_value = max(counter_dict.values())
            cells_with_highest_value = [k for k, v in counter_dict.items() if v == max_value]
            print(colored(a.name, 'green'), end=' ')
            choose_str = 'chooses one of' if len(cells_with_highest_value) > 1 else 'chooses'
            print(f'{choose_str}: {cells_with_highest_value}', end=' ')
            print(f'with the highest value: {max_value}')


def scenario_1():
    # init
    target1 = FunctionNode('targ1', create_func_target(cells_near_me=[3]), num=1)
    cell3 = FunctionNode('cell3', func_cell, num=3)
    cell8 = FunctionNode('cell8', func_cell, num=8)
    cell9 = FunctionNode('cell9', func_cell, num=9)
    robot1 = VariableNode('robot1', domain=[3, 8])
    robot2 = VariableNode('robot2', domain=[3, 9])

    target1.neighbours = [robot1, robot2]
    cell3.neighbours = [robot1, robot2]
    cell8.neighbours = [robot1]
    cell9.neighbours = [robot2]
    robot1.neighbours = [cell8, cell3, target1]
    robot2.neighbours = [cell9, cell3, target1]

    return [target1, cell3, cell8, cell9, robot1, robot2]


def scenario_2():
    # init
    target1 = FunctionNode('targ1', create_func_target(cells_near_me=[3]), num=1)

    cell3 = FunctionNode('cell3', func_cell, num=3)
    cell8 = FunctionNode('cell8', func_cell, num=8)
    cell9 = FunctionNode('cell9', func_cell, num=9)
    cell10 = FunctionNode('cell10', func_cell, num=10)

    robot1 = VariableNode('robot1', domain=[3, 8])
    robot2 = VariableNode('robot2', domain=[3, 9])
    robot3 = VariableNode('robot3', domain=[3, 10])

    target1.neighbours = [robot1, robot2, robot3]
    cell3.neighbours = [robot1, robot2, robot3]
    cell8.neighbours = [robot1]
    cell9.neighbours = [robot2]
    cell10.neighbours = [robot3]

    robot1.neighbours = [cell8, cell3, target1]
    robot2.neighbours = [cell9, cell3, target1]
    robot3.neighbours = [cell10, cell3, target1]

    return [target1, cell3, cell8, cell9, cell10, robot1, robot2, robot3]


def scenario_3():
    # init
    target1 = FunctionNode('targ1', create_func_target(cells_near_me=[3,8,9]), num=1)

    cell3 = FunctionNode('cell3', func_cell, num=3)
    cell8 = FunctionNode('cell8', func_cell, num=8)
    cell9 = FunctionNode('cell9', func_cell, num=9)
    cell10 = FunctionNode('cell10', func_cell, num=10)

    robot1 = VariableNode('robot1', domain=[3, 8])
    robot2 = VariableNode('robot2', domain=[3, 9])
    robot3 = VariableNode('robot3', domain=[3, 10])

    # neighbours
    target1.neighbours = [robot1, robot2, robot3]

    cell3.neighbours = [robot1, robot2, robot3]
    cell8.neighbours = [robot1]
    cell9.neighbours = [robot2]
    cell10.neighbours = [robot3]

    robot1.neighbours = [cell8, cell3, target1]
    robot2.neighbours = [cell9, cell3, target1]
    robot3.neighbours = [cell10, cell3, target1]

    return [target1, cell3, cell8, cell9, cell10, robot1, robot2, robot3]


def scenario_4():
    # print(scenario_4.__name__)
    # init
    target1 = FunctionNode('targ1', create_func_target(cells_near_me=[3]), num=1)

    cell3 = FunctionNode('cell3', func_cell, num=3)
    cell4 = FunctionNode('cell4', func_cell, num=4)
    cell5 = FunctionNode('cell5', func_cell, num=5)
    cell8 = FunctionNode('cell8', func_cell, num=8)
    cell9 = FunctionNode('cell9', func_cell, num=9)
    cell10 = FunctionNode('cell10', func_cell, num=10)

    robot1 = VariableNode('robot1', domain=[3, 4, 8])
    robot2 = VariableNode('robot2', domain=[3, 5, 9])
    robot3 = VariableNode('robot3', domain=[3, 4, 5, 10])

    # neighbours
    target1.neighbours = [robot1, robot2, robot3]

    cell3.neighbours = [robot1, robot2, robot3]
    cell4.neighbours = [robot1, robot3]
    cell5.neighbours = [robot2, robot3]
    cell8.neighbours = [robot1]
    cell9.neighbours = [robot2]
    cell10.neighbours = [robot3]

    robot1.neighbours = [cell8, cell4, cell3, target1]
    robot2.neighbours = [cell9, cell5, cell3, target1]
    robot3.neighbours = [cell10, cell5, cell4, cell3, target1]

    return [target1, cell3, cell4, cell5, cell8, cell9, cell10, robot1, robot2, robot3]


def scenario_5():
    # init
    target1 = FunctionNode('targ1', create_func_target(cells_near_me=[3,8,9]), num=1)

    cell3 = FunctionNode('cell3', func_cell, num=3)
    cell4 = FunctionNode('cell4', func_cell, num=4)
    cell5 = FunctionNode('cell5', func_cell, num=5)
    cell8 = FunctionNode('cell8', func_cell, num=8)
    cell9 = FunctionNode('cell9', func_cell, num=9)
    cell10 = FunctionNode('cell10', func_cell, num=10)

    robot1 = VariableNode('robot1', domain=[3, 4, 8])
    robot2 = VariableNode('robot2', domain=[3, 5, 9])
    robot3 = VariableNode('robot3', domain=[3, 4, 5, 10])

    # neighbours
    target1.neighbours = [robot1, robot2, robot3]

    cell3.neighbours = [robot1, robot2, robot3]
    cell4.neighbours = [robot1, robot3]
    cell5.neighbours = [robot2, robot3]
    cell8.neighbours = [robot1]
    cell9.neighbours = [robot2]
    cell10.neighbours = [robot3]

    robot1.neighbours = [cell8, cell4, cell3, target1]
    robot2.neighbours = [cell9, cell5, cell3, target1]
    robot3.neighbours = [cell10, cell5, cell4, cell3, target1]

    return [target1, cell3, cell4, cell5, cell8, cell9, cell10, robot1, robot2, robot3]


def scenario_6():
    # init
    target1 = FunctionNode('targ1', create_func_target(cells_near_me=[3]), num=1)

    cell3 = FunctionNode('cell3', func_cell, num=3)
    cell5 = FunctionNode('cell5', func_cell, num=5)
    cell8 = FunctionNode('cell8', func_cell, num=8)
    cell9 = FunctionNode('cell9', func_cell, num=9)
    cell10 = FunctionNode('cell10', func_cell, num=10)

    robot1 = VariableNode('robot1', domain=[3, 8])
    robot2 = VariableNode('robot2', domain=[3, 5, 9])
    robot3 = VariableNode('robot3', domain=[3, 5, 10])

    # neighbours
    target1.neighbours = [robot1, robot2, robot3]

    cell3.neighbours = [robot1, robot2, robot3]
    cell5.neighbours = [robot2, robot3]
    cell8.neighbours = [robot1]
    cell9.neighbours = [robot2]
    cell10.neighbours = [robot3]

    robot1.neighbours = [cell8, cell3, target1]
    robot2.neighbours = [cell9, cell5, cell3, target1]
    robot3.neighbours = [cell10, cell5, cell3, target1]

    return [target1, cell3, cell5, cell8, cell9, cell10, robot1, robot2, robot3]


def scenario_7():
    # init
    target1 = FunctionNode('targ1', create_func_target(cells_near_me=[3, 8, 9]), num=1)

    cell3 = FunctionNode('cell3', func_cell, num=3)
    cell5 = FunctionNode('cell5', func_cell, num=5)
    cell8 = FunctionNode('cell8', func_cell, num=8)
    cell9 = FunctionNode('cell9', func_cell, num=9)
    cell10 = FunctionNode('cell10', func_cell, num=10)

    robot1 = VariableNode('robot1', domain=[3, 8])
    robot2 = VariableNode('robot2', domain=[3, 5, 9])
    robot3 = VariableNode('robot3', domain=[3, 5, 10])

    # neighbours
    target1.neighbours = [robot1, robot2, robot3]

    cell3.neighbours = [robot1, robot2, robot3]
    cell5.neighbours = [robot2, robot3]
    cell8.neighbours = [robot1]
    cell9.neighbours = [robot2]
    cell10.neighbours = [robot3]

    robot1.neighbours = [cell8, cell3, target1]
    robot2.neighbours = [cell9, cell5, cell3, target1]
    robot3.neighbours = [cell10, cell5, cell3, target1]

    return [target1, cell3, cell5, cell8, cell9, cell10, robot1, robot2, robot3]

def scenario_8_1():
    # init
    # target1 = FunctionNode('targ1', create_func_target(cells_near_me=[3, 8, 9]), num=1)

    cell1 = FunctionNode('cell1', func_cell1, num=1)
    cell2 = FunctionNode('cell2', func_cell2, num=2)

    robot1 = VariableNode('robot1', domain=[1, 2])
    robot2 = VariableNode('robot2', domain=[1, 2])

    # neighbours
    cell1.neighbours = [robot1, robot2]
    cell2.neighbours = [robot1, robot2]


    robot1.neighbours = [cell1, cell2]
    robot2.neighbours = [cell1, cell2]

    return [cell1, cell2, robot1, robot2]

def scenario_8_2():
    # init
    # target1 = FunctionNode('targ1', create_func_target(cells_near_me=[3, 8, 9]), num=1)

    cell1 = FunctionNode('cell1', func_cell, num=1)
    cell2 = FunctionNode('cell2', func_cell, num=2)
    cell8 = FunctionNode('cell8', func_cell, num=8)
    cell9 = FunctionNode('cell9', func_cell, num=9)

    robot1 = VariableNode('robot1', domain=[1, 2, 8])
    robot2 = VariableNode('robot2', domain=[1, 2, 9])

    # neighbours
    cell1.neighbours = [robot1, robot2]
    cell2.neighbours = [robot1, robot2]
    cell8.neighbours = [robot1]
    cell9.neighbours = [robot2]

    robot1.neighbours = [cell1, cell2, cell8]
    robot2.neighbours = [cell1, cell2, cell9]

    return [cell1, cell2, cell8, cell9, robot1, robot2]


def scenario_9():
    # init
    target1 = FunctionNode('targ1', create_func_target(cells_near_me=[3]), num=1)
    target2 = FunctionNode('targ2', create_func_target(cells_near_me=[3]), num=2)
    cell3 = FunctionNode('cell3', func_cell, num=3)
    cell8 = FunctionNode('cell8', func_cell, num=8)
    cell9 = FunctionNode('cell9', func_cell, num=9)
    robot1 = VariableNode('robot1', domain=[3, 8])
    robot2 = VariableNode('robot2', domain=[3, 9])

    target1.neighbours = [robot1, robot2]
    target2.neighbours = [robot1, robot2]
    cell3.neighbours = [robot1, robot2]
    cell8.neighbours = [robot1]
    cell9.neighbours = [robot2]
    robot1.neighbours = [cell8, cell3, target1, target2]
    robot2.neighbours = [cell9, cell3, target1, target2]

    return [target1, target2, cell3, cell8, cell9, robot1, robot2]


def scenario_10():
    # init
    target1 = FunctionNode('targ1', create_func_target(cells_near_me=[3]), num=1)
    cell3 = FunctionNode('cell3', func_cell3, num=3)
    cell8 = FunctionNode('cell8', func_cell, num=8)
    cell9 = FunctionNode('cell9', func_cell, num=9)
    robot1 = VariableNode('robot1', domain=[3, 8])
    robot2 = VariableNode('robot2', domain=[3, 9])

    target1.neighbours = [robot1, robot2]
    cell3.neighbours = [robot1, robot2]
    cell8.neighbours = [robot1]
    cell9.neighbours = [robot2]
    robot1.neighbours = [cell8, cell3, target1]
    robot2.neighbours = [cell9, cell3, target1]

    return [target1, cell3, cell8, cell9, robot1, robot2]


def main():
    # init
    # scenario_func = scenario_1
    # scenario_func = scenario_2
    # scenario_func = scenario_3
    # scenario_func = scenario_4
    # scenario_func = scenario_5
    # scenario_func = scenario_6
    # scenario_func = scenario_7
    scenario_func = scenario_8_1
    # scenario_func = scenario_8_2
    # scenario_func = scenario_9
    # scenario_func = scenario_10

    all_agents = scenario_func()
    print(scenario_func.__name__)

    init_message_boxes(all_agents)

    for iteration in range(ITERATIONS):
        send_message(all_agents, iteration)
        print_table_of_messages(all_agents, iteration)


if __name__ == '__main__':
    main()

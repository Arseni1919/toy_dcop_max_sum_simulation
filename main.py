from pprint import pprint
import itertools
import collections
from prettytable import PrettyTable
ITERATIONS = 20


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
            message[d] = 9999999
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
            # print(i)
            # if i[0] == 3 and var_node.name == 'robot1' and self.name == 'cell3':
            #     print(i, self.func(self, i, order_of_nei) + self._prev_iter_brings(i, order_of_nei, iteration))
            message[i[0]] = min(message[i[0]], self.func(self, i, order_of_nei) +
                                self._prev_iter_brings(i, order_of_nei, iteration))
        flatten_message(message)
        var_node.message_box[iteration][self.name] = message


class VariableNode:
    def __init__(self, name, domain):
        self.name = name
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


def func_target1(self, combination, order_of_nei):
    count = 0
    me = combination[0]
    if me in [1,2,3]:
        others = combination[1:]
        for i in others:
            if i in [1,2,3]:
                count += 1
        return min(30, 100 - 30*count)
    return 0


def func_cell(self, combination, order_of_nei):
    if combination[0] == self.num:
        counter = 0
        for i in collections.Counter(combination).items():
            if i[0] == self.num:
                counter = max(counter, i[1])
        if counter > 1:
            return -30 * counter
    return 0


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
                    cell_to_print = cell_to_print + str(k) + '->' + str(v) + '\n'
                raw.append(cell_to_print)
            else:
                raw.append('')
        table.add_row(raw)
    print('### ITERATION: %s ###' % iteration)
    print(table)


def scenario_1():
    # init
    target1 = FunctionNode('targ1', func_target1, 1)
    cell1 = FunctionNode('cell1', func_cell, 1)
    cell2 = FunctionNode('cell2', func_cell, 2)
    cell3 = FunctionNode('cell3', func_cell, 3)
    cell4 = FunctionNode('cell4', func_cell, 4)
    cell5 = FunctionNode('cell5', func_cell, 5)
    robot1 = VariableNode('robot1', [1, 3, 4])
    robot2 = VariableNode('robot2', [2, 3, 5])
    robot3 = VariableNode('robot3', [3, 4, 5])

    target1.neighbours = [robot1, robot2, robot3]
    cell1.neighbours = [robot1]
    cell2.neighbours = [robot2]
    cell3.neighbours = [robot1, robot2, robot3]
    cell4.neighbours = [robot1, robot3]
    cell5.neighbours = [robot2, robot3]
    robot1.neighbours = [cell1, cell3, cell4, target1]
    robot2.neighbours = [cell2, cell3, cell5, target1]
    robot3.neighbours = [cell3, cell4, cell5, target1]

    return [target1, cell1, cell2, cell3, cell4, cell5, robot1, robot2, robot3]


def scenario_2():
    # init
    target1 = FunctionNode('targ1', func_target1, 1)
    cell1 = FunctionNode('cell1', func_cell, 1)
    cell2 = FunctionNode('cell2', func_cell, 2)
    cell3 = FunctionNode('cell3', func_cell, 3)
    cell4 = FunctionNode('cell4', func_cell, 4)
    cell5 = FunctionNode('cell5', func_cell, 5)
    robot1 = VariableNode('robot1', [1, 3, 4])
    robot2 = VariableNode('robot2', [2, 3, 5])

    target1.neighbours = [robot1, robot2]
    cell1.neighbours = [robot1]
    cell2.neighbours = [robot2]
    cell3.neighbours = [robot1, robot2]
    cell4.neighbours = [robot1]
    cell5.neighbours = [robot2]
    robot1.neighbours = [cell1, cell3, cell4, target1]
    robot2.neighbours = [cell2, cell3, cell5, target1]

    return [target1, cell1, cell2, cell3, cell4, cell5, robot1, robot2]


def main():
    # init
    # all_agents = scenario_1()
    all_agents = scenario_2()

    init_message_boxes(all_agents)

    for iteration in range(ITERATIONS):
        send_message(all_agents, iteration)
        # pprint(robot3.message_box[iteration])
        # print()
        # pprint(cell3.message_box[iteration])
        print('---')
        print_table_of_messages(all_agents, iteration)


if __name__ == '__main__':
    main()


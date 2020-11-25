from funcs import *


class FunctionNode:
    def __init__(self, name, func, num, common: str = ''):
        self.name = name
        self.func = func
        self.num = num
        self.common = common
        self.neighbours = []
        self.message_box = {}
        if LOAD_PREVIOUS_WEIGHTS:
            self.rund = load_weight_of(self.name, file_name)
        else:
            self.rund = random.choice(range(100)) / 100

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
                    curr_sum += self.message_box[iteration - 1][nei.name][i[order]]
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
            # print(f'{self.name}: {i} = {self.func(self, i, order_of_nei)}')
        if FLATTEN or 'tar' in self.name:
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
        if LOAD_PREVIOUS_WEIGHTS:
            self.rund = load_weight_of(self.name, file_name)
        else:
            self.rund = random.choice(range(100)) / 100

    def get_neighbour(self, n):
        for nei in self.neighbours:
            if nei.num == n:
                return nei

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
                    past_message = self.message_box[iteration - 1][nei.name]
                    for d in self.domain:
                        message[d] += past_message[d]
        if FLATTEN:
            flatten_message(message)
        func_node.message_box[iteration][self.name] = message

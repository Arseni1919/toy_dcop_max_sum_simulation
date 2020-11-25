from CONSTANTS import *


def init_message_boxes(agents):
    for agent in agents:
        for itr in range(ITERATIONS):
            agent.message_box[itr] = {}
            for nei in agent.neighbours:
                agent.message_box[itr][nei.name] = 0


def create_func_target(cells_near_me):
    def func_target(self, combination, order_of_nei):
        self.cells_near_me = cells_near_me
        count = 0
        domain_choice_of_var = combination[0]
        others = combination
        for i in others:
            if i in cells_near_me:
                count += 1
        if count == 0:
            return 0
        return max(0, min(REQ, CRED * count))

    return func_target


def func_cell_zero(self, combination, order_of_nei):
    return 0


def func_cell(self, combination, order_of_nei):

    # if there are neighbours to the cell
    # if len(order_of_nei) <= 1:
    #     return 0
    counter = 0
    # if the cell itself chosen by more than one robot
    for item_and_how_many_of_it in collections.Counter(combination).items():
        # looking only on one item and it th cell itself
        if item_and_how_many_of_it[0] == self.num:
            counter = max(counter, item_and_how_many_of_it[1])
    if counter > 1:
        # return -30 * counter  # + (0.5 - random.random())
        return MINUS_INF

    # if the cell is even inside the combination
    if self.num in combination:
        i = combination.index(self.num)
        val = calc_weight(self, order_of_nei[i])
        return val
    return 0


def func_cell1(self, combination, order_of_nei, comb=None):
    my_dict = {
        (1, 1): MINUS_INF,
        (1, 2): A,
        (1, 9): 0,
        (2, 1): B,
        (2, 2): 0,
        (2, 2): 0,
        (2, 9): 0,
        (8, 1): 0,
        (8, 2): 0,
        (8, 9): 0,
    }

    if comb is None:
        comb = []
        for t in order_of_nei:
            comb.append(combination[t.num - 1])
        return my_dict[tuple(comb)]

    return my_dict[tuple(comb)]


def func_cell2(self, combination, order_of_nei, comb=None):
    my_dict = {
        (1, 1): 0,
        (1, 2): C,
        (1, 9): 0,
        (2, 1): D,
        (2, 2): MINUS_INF,
        (2, 9): 0,
        (8, 1): 0,
        (8, 2): 0,
        (8, 9): 0,
    }

    if comb is None:
        comb = []
        for t in order_of_nei:
            comb.append(combination[t.num - 1])

        return my_dict[tuple(comb)]

    return my_dict[tuple(comb)]


def func_cell3(self, combination, order_of_nei):
    comb = []
    for t in order_of_nei:
        comb.append(combination[t.num - 1])

    my_dict = {
        (3, 3): MINUS_INF,
        (3, 9): 0.1,
        (8, 3): 0.3,
        (8, 9): 0
    }
    return my_dict[tuple(comb)]

# def print_all_pos_sum_weights(all_agents, i=ITERATIONS-1):
#     variable_nodes = []
#     function_nodes = []
#     for agent in all_agents:
#         if isinstance(agent, VariableNode):
#             variable_nodes.append(agent)
#         else:
#             function_nodes.append(agent)
#
#     n8, n9 = 0, 0
#     for a in all_agents:
#         if 'robot' in a.name:
#             # print(f'{a.name}: {a.message_box[i]}')
#             counter_dict = {}
#             for d in a.domain:
#                 counter_dict[d] = 0
#             for b in all_agents:
#                 if b.name in a.message_box[i]:
#                     for k, v in a.message_box[i][b.name].items():
#                         counter_dict[k] += v
#             # print(f'{a.name}: {counter_dict}')
#         else:
#             # print(f'{a.name}: {a.message_box[i]}')
#             if a.name == 'cell8':
#                 n8 = a.message_box[i]['robot1'][1]
#             if a.name == 'cell9':
#                 n9 = a.message_box[i]['robot2'][1]
#     print(f'{n8}, {n9}')
#     print(f'{abs(n8 - 30)}, {abs(n9 - 30)}')


def send_message(agents, iteration):
    for agent in agents:
        # print(agent.name)
        for nei in agent.neighbours:
            agent.send_message_to(nei, iteration)


def flatten_message(message):
    min_value = 99999
    for v in message.values():
        min_value = min(min_value, v)

    for k in message.keys():
        message[k] = message[k] - min_value


def print_constrains(all_agents, name):
    cell = None
    for agent in all_agents:
        if agent.name == name:
            cell = agent
            break
    to_print = f'{cell.name}: \n'
    list_of_domains, order_of_nei = cell._create_list_of_domains(cell.neighbours[0])
    for i in itertools.product(*list_of_domains):
        res = cell.func(cell, i, order_of_nei)
        if res >= 0:
            res = res
            to_print += f'{i}: {round(res, 3)}\n'
        else:
            res = '-'
            to_print += f'{i}: {res}\n'
    print(to_print)


def print_all_comb_weights(all_agents):
    cell3 = 'cell3'
    cell4 = 'cell4'
    cell5 = 'cell5'
    robot1 = 'robot1'
    robot2 = 'robot2'
    robot3 = 'robot3'
    for agent in all_agents:
        if agent.name == cell3:
            cell3 = agent
        if agent.name == cell4:
            cell4 = agent
        if agent.name == cell5:
            cell5 = agent
        if agent.name == robot1:
            robot1 = agent
        if agent.name == robot2:
            robot2 = agent
        if agent.name == robot3:
            robot3 = agent

    list_of_domains, order_of_nei = cell3._create_list_of_domains(robot1)
    # print(list_of_domains)
    list_of_weights = []
    to_print = ''
    order_of_nei = [robot1, robot2, robot3]
    for i in itertools.product(*list_of_domains):
        res = cell3.func(cell3, i, order_of_nei) + cell4.func(cell4, i, order_of_nei) + cell5.func(cell5, i,
                                                                                                   order_of_nei)
        if res >= 0:
            res = res
            list_of_weights.append(round(res, 3))
            to_print += f'{i}: {round(res, 3)}\n'
            # print(f'{i}: {round(res, 3)}')
        else:
            res = '-'
            to_print += f'{i}: {res}\n'
            # print(f'{i}: {res}')
    print(to_print)
    print(f'list_of_weights - set(list_of_weights): {len(list_of_weights) - len(set(list_of_weights))}')


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


def print_choices(all_agents, iteration):
    assignments = []
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
            print(f'with the highest value: {max_value:.2f}')
            assignments.extend(cells_with_highest_value)
    # print_all_pos_sum_weights(all_agents, iteration)
    return len(assignments) > len(set(assignments))


def create_choice_list(all_agents):
    choice_list = {}
    for a in all_agents:
        if 'robot' in a.name:
            choice_list[a.name] = {'choice': [], 'weight': []}
    return choice_list


def extend_choice_list(all_agents, iteration, choice_list):

    for a in all_agents:
        if 'robot' in a.name:
            counter_dict = {}
            for d in a.domain:
                counter_dict[d] = 0
            for b in all_agents:
                if b.name in a.message_box[iteration]:
                    for k, v in a.message_box[iteration][b.name].items():
                        counter_dict[k] += v
            choice, weight = max(counter_dict.items(), key=operator.itemgetter(1))

            choice = choice - 100 if choice > 100 else choice
            choice_list[a.name]['choice'].append(choice)
            choice_list[a.name]['weight'].append(weight)
            # choice_list[a.name]['choice'].append(max(counter_dict.items(), key=operator.itemgetter(1))[0])
            # choice_list[a.name]['weight'].append(max(counter_dict.items(), key=operator.itemgetter(1))[1])


def graph_choice_list(choice_list, ITERATIONS):
    fig, axs = plt.subplots(2, 1)
    # ax.scatter(z, y)
    for robot_name, choices_dict in choice_list.items():
        axs[0].plot(choices_dict['choice'], label=robot_name, ls='dashdot', alpha=0.5)
        axs[1].plot(choices_dict['weight'][:], label=robot_name, ls='dashdot', alpha=0.5)
        for i, txt in enumerate(choices_dict['weight']):
            if i % 5 == 0:
                axs[0].annotate(round(txt, 2), (i, choices_dict['choice'][i]), fontsize=5)
    axs[0].set_xticks(range(1, ITERATIONS+1))
    axs[0].set_xticklabels(range(1, ITERATIONS+1), fontsize=5)
    axs[1].set_xticks(range(3, ITERATIONS + 1))
    axs[1].set_xticklabels(range(3, ITERATIONS + 1), fontsize=5)
    # plt.axhline(y=0, color='black')
    axs[0].legend()

    plt.title(f'Choices of Robots (y - choices, x - time)')
    plt.show()


def calc_weight(cell, robot):
    # return order_of_nei[i].rund / 10 * (self.num + 1)
    # return order_of_nei[i].rund / 10 * (self.num + 2)
    # return order_of_nei[i].num / 10 * (self.num + 1)
    # return order_of_nei[i].num / 10 * (self.num + order_of_nei[i].rund)
    # aaa = order_of_nei[i].rund / 10 * (self.num+100)
    # aaa = order_of_nei[i].rund * (self.num/order_of_nei[i].num + self.rund) / 10
    # val = round(order_of_nei[i].rund * (self.rund) * 10, 2)  # --> works

    return round(cell.rund * robot.rund * 10, 2)


def print_assignment_costs(all_agents):
    list_of_domains = []
    list_of_robots = []
    list_of_targets = []

    for agent in all_agents:
        if 'robot' in agent.name:
            list_of_robots.append(agent)
            list_of_domains.append(agent.domain)
        if 'targ' in agent.name:
            list_of_targets.append(agent)

    max_val, max_comb = 0, []
    comb_vs_val = []
    for comb in itertools.product(*list_of_domains):
        # each one peaks one cell
        if len(set(comb)) == len(comb):
        # if True:
            val = 0
            # the value given by cells
            for indx, robot in enumerate(list_of_robots):
                val += calc_weight(robot.get_neighbour(comb[indx]), robot)
                # val += round(robot.get_neighbour(comb[indx]).rund * robot.rund * 10, 2)
            # the value given by target
            for target in list_of_targets:
                for cell_near_target in target.cells_near_me:
                    if cell_near_target in comb:
                        val += CRED
            if val > max_val:
                max_val = val
                max_comb = comb
            comb_vs_val.append((max_comb, val))
            # print(f'{comb}: \t{val:.2f}')

    # for comb_vs_val_i in comb_vs_val:
    #     if comb_vs_val_i[1] == max_val:
    #         print(f'(max) -> {comb_vs_val_i[0]}: \t{comb_vs_val_i[1]:.2f}')
    print(f'(max) -> {max_comb}: \t{max_val:.2f}')


def extend_difference_lists(all_agents,
                            iteration,
                            DIFFERENCE_ROBOT_1,
                            DIFFERENCE_ROBOT_2):
    for a in all_agents:
        if 'robot' in a.name:
            counter_dict = {}
            for d in a.domain:
                counter_dict[d] = 0
            for b in all_agents:
                if b.name in a.message_box[iteration]:
                    for k, v in a.message_box[iteration][b.name].items():
                        counter_dict[k] += v

            if a.name == 'robot1':
                DIFFERENCE_ROBOT_1.append(counter_dict[1] - counter_dict[2])
            if a.name == 'robot3':
                DIFFERENCE_ROBOT_2.append(counter_dict[1] - counter_dict[2])


def extend_MESSAGES_FROM_CELL_TO_ROBOT(all_agents, iteration, MESSAGES_FROM_CELL_TO_ROBOT, from_c_to_r):
    for a in all_agents:
        if 'robot' in a.name and a.num == from_c_to_r[1]:
            for b in all_agents:
                if b.name in a.message_box[iteration] and b.num == from_c_to_r[0]:
                    for k, v in a.message_box[iteration][b.name].items():
                        MESSAGES_FROM_CELL_TO_ROBOT[k-1].append(v)


def print_equation(all_agents, names):
    a, b, c, d = 0, 0, 0, 0

    for name in names:
        cell = None
        for agent in all_agents:
            if agent.name == name:
                cell = agent
                break
        to_print = f'{cell.name}: \n'
        list_of_domains, order_of_nei = cell._create_list_of_domains(cell.neighbours[0])
        for i in itertools.product(*list_of_domains):
            res = cell.func(cell, i, order_of_nei)
            if i == (1, 2) and name == 'cell1':
                a = res
            if i == (2, 1) and name == 'cell1':
                b = res
            if i == (1, 2) and name == 'cell2':
                c = res
            if i == (2, 1) and name == 'cell2':
                d = res

    print(f'The growth: {abs((a + c) - (b + d)):.2f} ')
    print(f'(1, 2) = {a + c:.2f}')
    print(f'(2, 1) = {b + d:.2f}')
    print(f'a:{a:.2f}, b:{b:.2f}, c:{c:.2f}, d:{d:.2f}')
    s = (c-b)/(a+c-b-d)
    # print(f'check: {math.ceil(4*(c-b)/(a+c-b-d))}')
    if a+c > b+d:
        print(f'a+c ({a+c:.2f}) > b+2d ({b+2*d:.2f}) is {a+c > b+2*d}')
        print(f'the convergence will start on iteration: {2 * math.ceil(d / (a + c - b - d))+ 1}')
    if a+c < b+d:
        print(f'b+d ({b+d:.2f}) > a+2c ({a+2*c:.2f}) is {a+2*c < b+d}')
        print(f'the convergence will start on iteration: {2 * math.ceil(c / (b + d - a - c)) + 1}')

    # print(f'4*math.ceil((a-b)/(a+c-(b+d))): {4*math.ceil((a-b)/(a+c-(b+d)))}')


def print_differences(DIFFERENCE_ROBOT_1, DIFFERENCE_ROBOT_2):
    # for i in range(0, len(DIFFERENCE_ROBOT_1)):
    for i in range(3):
        # print(f'({DIFFERENCE_ROBOT_1[i] - DIFFERENCE_ROBOT_1[i-4]}) and '
        #       f'({DIFFERENCE_ROBOT_2[i] - DIFFERENCE_ROBOT_2[i-4]})')
        print(f'({DIFFERENCE_ROBOT_1[i]}) and '
              f'({DIFFERENCE_ROBOT_2[i]})')


def print_graph(DIFFERENCE_ROBOT_1, DIFFERENCE_ROBOT_2, ITERATIONS):
    plt.plot(DIFFERENCE_ROBOT_1, label='Robot 1')
    plt.plot(DIFFERENCE_ROBOT_2, label='Robot 2')
    plt.xticks(range(1, ITERATIONS+1))
    plt.axhline(y=0, color='black')
    plt.legend()
    # fig_manager = plt.get_current_fig_manager()
    # fig_manager.window.SetPosition((500, 0))
    # thismanager.window.SetPosition((500, 0))
    plt.title(f'All weights of 1 minus all weights of 2')
    plt.show()


def print_graph_from_c_to_r(MESSAGES_FROM_CELL_TO_ROBOT, ITERATIONS, from_c_to_r):
    for i in range(len(MESSAGES_FROM_CELL_TO_ROBOT[0])):
        if i == 0 or i % 2:
            if i != 1:
                continue
        print(f'[{i+1}] '
              f'\t1: {MESSAGES_FROM_CELL_TO_ROBOT[0][i]:.2f} '
              f'\t(+{round(MESSAGES_FROM_CELL_TO_ROBOT[0][i]-MESSAGES_FROM_CELL_TO_ROBOT[0][i-1], 3)}), '
              f'\t2: {MESSAGES_FROM_CELL_TO_ROBOT[1][i]:.2f} '
              f'\t(+{round(MESSAGES_FROM_CELL_TO_ROBOT[1][i]-MESSAGES_FROM_CELL_TO_ROBOT[1][i-1], 3)})')

    plt.plot(MESSAGES_FROM_CELL_TO_ROBOT[0], label='of cell 1')
    plt.plot(MESSAGES_FROM_CELL_TO_ROBOT[1], label='of cell 2')
    plt.xticks(range(1, ITERATIONS+1))
    plt.axhline(y=0, color='black')
    plt.legend()
    plt.title(f'From Target {from_c_to_r[0]} to Robot {from_c_to_r[1]}')
    plt.show()

def plot_cell_messages(all_agents, iteration):
    # headers = ["to \ from", ]
    headers = []
    raws = [[],[]]
    colors = [["#56b5fd", "w", "w", "w", "w"], ["#1ac3f5", "w", "w", "w", "w"]]

    for agent in all_agents:
        if 'robot' in agent.name:
            for sender, message in agent.message_box[iteration].items():
                headers.append(f'{sender}->{agent.name}')
                raws[0].append(round(message[1], 2))
                raws[1].append(round(message[2], 2))

    fig, axs = plt.subplots(2, 1, figsize=(8.4, 4.8))  # (w, h)
    fig.canvas.set_window_title(f'Iteration: {iteration}')
    # collabel = ("col 1", "col 2", "col 3")
    rawlabel = (1, 2)
    axs[0].axis('tight')
    axs[0].axis('off')
    the_table = axs[0].table(cellText=raws, colLabels=headers, rowLabels=rawlabel, loc='center')
    the_table[(1, 0)].set_facecolor("#56b5fd")
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


def save_weights(all_agents, file_name: str):
    # open the file for writing
    curr_dict = {}
    for agent in all_agents:
        curr_dict[agent.name] = agent.rund
    with open(file_name, 'wb') as fileObject:
        pickle.dump(curr_dict, fileObject)


def load_weight_of(agent_name: str, file_name: str):
    with open(file_name, 'rb') as handle:
        dict = pickle.load(handle)
        return dict[agent_name]


def get_dict_of_weights(file_name: str):
    with open(file_name, 'rb') as handle:
        return pickle.load(handle)


def reassign_common_weights(all_agents):
    for agent in all_agents:
        if 'cell' in agent.name:
            if agent.common != '':
                for common_agent in all_agents:
                    if common_agent.name == agent.common:
                        agent.rund = common_agent.rund
                # agent.rund = random.choice([0.01,0.02,0.03])



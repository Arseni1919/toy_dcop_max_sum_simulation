from scenarious import *


def main():
    # init
    # scenario_func = scenario_2_2  # !
    # scenario_func = scenario_2_2_1  # !
    # scenario_func = scenario_3_1  # !
    # scenario_func = scenario_3_2  # !
    # scenario_func = scenario_3_3  # !
    # scenario_func = scenario_3_5  # !
    # scenario_func = scenario_3_6  # !
    # scenario_func = scenario_3_7  # !
    # scenario_func = scenario_3_20  # !
    # scenario_func = scenario_3_20_1  # !
    # scenario_func = scenario_3_21  # !
    # scenario_func = scenario_3_21_1  # !
    # scenario_func = scenario_3_22  # !
    scenario_func = scenario_4_1  # !
    # scenario_func = scenario_4_1_1
    # scenario_func = scenario_4_3  # !
    # scenario_func = scenario_4_6
    # scenario_func = scenario_4_7
    # scenario_func = scenario_4_9  # !
    # scenario_func = scenario_4_10  # !
    # scenario_func = scenario_4_20
    # scenario_func = scenario_4_16
    # scenario_func = scenario_4_17

    all_agents = scenario_func()
    # reassign_common_weights(all_agents)
    print(scenario_func.__name__)
    DIFFERENCE_ROBOT_1 = []
    DIFFERENCE_ROBOT_2 = []
    choice_list = create_choice_list(all_agents)
    MESSAGES_FROM_CELL_TO_ROBOT = [[], []]
    tp = TablePlotter()

    init_message_boxes(all_agents)
    collisions = []
    for iteration in range(ITERATIONS):
        send_message(all_agents, iteration)
        print_table_of_messages(all_agents, iteration)

        # tp.plot_cell_messages(all_agents, iteration)

        collisions.append(print_choices(all_agents, iteration))
        # extend_difference_lists(all_agents, iteration, DIFFERENCE_ROBOT_1, DIFFERENCE_ROBOT_2)
        extend_choice_list(all_agents, iteration, choice_list)
        # extend_MESSAGES_FROM_CELL_TO_ROBOT(all_agents, iteration, MESSAGES_FROM_CELL_TO_ROBOT, from_c_to_r)

    print(f'collisions: {sum(collisions[-10:])} (for last ten iterations)')
    # print_all_pos_sum_weights(all_agents, 0)
    if scenario_func is scenario_3_5:
        print_constrains(all_agents, 'cell1')
        print_constrains(all_agents, 'cell2')
        print_equation(all_agents, names=['cell1', 'cell2'])

    # print_differences(DIFFERENCE_ROBOT_1, DIFFERENCE_ROBOT_2)
    # print_graph(DIFFERENCE_ROBOT_1, DIFFERENCE_ROBOT_2, ITERATIONS)
    print_assignment_costs(all_agents)
    graph_choice_list(choice_list, ITERATIONS)
    # print_graph_from_c_to_r(MESSAGES_FROM_CELL_TO_ROBOT, ITERATIONS, from_c_to_r)
    if SAVE_WEIGHTS:
        save_weights(all_agents, file_name)
    print('-' * 20)


if __name__ == '__main__':
    main()

    # for i in np.arange(0.0, 1.0, 0.05):
    #     cur_sum = 30.0
    #     x = cur_sum * i
    #     # A = x
    #     # C = cur_sum - x
    #     # B = x
    #     # D = cur_sum - x
    #     CRED = x
    #     main()


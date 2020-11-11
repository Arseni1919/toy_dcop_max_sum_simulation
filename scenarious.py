from agents import *


def scenario_3_1():
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


def scenario_3_2():
    # init
    target1 = FunctionNode('targ1', create_func_target(cells_near_me=[1, 11, 12]), num=1)
    cell1 = FunctionNode('cell1', func_cell, num=1)
    cell8 = FunctionNode('cell8', func_cell, num=8)
    cell9 = FunctionNode('cell9', func_cell, num=9)
    cell11 = FunctionNode('cell11', func_cell, num=11)
    cell12 = FunctionNode('cell12', func_cell, num=12)
    robot1 = VariableNode('robot1', domain=[3, 8, 11])
    robot2 = VariableNode('robot2', domain=[3, 9, 12])

    target1.neighbours = [robot1, robot2]
    cell1.neighbours = [robot1, robot2]
    cell8.neighbours = [robot1]
    cell9.neighbours = [robot2]
    cell11.neighbours = [robot1]
    cell12.neighbours = [robot2]
    robot1.neighbours = [cell11, cell8, cell1, target1]
    robot2.neighbours = [cell12, cell9, cell1, target1]

    return [target1, cell1, cell8, cell9, cell11, cell12, robot1, robot2]


def scenario_3_3():
    # init
    target1 = FunctionNode('targ1', create_func_target(cells_near_me=[1, 11, 12, 8, 9]), num=1)
    cell1 = FunctionNode('cell1', func_cell, num=1)
    cell8 = FunctionNode('cell8', func_cell, num=8)
    cell9 = FunctionNode('cell9', func_cell, num=9)
    cell11 = FunctionNode('cell11', func_cell, num=11)
    cell12 = FunctionNode('cell12', func_cell, num=12)
    robot1 = VariableNode('robot1', domain=[3, 8, 11])
    robot2 = VariableNode('robot2', domain=[3, 9, 12])

    target1.neighbours = [robot1, robot2]
    cell1.neighbours = [robot1, robot2]
    cell8.neighbours = [robot1]
    cell9.neighbours = [robot2]
    cell11.neighbours = [robot1]
    cell12.neighbours = [robot2]
    robot1.neighbours = [cell11, cell8, cell1, target1]
    robot2.neighbours = [cell12, cell9, cell1, target1]

    return [target1, cell1, cell8, cell9, cell11, cell12, robot1, robot2]


def scenario_3_20():
    # print(scenario_4.__name__)
    # init
    cell1 = FunctionNode('cell1', func_cell, num=1)
    cell2 = FunctionNode('cell2', func_cell, num=2)
    cell3 = FunctionNode('cell3', func_cell, num=3)

    robot1 = VariableNode('robot1', domain=[1, 2])
    robot2 = VariableNode('robot2', domain=[1, 3])
    robot3 = VariableNode('robot3', domain=[1, 2, 3])

    # neighbours
    cell1.neighbours = [robot1, robot2, robot3]
    cell2.neighbours = [robot1, robot3]
    cell3.neighbours = [robot2, robot3]

    robot1.neighbours = [cell2, cell1,]
    robot2.neighbours = [cell3, cell1,]
    robot3.neighbours = [cell3, cell2, cell1,]

    return [cell1, cell2, cell3, robot1, robot2, robot3]


def scenario_3_20_1():
    # print(scenario_4.__name__)
    # init
    cell1 = FunctionNode('cell1', func_cell, num=1)
    cell2 = FunctionNode('cell2', func_cell, num=2)
    cell3 = FunctionNode('cell3', func_cell, num=3)
    cell8 = FunctionNode('cell8', func_cell, num=8)
    cell9 = FunctionNode('cell9', func_cell, num=9)
    cell10 = FunctionNode('cell10', func_cell, num=10)

    robot1 = VariableNode('robot1', domain=[1, 2, 8])
    robot2 = VariableNode('robot2', domain=[1, 3, 9])
    robot3 = VariableNode('robot3', domain=[1, 2, 3, 10])

    # neighbours
    cell1.neighbours = [robot1, robot2, robot3]
    cell2.neighbours = [robot1, robot3]
    cell3.neighbours = [robot2, robot3]
    cell8.neighbours = [robot1]
    cell9.neighbours = [robot2]
    cell10.neighbours = [robot3]

    robot1.neighbours = [cell8, cell2, cell1]
    robot2.neighbours = [cell9, cell3, cell1]
    robot3.neighbours = [cell10, cell3, cell2, cell1]

    return [cell1, cell2, cell3, cell8, cell9, cell10, robot1, robot2, robot3]


def scenario_3_21():
    # print(scenario_4.__name__)
    # init
    cell112 = FunctionNode('cell112', func_cell, num=112, common='cell112')
    cell113 = FunctionNode('cell113', func_cell, num=113, common='cell112')
    cell123 = FunctionNode('cell123', func_cell, num=123, common='cell112')
    cell2 = FunctionNode('cell2', func_cell, num=2)
    cell3 = FunctionNode('cell3', func_cell, num=3)

    robot1 = VariableNode('robot1', domain=[112, 113, 2])
    robot2 = VariableNode('robot2', domain=[112, 123, 3])
    robot3 = VariableNode('robot3', domain=[113, 123, 2, 3])

    # neighbours
    cell112.neighbours = [robot1, robot2]
    cell113.neighbours = [robot1, robot3]
    cell123.neighbours = [robot2, robot3]
    cell2.neighbours = [robot1, robot3]
    cell3.neighbours = [robot2, robot3]

    robot1.neighbours = [cell2, cell112, cell113]
    robot2.neighbours = [cell3, cell112, cell123]
    robot3.neighbours = [cell3, cell2, cell113, cell123]

    return [cell112, cell113, cell123, cell2, cell3, robot1, robot2, robot3]


def scenario_3_21_1():
    # print(scenario_4.__name__)
    # init
    cell112 = FunctionNode('cell112', func_cell, num=112, common='cell112')
    cell113 = FunctionNode('cell113', func_cell, num=113, common='cell112')
    cell123 = FunctionNode('cell123', func_cell, num=123, common='cell112')
    cell2 = FunctionNode('cell2', func_cell, num=2)
    cell3 = FunctionNode('cell3', func_cell, num=3)
    cell10 = FunctionNode('cell10', func_cell, num=10)
    cell20 = FunctionNode('cell20', func_cell, num=20)
    cell30 = FunctionNode('cell30', func_cell, num=30)

    robot1 = VariableNode('robot1', domain=[112, 113, 2, 10])
    robot2 = VariableNode('robot2', domain=[112, 123, 3, 20])
    robot3 = VariableNode('robot3', domain=[113, 123, 2, 3, 30])

    # neighbours
    cell112.neighbours = [robot1, robot2]
    cell113.neighbours = [robot1, robot3]
    cell123.neighbours = [robot2, robot3]
    cell2.neighbours = [robot1, robot3]
    cell3.neighbours = [robot2, robot3]
    cell10.neighbours = [robot1]
    cell20.neighbours = [robot2]
    cell30.neighbours = [robot3]

    robot1.neighbours = [cell2, cell112, cell113, cell10]
    robot2.neighbours = [cell3, cell112, cell123, cell20]
    robot3.neighbours = [cell3, cell2, cell113, cell123, cell30]

    return [cell112, cell113, cell123, cell2, cell3, cell10, cell20, cell30, robot1, robot2, robot3]


def scenario_3_22():
    # print(scenario_4.__name__)
    # init
    cell113 = FunctionNode('cell113', func_cell, num=113)
    cell123 = FunctionNode('cell123', func_cell, num=123)
    cell2 = FunctionNode('cell2', func_cell, num=2)
    cell3 = FunctionNode('cell3', func_cell, num=3)

    robot1 = VariableNode('robot1', domain=[113, 2])
    robot2 = VariableNode('robot2', domain=[123, 3])
    robot3 = VariableNode('robot3', domain=[113, 123, 2, 3])

    # neighbours
    cell113.neighbours = [robot1, robot3]
    cell123.neighbours = [robot2, robot3]
    cell2.neighbours = [robot1, robot3]
    cell3.neighbours = [robot2, robot3]

    robot1.neighbours = [cell2, cell113]
    robot2.neighbours = [cell3, cell123]
    robot3.neighbours = [cell3, cell2, cell113, cell123]

    return [cell113, cell123, cell2, cell3, robot1, robot2, robot3]


def scenario_4_1():
    # print(scenario_4.__name__)
    # init
    target1 = FunctionNode('targ1', create_func_target(cells_near_me=[1]), num=1)

    cell1 = FunctionNode('cell1', func_cell, num=1)
    cell2 = FunctionNode('cell2', func_cell, num=2)
    cell3 = FunctionNode('cell3', func_cell, num=3)
    cell8 = FunctionNode('cell8', func_cell, num=8)
    cell9 = FunctionNode('cell9', func_cell, num=9)
    cell10 = FunctionNode('cell10', func_cell, num=10)

    robot1 = VariableNode('robot1', domain=[1, 2, 8])
    robot2 = VariableNode('robot2', domain=[1, 3, 9])
    robot3 = VariableNode('robot3', domain=[1, 2, 3, 10])

    # neighbours
    target1.neighbours = [robot1, robot2, robot3]

    cell1.neighbours = [robot1, robot2, robot3]
    cell2.neighbours = [robot1, robot3]
    cell3.neighbours = [robot2, robot3]
    cell8.neighbours = [robot1]
    cell9.neighbours = [robot2]
    cell10.neighbours = [robot3]

    robot1.neighbours = [cell8, cell2, cell1, target1]
    robot2.neighbours = [cell9, cell3, cell1, target1]
    robot3.neighbours = [cell10, cell3, cell2, cell1, target1]

    return [target1, cell1, cell2, cell3, cell8, cell9, cell10, robot1, robot2, robot3]


def scenario_4_1_1():
    # print(scenario_4.__name__)
    # init
    target1 = FunctionNode('targ1', create_func_target(cells_near_me=[112, 113, 123]), num=1)

    cell112 = FunctionNode('cell112', func_cell, num=112, common='cell112')
    cell113 = FunctionNode('cell113', func_cell, num=113, common='cell112')
    cell123 = FunctionNode('cell123', func_cell, num=123, common='cell112')
    cell2 = FunctionNode('cell2', func_cell, num=2)
    cell3 = FunctionNode('cell3', func_cell, num=3)
    cell10 = FunctionNode('cell10', func_cell, num=10)
    cell20 = FunctionNode('cell20', func_cell, num=20)
    cell30 = FunctionNode('cell30', func_cell, num=30)

    robot1 = VariableNode('robot1', domain=[112, 113, 2, 10])
    robot2 = VariableNode('robot2', domain=[112, 123, 3, 20])
    robot3 = VariableNode('robot3', domain=[113, 123, 2, 3, 30])

    # neighbours
    target1.neighbours = [robot1, robot2, robot3]
    cell112.neighbours = [robot1, robot2]
    cell113.neighbours = [robot1, robot3]
    cell123.neighbours = [robot2, robot3]
    cell2.neighbours = [robot1, robot3]
    cell3.neighbours = [robot2, robot3]
    cell10.neighbours = [robot1]
    cell20.neighbours = [robot2]
    cell30.neighbours = [robot3]

    robot1.neighbours = [cell2, cell112, cell113, cell10, target1]
    robot2.neighbours = [cell3, cell112, cell123, cell20, target1]
    robot3.neighbours = [cell3, cell2, cell113, cell123, cell30, target1]

    return [target1, cell112, cell113, cell123, cell2, cell3, cell10, cell20, cell30, robot1, robot2, robot3]


def scenario_4_3():
    # init
    target1 = FunctionNode('targ1', create_func_target(cells_near_me=[3, 8, 9]), num=1)

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


def scenario_4_9():
    # init
    target1 = FunctionNode('targ1', create_func_target(cells_near_me=[1]), num=1)

    cell1 = FunctionNode('cell1', func_cell, num=1)
    cell2 = FunctionNode('cell2', func_cell, num=2)
    cell8 = FunctionNode('cell8', func_cell, num=8)
    cell9 = FunctionNode('cell9', func_cell, num=9)
    cell10 = FunctionNode('cell10', func_cell, num=10)

    robot1 = VariableNode('robot1', domain=[1, 8])
    robot2 = VariableNode('robot2', domain=[1, 2, 9])
    robot3 = VariableNode('robot3', domain=[1, 2, 10])

    # neighbours
    target1.neighbours = [robot1, robot2, robot3]

    cell1.neighbours = [robot1, robot2, robot3]
    cell2.neighbours = [robot2, robot3]
    cell8.neighbours = [robot1]
    cell9.neighbours = [robot2]
    cell10.neighbours = [robot3]

    robot1.neighbours = [cell8, cell1, target1]
    robot2.neighbours = [cell9, cell2, cell1, target1]
    robot3.neighbours = [cell10, cell2, cell1, target1]

    return [target1, cell1, cell2, cell8, cell9, cell10, robot1, robot2, robot3]


def scenario_4_10():
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


def scenario_2_2():
    # init
    # target1 = FunctionNode('targ1', create_func_target(cells_near_me=[3, 8, 9]), num=1)
    if RANDOM_FUNCS:
        cell1 = FunctionNode('cell1', func_cell, num=1)
        cell2 = FunctionNode('cell2', func_cell, num=2)
    else:
        cell1 = FunctionNode('cell1', func_cell1, num=1)
        cell2 = FunctionNode('cell2', func_cell2, num=2)
    # cell1 = FunctionNode('cell1', func_cell1, num=1)
    # cell2 = FunctionNode('cell2', func_cell2, num=2)

    robot1 = VariableNode('robot1', domain=[1, 2])
    robot2 = VariableNode('robot2', domain=[1, 2])

    # neighbours
    cell1.neighbours = [robot1, robot2]
    cell2.neighbours = [robot1, robot2]

    robot1.neighbours = [cell1, cell2]
    robot2.neighbours = [cell1, cell2]

    return [cell1, cell2, robot1, robot2]


def scenario_2_2_1():
    # init
    # target1 = FunctionNode('targ1', create_func_target(cells_near_me=[3, 8, 9]), num=1)
    if RANDOM_FUNCS:
        cell1 = FunctionNode('cell1', func_cell, num=1)
        cell2 = FunctionNode('cell2', func_cell, num=2)
    else:
        cell1 = FunctionNode('cell1', func_cell1, num=1)
        cell2 = FunctionNode('cell2', func_cell2, num=2)
    cell10 = FunctionNode('cell10', func_cell, num=10)
    cell20 = FunctionNode('cell20', func_cell, num=20)

    robot1 = VariableNode('robot1', domain=[1, 2, 10])
    robot2 = VariableNode('robot2', domain=[1, 2, 20])

    # neighbours
    cell1.neighbours = [robot1, robot2]
    cell2.neighbours = [robot1, robot2]
    cell10.neighbours = [robot1]
    cell20.neighbours = [robot2]

    robot1.neighbours = [cell1, cell2, cell10]
    robot2.neighbours = [cell1, cell2, cell20]

    return [cell1, cell2, cell10, cell20, robot1, robot2]


def scenario_4_20():
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


def scenario_3_5():
    # init
    target1 = FunctionNode('targ1', create_func_target(cells_near_me=[1]), num=1)
    if RANDOM_FUNCS:
        cell1 = FunctionNode('cell1', func_cell, num=1)
        cell2 = FunctionNode('cell2', func_cell, num=2)
    else:
        cell1 = FunctionNode('cell1', func_cell1, num=1)
        cell2 = FunctionNode('cell2', func_cell2, num=2)
    # cell8 = FunctionNode('cell8', func_cell, num=8)
    # cell9 = FunctionNode('cell9', func_cell, num=9)
    robot1 = VariableNode('robot1', domain=[1, 2])
    robot2 = VariableNode('robot2', domain=[1, 2])

    target1.neighbours = [robot1, robot2]
    cell1.neighbours = [robot1, robot2]
    cell2.neighbours = [robot1, robot2]
    # cell8.neighbours = [robot1]
    # cell9.neighbours = [robot2]
    robot1.neighbours = [cell1, cell2, target1, ]  # cell8,
    robot2.neighbours = [cell1, cell2, target1, ]  # cell9,

    # return [target1, cell1, cell2, cell8, cell9, robot1, robot2]
    return [target1, cell1, cell2, robot1, robot2]


def scenario_3_6():
    # init
    target1 = FunctionNode('targ1', create_func_target(cells_near_me=[1, 12]), num=1)
    if RANDOM_FUNCS:
        cell1 = FunctionNode('cell1', func_cell, num=1)
        cell2 = FunctionNode('cell2', func_cell, num=2)
    else:
        cell1 = FunctionNode('cell1', func_cell1, num=1)
        cell2 = FunctionNode('cell2', func_cell2, num=2)
    cell12 = FunctionNode('cell12', func_cell, num=12)

    robot1 = VariableNode('robot1', domain=[1, 2])
    robot2 = VariableNode('robot2', domain=[1, 2])

    target1.neighbours = [robot1, robot2]
    cell1.neighbours = [robot1, robot2]
    cell2.neighbours = [robot1, robot2]
    cell12.neighbours = [robot2]

    robot1.neighbours = [cell1, cell2, target1, ]
    robot2.neighbours = [cell1, cell2, cell12, target1, ]

    return [target1, cell1, cell2, cell12, robot1, robot2]


def scenario_3_7():
    # init
    target1 = FunctionNode('targ1', create_func_target(cells_near_me=[1, 9, 12]), num=1)
    if RANDOM_FUNCS:
        cell1 = FunctionNode('cell1', func_cell, num=1)
        cell2 = FunctionNode('cell2', func_cell, num=2)
    else:
        cell1 = FunctionNode('cell1', func_cell1, num=1)
        cell2 = FunctionNode('cell2', func_cell2, num=2)
    cell12 = FunctionNode('cell12', func_cell, num=12)
    cell9 = FunctionNode('cell9', func_cell, num=9)
    robot1 = VariableNode('robot1', domain=[1, 2])
    robot2 = VariableNode('robot2', domain=[1, 2])

    target1.neighbours = [robot1, robot2]
    cell1.neighbours = [robot1, robot2]
    cell2.neighbours = [robot1, robot2]
    cell12.neighbours = [robot2]
    cell9.neighbours = [robot2]

    robot1.neighbours = [cell1, cell2, target1, ]
    robot2.neighbours = [cell1, cell2, cell9, cell12, target1, ]

    return [target1, cell1, cell2, cell9, cell12, robot1, robot2]


def scenario_4_16():
    # init
    target1 = FunctionNode('targ1', create_func_target(cells_near_me=[1, 3]), num=1)

    cell1 = FunctionNode('cell1', func_cell, num=1)
    cell2 = FunctionNode('cell2', func_cell, num=2)
    cell3 = FunctionNode('cell3', func_cell, num=3)
    cell8 = FunctionNode('cell8', func_cell, num=8)
    cell9 = FunctionNode('cell9', func_cell, num=9)
    cell10 = FunctionNode('cell10', func_cell, num=10)

    robot1 = VariableNode('robot1', domain=[3, 8])
    robot2 = VariableNode('robot2', domain=[1, 2, 3, 9])
    robot3 = VariableNode('robot3', domain=[1, 2, 10])

    # neighbours
    target1.neighbours = [robot1, robot2, robot3]

    cell1.neighbours = [robot2, robot3]
    cell2.neighbours = [robot2, robot3]
    cell3.neighbours = [robot1, robot2]
    cell8.neighbours = [robot1]
    cell9.neighbours = [robot2]
    cell10.neighbours = [robot3]

    robot1.neighbours = [cell8, cell3, target1]
    robot2.neighbours = [cell9, cell3, cell2, cell1, target1]
    robot3.neighbours = [cell10, cell2, cell1, target1]

    return [target1, cell1, cell2, cell3, cell8, cell9, cell10, robot1, robot2, robot3]


def scenario_4_17():
    # init
    target1 = FunctionNode('targ1', create_func_target(cells_near_me=[1, 3, 4]), num=1)

    cell1 = FunctionNode('cell1', func_cell, num=1)
    cell2 = FunctionNode('cell2', func_cell, num=2)
    cell3 = FunctionNode('cell3', func_cell, num=3)
    cell4 = FunctionNode('cell4', func_cell, num=4)
    cell8 = FunctionNode('cell8', func_cell, num=8)
    cell9 = FunctionNode('cell9', func_cell, num=9)
    cell10 = FunctionNode('cell10', func_cell, num=10)

    robot1 = VariableNode('robot1', domain=[3, 4, 8])
    robot2 = VariableNode('robot2', domain=[1, 2, 3, 9])
    robot3 = VariableNode('robot3', domain=[1, 2, 10])

    # neighbours
    target1.neighbours = [robot1, robot2, robot3]

    cell1.neighbours = [robot2, robot3]
    cell2.neighbours = [robot2, robot3]
    cell3.neighbours = [robot1, robot2]
    cell4.neighbours = [robot1]
    cell8.neighbours = [robot1]
    cell9.neighbours = [robot2]
    cell10.neighbours = [robot3]

    robot1.neighbours = [cell8, cell3, cell4, target1]
    robot2.neighbours = [cell9, cell3, cell2, cell1, target1]
    robot3.neighbours = [cell10, cell2, cell1, target1]

    return [target1, cell1, cell2, cell3, cell4, cell8, cell9, cell10, robot1, robot2, robot3]


def scenario_4_6():
    # init
    target1 = FunctionNode('targ1', create_func_target(cells_near_me=[1, 3]), num=1)

    cell1 = FunctionNode('cell1', func_cell, num=1)
    # cell2 = FunctionNode('cell2', func_cell, num=2)
    cell3 = FunctionNode('cell3', func_cell, num=3)
    cell8 = FunctionNode('cell8', func_cell, num=8)
    cell9 = FunctionNode('cell9', func_cell, num=9)
    cell10 = FunctionNode('cell10', func_cell, num=10)

    robot1 = VariableNode('robot1', domain=[3, 8])
    robot2 = VariableNode('robot2', domain=[1, 3, 9])
    robot3 = VariableNode('robot3', domain=[1, 10])

    # neighbours
    target1.neighbours = [robot1, robot2, robot3]

    cell1.neighbours = [robot2, robot3]
    # cell2.neighbours = [robot2, robot3]
    cell3.neighbours = [robot1, robot2]
    cell8.neighbours = [robot1]
    cell9.neighbours = [robot2]
    cell10.neighbours = [robot3]

    robot1.neighbours = [cell8, cell3, target1]
    robot2.neighbours = [cell9, cell3, cell1, target1]
    robot3.neighbours = [cell10, cell1, target1]

    return [target1, cell1, cell3, cell8, cell9, cell10, robot1, robot2, robot3]


def scenario_4_7():
    # init
    target1 = FunctionNode('targ1', create_func_target(cells_near_me=[1, 3, 4, 5]), num=1)

    cell1 = FunctionNode('cell1', func_cell, num=1)
    # cell2 = FunctionNode('cell2', func_cell, num=2)
    cell3 = FunctionNode('cell3', func_cell, num=3)
    cell4 = FunctionNode('cell4', func_cell, num=4)
    cell5 = FunctionNode('cell5', func_cell, num=5)
    cell8 = FunctionNode('cell8', func_cell, num=8)
    cell9 = FunctionNode('cell9', func_cell, num=9)
    cell10 = FunctionNode('cell10', func_cell, num=10)

    robot1 = VariableNode('robot1', domain=[3, 4, 8])
    robot2 = VariableNode('robot2', domain=[1, 3, 9])
    robot3 = VariableNode('robot3', domain=[1, 5, 10])

    # neighbours
    target1.neighbours = [robot1, robot2, robot3]

    cell1.neighbours = [robot2, robot3]
    # cell2.neighbours = [robot2, robot3]
    cell3.neighbours = [robot1, robot2]
    cell4.neighbours = [robot1]
    cell5.neighbours = [robot3]
    cell8.neighbours = [robot1]
    cell9.neighbours = [robot2]
    cell10.neighbours = [robot3]

    robot1.neighbours = [cell8, cell4, cell3, target1]
    robot2.neighbours = [cell9, cell3, cell1, target1]
    robot3.neighbours = [cell10, cell5, cell1, target1]

    return [target1, cell1, cell3, cell4, cell5, cell8, cell9, cell10, robot1, robot2, robot3]

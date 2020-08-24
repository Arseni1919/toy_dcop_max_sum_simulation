#
#
# def scenario_1():
#     # init
#     target1 = FunctionNode('targ1', func_target1, 1)
#     cell1 = FunctionNode('cell1', func_cell, 1)
#     cell2 = FunctionNode('cell2', func_cell, 2)
#     cell3 = FunctionNode('cell3', func_cell, 3)
#     cell4 = FunctionNode('cell4', func_cell, 4)
#     cell5 = FunctionNode('cell5', func_cell, 5)
#     robot1 = VariableNode('robot1', [1, 3, 4])
#     robot2 = VariableNode('robot2', [2, 3, 5])
#     robot3 = VariableNode('robot3', [3, 4, 5])
#
#     target1.neighbours = [robot1, robot2, robot3]
#     cell1.neighbours = [robot1]
#     cell2.neighbours = [robot2]
#     cell3.neighbours = [robot1, robot2, robot3]
#     cell4.neighbours = [robot1, robot3]
#     cell5.neighbours = [robot2, robot3]
#     robot1.neighbours = [cell1, cell3, cell4, target1]
#     robot2.neighbours = [cell2, cell3, cell5, target1]
#     robot3.neighbours = [cell3, cell4, cell5, target1]
#
#     return [target1, cell1, cell2, cell3, cell4, cell5, robot1, robot2, robot3]
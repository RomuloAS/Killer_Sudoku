"""These tables list the possible combinations for various sums"""


cell_1 = {

    1: [[1]],
    2: [[2]],
    3: [[3]],
    4: [[4]],
    5: [[5]],
    6: [[6]],
    7: [[7]],
    8: [[8]],
    9: [[9]]

}

cell_2 = {

    3: [[1, 2]],
    4: [[1, 3]],
    5: [[1, 4], [2, 3]],
    6: [[1, 5], [2, 4]],
    7: [[1, 6], [2, 5], [3, 4]],
    8: [[1, 7], [2, 6], [3, 5]],
    9: [[1, 8], [2, 7], [3, 6], [4, 5]],
    10: [[1, 9], [2, 8], [3, 7], [4, 6]],
    11: [[2, 9], [3, 8], [4, 7], [5, 6]],
    12: [[3, 9], [4, 8], [5, 7]],
    13: [[4, 9], [5, 8], [6, 7]],
    14: [[5, 9], [6, 8]],
    15: [[6, 9], [7, 8]],
    16: [[7, 9]],
    17: [[8, 9]]
}

cell_3 = {

    6: [[1, 2, 3]],
    7: [[1, 2, 4]],
    8: [[1, 2, 5], [1, 3, 4]],
    9: [[1, 2, 6], [1, 3, 5], [2, 3, 4]],
    10: [[1, 2, 7], [1, 3, 6], [1, 4, 5], [2, 3, 5]],
    11: [[1, 2, 8], [1, 3, 7], [1, 4, 6], [2, 3, 6], [2, 4, 5]],
    12: [[1, 2, 9], [1, 3, 8], [1, 4, 7], [1, 5, 6], [2, 3, 7], [2, 4, 6], [3, 4, 5]],
    13: [[1, 3, 9], [1, 4, 8], [1, 5, 7], [2, 3, 8], [2, 4, 7], [2, 5, 6], [3, 4, 6]],
    14: [[1, 4, 9], [1, 5, 8], [1, 6, 7], [2, 3, 9], [2, 4, 8], [2, 5, 7], [3, 4, 7], [3, 5, 6]],
    15: [[1, 5, 9], [1, 6, 8], [2, 4, 9], [2, 5, 8], [2, 6, 7], [3, 4, 8], [3, 5, 7], [4, 5, 6]],
    16: [[1, 6, 9], [1, 7, 8], [2, 5, 9], [2, 6, 8], [3, 4, 9], [3, 5, 8], [3, 6, 7], [4, 5, 7]],
    17: [[1, 7, 9], [2, 6, 9], [2, 7, 8], [3, 5, 9], [3, 6, 8], [4, 5, 8], [4, 6, 7]],
    18: [[1, 8, 9], [2, 7, 9], [3, 6, 9], [3, 7, 8], [4, 5, 9], [4, 6, 8], [5, 6, 7]],
    19: [[2, 8, 9], [3, 7, 9], [4, 6, 9], [4, 7, 8], [5, 6, 8]],
    20: [[3, 8, 9], [4, 7, 9], [5, 6, 9], [5, 7, 8]],
    21: [[4, 8, 9], [5, 7, 9], [6, 7, 8]],
    22: [[5, 8, 9], [6, 7, 9]],
    23: [[6, 8, 9]],
    24: [[7, 8, 9]]

}

cell_4 = {

    10: [[1, 2, 3, 4]],
    11: [[1, 2, 3, 5]],
    12: [[1, 2, 3, 6], [1, 2, 4, 5]],
    13: [[1, 2, 3, 7], [1, 2, 4, 6], [1, 3, 4, 5]],
    14: [[1, 2, 3, 8], [1, 2, 4, 7], [1, 2, 5, 6], [1, 3, 4, 6], [2, 3, 4, 5]],
    15: [[1, 2, 3, 9], [1, 2, 4, 8], [1, 2, 5, 7], [1, 3, 4, 7], [1, 3, 5, 6], [2, 3, 4, 6]],
    16: [[1, 2, 4, 9], [1, 2, 5, 8], [1, 2, 6, 7], [1, 3, 4, 8], [1, 3, 5, 7], [1, 4, 5, 6], [2, 3, 4, 7], [2, 3, 5, 6]],
    17: [[1, 2, 5, 9], [1, 2, 6, 8], [1, 3, 4, 9], [1, 3, 5, 8], [1, 3, 6, 7], [1, 4, 5, 7], [2, 3, 4, 8], [2, 3, 5, 7], [2, 4, 5, 6]],
    18: [[1, 2, 6, 9], [1, 2, 7, 8], [1, 3, 5, 9], [1, 3, 6, 8], [1, 4, 5, 8], [1, 4, 6, 7], [2, 3, 4, 9], [2, 3, 5, 8], [2, 3, 6, 7], [2, 4, 5, 7], [3, 4, 5, 6]],
    19: [[1, 2, 7, 9], [1, 3, 6, 9], [1, 3, 7, 8], [1, 4, 5, 9], [1, 4, 6, 8], [1, 5, 6, 7], [2, 3, 5, 9], [2, 3, 6, 8], [2, 4, 5, 8], [2, 4, 6, 7], [3, 4, 5, 7]],
    20: [[1, 2, 8, 9], [1, 3, 7, 9], [1, 4, 6, 9], [1, 4, 7, 8], [1, 5, 6, 8], [2, 3, 6, 9], [2, 3, 7, 8], [2, 4, 5, 9], [2, 4, 6, 8], [2, 5, 6, 7], [3, 4, 5, 8], [3, 4, 6, 7]],
    21: [[1, 3, 8, 9], [1, 4, 7, 9], [1, 5, 6, 9], [1, 5, 7, 8], [2, 3, 7, 9], [2, 4, 6, 9], [2, 4, 7, 8], [2, 5, 6, 8], [3, 4, 5, 9], [3, 4, 6, 8], [3, 5, 6, 7]],
    22: [[1, 4, 8, 9], [1, 5, 7, 9], [1, 6, 7, 8], [2, 3, 8, 9], [2, 4, 7, 9], [2, 5, 6, 9], [2, 5, 7, 8], [3, 4, 6, 9], [3, 4, 7, 8], [3, 5, 6, 8], [4, 5, 6, 7]],
    23: [[1, 5, 8, 9], [1, 6, 7, 9], [2, 4, 8, 9], [2, 5, 7, 9], [2, 6, 7, 8], [3, 4, 7, 9], [3, 5, 6, 9], [3, 5, 7, 8], [4, 5, 6, 8]],
    24: [[1, 6, 8, 9], [2, 5, 8, 9], [2, 6, 7, 9], [3, 4, 8, 9], [3, 5, 7, 9], [3, 6, 7, 8], [4, 5, 6, 9], [4, 5, 7, 8]],
    25: [[1, 7, 8, 9], [2, 6, 8, 9], [3, 5, 8, 9], [3, 6, 7, 9], [4, 5, 7, 9], [4, 6, 7, 8]],
    26: [[2, 7, 8, 9], [3, 6, 8, 9], [4, 5, 8, 9], [4, 6, 7, 9], [5, 6, 7, 8]],
    27: [[3, 7, 8, 9], [4, 6, 8, 9], [5, 6, 7, 9]],
    28: [[4, 7, 8, 9], [5, 6, 8, 9]],
    29: [[5, 7, 8, 9]],
    30: [[6, 7, 8, 9]]

}

cell_5 = {

    15: [[1, 2, 3, 4, 5]],
    16: [[1, 2, 3, 4, 6]],
    17: [[1, 2, 3, 4, 7], [1, 2, 3, 5, 6]],
    18: [[1, 2, 3, 4, 8], [1, 2, 3, 5, 7], [1, 2, 4, 5, 6]],
    19: [[1, 2, 3, 4, 9], [1, 2, 3, 5, 8], [1, 2, 3, 6, 7], [1, 2, 4, 5, 7], [1, 3, 4, 5, 6]],
    20: [[1, 2, 3, 5, 9], [1, 2, 3, 6, 8], [1, 2, 4, 5, 8], [1, 2, 4, 6, 7], [1, 3, 4, 5, 7], [2, 3, 4, 5, 6]],
    21: [[1, 2, 3, 6, 9], [1, 2, 3, 7, 8], [1, 2, 4, 5, 9], [1, 2, 4, 6, 8], [1, 2, 5, 6, 7], [1, 3, 4, 5, 8], [1, 3, 4, 6, 7], [2, 3, 4, 5, 7]],
    22: [[1, 2, 3, 7, 9], [1, 2, 4, 6, 9], [1, 2, 4, 7, 8], [1, 2, 5, 6, 8], [1, 3, 4, 5, 9], [1, 3, 4, 6, 8], [1, 3, 5, 6, 7], [2, 3, 4, 5, 8], [2, 3, 4, 6, 7]],
    23: [[1, 2, 3, 8, 9], [1, 2, 4, 7, 9], [1, 2, 5, 6, 9], [1, 2, 5, 7, 8], [1, 3, 4, 6, 9], [1, 3, 4, 7, 8], [1, 3, 5, 6, 8], [1, 4, 5, 6, 7], [2, 3, 4, 5, 9], [2, 3, 4, 6, 8], [2, 3, 5, 6, 7]],
    24: [[1, 2, 4, 8, 9], [1, 2, 5, 7, 9], [1, 2, 6, 7, 8], [1, 3, 4, 7, 9], [1, 3, 5, 6, 9], [1, 3, 5, 7, 8], [1, 4, 5, 6, 8], [2, 3, 4, 6, 9], [2, 3, 4, 7, 8], [2, 3, 5, 6, 8], [2, 4, 5, 6, 7]],
    25: [[1, 2, 5, 8, 9], [1, 2, 6, 7, 9], [1, 3, 4, 8, 9], [1, 3, 5, 7, 9], [1, 3, 6, 7, 8], [1, 4, 5, 6, 9], [1, 4, 5, 7, 8], [2, 3, 4, 7, 9], [2, 3, 5, 6, 9], [2, 3, 5, 7, 8], [2, 4, 5, 6, 8], [3, 4, 5, 6, 7]],
    26: [[1, 2, 6, 8, 9], [1, 3, 5, 8, 9], [1, 3, 6, 7, 9], [1, 4, 5, 7, 9], [1, 4, 6, 7, 8], [2, 3, 4, 8, 9], [2, 3, 5, 7, 9], [2, 3, 6, 7, 8], [2, 4, 5, 6, 9], [2, 4, 5, 7, 8], [3, 4, 5, 6, 8]],
    27: [[1, 2, 7, 8, 9], [1, 3, 6, 8, 9], [1, 4, 5, 8, 9], [1, 4, 6, 7, 9], [1, 5, 6, 7, 8], [2, 3, 5, 8, 9], [2, 3, 6, 7, 9], [2, 4, 5, 7, 9], [2, 4, 6, 7, 8], [3, 4, 5, 6, 9], [3, 4, 5, 7, 8]],
    28: [[1, 3, 7, 8, 9], [1, 4, 6, 8, 9], [1, 5, 6, 7, 9], [2, 3, 6, 8, 9], [2, 4, 5, 8, 9], [2, 4, 6, 7, 9], [2, 5, 6, 7, 8], [3, 4, 5, 7, 9], [3, 4, 6, 7, 8]],
    29: [[1, 4, 7, 8, 9], [1, 5, 6, 8, 9], [2, 3, 7, 8, 9], [2, 4, 6, 8, 9], [2, 5, 6, 7, 9], [3, 4, 5, 8, 9], [3, 4, 6, 7, 9], [3, 5, 6, 7, 8]],
    30: [[1, 5, 7, 8, 9], [2, 4, 7, 8, 9], [2, 5, 6, 8, 9], [3, 4, 6, 8, 9], [3, 5, 6, 7, 9], [4, 5, 6, 7, 8]],
    31: [[1, 6, 7, 8, 9], [2, 5, 7, 8, 9], [3, 4, 7, 8, 9], [3, 5, 6, 8, 9], [4, 5, 6, 7, 9]],
    32: [[2, 6, 7, 8, 9], [3, 5, 7, 8, 9], [4, 5, 6, 8, 9]],
    33: [[3, 6, 7, 8, 9], [4, 5, 7, 8, 9]],
    34: [[4, 6, 7, 8, 9]],
    35: [[5, 6, 7, 8, 9]]

}

cell_6 = {

    21: [[1, 2, 3, 4, 5, 6]],
    22: [[1, 2, 3, 4, 5, 7]],
    23: [[1, 2, 3, 4, 5, 8], [1, 2, 3, 4, 6, 7]],
    24: [[1, 2, 3, 4, 5, 9], [1, 2, 3, 4, 6, 8], [1, 2, 3, 5, 6, 7]],
    25: [[1, 2, 3, 4, 6, 9], [1, 2, 3, 4, 7, 8], [1, 2, 3, 5, 6, 8], [1, 2, 4, 5, 6, 7]],
    26: [[1, 2, 3, 4, 7, 9], [1, 2, 3, 5, 6, 9], [1, 2, 3, 5, 7, 8], [1, 2, 4, 5, 6, 8], [1, 3, 4, 5, 6, 7]],
    27: [[1, 2, 3, 4, 8, 9], [1, 2, 3, 5, 7, 9], [1, 2, 3, 6, 7, 8], [1, 2, 4, 5, 6, 9], [1, 2, 4, 5, 7, 8], [1, 3, 4, 5, 6, 8], [2, 3, 4, 5, 6, 7]],
    28: [[1, 2, 3, 5, 8, 9], [1, 2, 3, 6, 7, 9], [1, 2, 4, 5, 7, 9], [1, 2, 4, 6, 7, 8], [1, 3, 4, 5, 6, 9], [1, 3, 4, 5, 7, 8], [2, 3, 4, 5, 6, 8]],
    29: [[1, 2, 3, 6, 8, 9], [1, 2, 4, 5, 8, 9], [1, 2, 4, 6, 7, 9], [1, 2, 5, 6, 7, 8], [1, 3, 4, 5, 7, 9], [1, 3, 4, 6, 7, 8], [2, 3, 4, 5, 6, 9], [2, 3, 4, 5, 7, 8]],
    30: [[1, 2, 3, 7, 8, 9], [1, 2, 4, 6, 8, 9], [1, 2, 5, 6, 7, 9], [1, 3, 4, 5, 8, 9], [1, 3, 4, 6, 7, 9], [1, 3, 5, 6, 7, 8], [2, 3, 4, 5, 7, 9], [2, 3, 4, 6, 7, 8]],
    31: [[1, 2, 4, 7, 8, 9], [1, 2, 5, 6, 8, 9], [1, 3, 4, 6, 8, 9], [1, 3, 5, 6, 7, 9], [1, 4, 5, 6, 7, 8], [2, 3, 4, 5, 8, 9], [2, 3, 4, 6, 7, 9], [2, 3, 5, 6, 7, 8]],
    32: [[1, 2, 5, 7, 8, 9], [1, 3, 4, 7, 8, 9], [1, 3, 5, 6, 8, 9], [1, 4, 5, 6, 7, 9], [2, 3, 4, 6, 8, 9], [2, 3, 5, 6, 7, 9], [2, 4, 5, 6, 7, 8]],
    33: [[1, 2, 6, 7, 8, 9], [1, 3, 5, 7, 8, 9], [1, 4, 5, 6, 8, 9], [2, 3, 4, 7, 8, 9], [2, 3, 5, 6, 8, 9], [2, 4, 5, 6, 7, 9], [3, 4, 5, 6, 7, 8]],
    34: [[1, 3, 6, 7, 8, 9], [1, 4, 5, 7, 8, 9], [2, 3, 5, 7, 8, 9], [2, 4, 5, 6, 8, 9], [3, 4, 5, 6, 7, 9]],
    35: [[1, 4, 6, 7, 8, 9], [2, 3, 6, 7, 8, 9], [2, 4, 5, 7, 8, 9], [3, 4, 5, 6, 8, 9]],
    36: [[1, 5, 6, 7, 8, 9], [2, 4, 6, 7, 8, 9], [3, 4, 5, 7, 8, 9]],
    37: [[2, 5, 6, 7, 8, 9], [3, 4, 6, 7, 8, 9]],
    38: [[3, 5, 6, 7, 8, 9]],
    39: [[4, 5, 6, 7, 8, 9]]

}

cell_7 = {

    28: [[1, 2, 3, 4, 5, 6, 7]],
    29: [[1, 2, 3, 4, 5, 6, 8]],
    30: [[1, 2, 3, 4, 5, 6, 9], [1, 2, 3, 4, 5, 7, 8]],
    31: [[1, 2, 3, 4, 5, 7, 9], [1, 2, 3, 4, 6, 7, 8]],
    32: [[1, 2, 3, 4, 5, 8, 9], [1, 2, 3, 4, 6, 7, 9], [1, 2, 3, 5, 6, 7, 8]],
    33: [[1, 2, 3, 4, 6, 8, 9], [1, 2, 3, 5, 6, 7, 9], [1, 2, 4, 5, 6, 7, 8]],
    34: [[1, 2, 3, 4, 7, 8, 9], [1, 2, 3, 5, 6, 8, 9], [1, 2, 4, 5, 6, 7, 9], [1, 3, 4, 5, 6, 7, 8]],
    35: [[1, 2, 3, 5, 7, 8, 9], [1, 2, 4, 5, 6, 8, 9], [1, 3, 4, 5, 6, 7, 9], [2, 3, 4, 5, 6, 7, 8]],
    36: [[1, 2, 3, 6, 7, 8, 9], [1, 2, 4, 5, 7, 8, 9], [1, 3, 4, 5, 6, 8, 9], [2, 3, 4, 5, 6, 7, 9]],
    37: [[1, 2, 4, 6, 7, 8, 9], [1, 3, 4, 5, 7, 8, 9], [2, 3, 4, 5, 6, 8, 9]],
    38: [[1, 2, 5, 6, 7, 8, 9], [1, 3, 4, 6, 7, 8, 9], [2, 3, 4, 5, 7, 8, 9]],
    39: [[1, 3, 5, 6, 7, 8, 9], [2, 3, 4, 6, 7, 8, 9]],
    40: [[1, 4, 5, 6, 7, 8, 9], [2, 3, 5, 6, 7, 8, 9]],
    41: [[2, 4, 5, 6, 7, 8, 9]],
    42: [[3, 4, 5, 6, 7, 8, 9]]

}

cell_8 = {

    36: [[1, 2, 3, 4, 5, 6, 7, 8]],
    37: [[1, 2, 3, 4, 5, 6, 7, 9]],
    38: [[1, 2, 3, 4, 5, 6, 8, 9]],
    39: [[1, 2, 3, 4, 5, 7, 8, 9]],
    40: [[1, 2, 3, 4, 6, 7, 8, 9]],
    41: [[1, 2, 3, 5, 6, 7, 8, 9]],
    42: [[1, 2, 4, 5, 6, 7, 8, 9]],
    43: [[1, 3, 4, 5, 6, 7, 8, 9]],
    44: [[2, 3, 4, 5, 6, 7, 8, 9]]

}

cell_9 = {

    45: [[1, 2, 3, 4, 5, 6, 7, 8, 9]]

}

""" Class sudoku and all your features"""

import pandas as pd
import itertools
from cage_total_tables import *
from collections import OrderedDict


class Vertex():
    """Vertex structure"""

    def __init__(self, index=None, column=None, total=0):
        self.index = index
        self.column = column
        self.adjacents = []
        self.total = total

    def setIndex(self, index):
        self.index = index

    def getIndex(self):
        return self.index

    def setColumn(self, column):
        self.column = column

    def getColumn(self):
        return self.column

    def setAdjacents(self, vertex):
        self.adjacents.append(vertex)

    def getAdjacents(self):
        return self.adjacents

    def setTotal(self, total):
        self.total = total

    def getTotal(self):
        return self.total

    def getVerticesSum(self):
        return len(self.getAdjacents()) + 1

    def __str__(self):
        show = "Vertex: " + str(self.index) + ":" + str(
            self.column) + " with total = " + str(
            self.total) + " and adjacents:"
        for adj in self.getAdjacents():
            show = show + " " + str(adj.index) + ":" + str(adj.column)
        return show


class Killer_sudoku():
    """ Represent a sudoku table """

    def __init__(self):
        """Initialize atributes to describe sudoku"""

        # Create sudoku table
        self.table = {(x, y): 0 for x in range(1, 10) for y in range(1, 10)}
        self.cage_total_tables = {1: cell_1, 2: cell_2, 3: cell_3,
                                  4: cell_4, 5: cell_5, 6: cell_6,
                                  7: cell_7, 8: cell_8, 9: cell_9}
        self.re1 = {1: 0, 2: 0, 3: 0,
                    4: 3, 5: 3, 6: 3,
                    7: 6, 8: 6, 9: 6}
        self.re2 = {1: 1, 2: 1, 3: 1,
                    4: 2, 5: 2, 6: 2,
                    7: 3, 8: 3, 9: 3}

    def __str__(self):
        k_sudoku = ""
        for x in range(1, 10):
            for y in range(1, 10):
                k_sudoku = k_sudoku + str(self.table[(x, y)]) + " "
            k_sudoku = k_sudoku + "\n"
        return k_sudoku

    def readCSV(self, path):
        """Fill sudoku table from a csv file"""

        csv_file = pd.read_csv(path, header=-1)
        self.i_values = OrderedDict()  # killer sudoku initial values
        indexes = {"A": 1, "B": 2, "C": 3,
                   "D": 4, "E": 5, "F": 6,
                   "G": 7, "H": 8, "I": 9}

        pos = []  # positions
        for value in sorted(csv_file.values):
            pos.extend(value.item(0).split(";"))
            pos = sorted(pos)
            total = int(pos[0])
            index_r, column = indexes[pos[1][0]], int(pos[1][1])
            v = Vertex(index_r, column, total)
            for i in range(2, len(pos)):
                index, column = indexes[pos[i][0]], int(pos[i][1])
                adj = Vertex(index, column, total)
                v.setAdjacents(adj)
            if(index_r in self.i_values):
                self.i_values[index_r].append(v)
            else:
                self.i_values[index_r] = [v]
            pos.clear()

        self.i_lenght = sorted(self.i_values.keys())[-1]

    def solver(self, rows={1: set(), 2: set(), 3: set(),
                           4: set(), 5: set(), 6: set(),
                           7: set(), 8: set(), 9: set()},
               columns={1: set(), 2: set(), 3: set(),
                        4: set(), 5: set(), 6: set(),
                        7: set(), 8: set(), 9: set()},
               regions={1: set(), 2: set(), 3: set(),
                        4: set(), 5: set(), 6: set(),
                        7: set(), 8: set(), 9: set()},
               pos=1, v=0):
        """This function try to solve killer sudoku using cage total tables"""

        while True:
            if pos in self.i_values:
                vertex = self.i_values[pos][v]
                break
            else:
                pos += 1

        re_v = self.re1[vertex.index] + self.re2[vertex.column]
        length = len(self.i_values[pos])
        r = vertex.getVerticesSum()
        cage_table = self.cage_total_tables[r][vertex.total]

        for cage in cage_table:
            for comb in list(itertools.permutations(set(cage))):
                found = False

                self.table[(vertex.index, vertex.column)] = comb[0]

                r_length = len(rows[vertex.index])
                rows[vertex.index].add(comb[0])
                if(r_length == len(rows[vertex.index])):
                    continue

                c_length = len(columns[vertex.column])
                columns[vertex.column].add(comb[0])
                if(c_length == len(columns[vertex.column])):
                    rows[vertex.index].remove(comb[0])
                    continue

                re_length = len(regions[re_v])
                regions[re_v].add(comb[0])
                if(re_length == len(regions[re_v])):
                    rows[vertex.index].remove(comb[0])
                    columns[vertex.column].remove(comb[0])
                    continue

                next_comp = False
                for i, adj in enumerate(vertex.getAdjacents(), 1):

                    self.table[(adj.index, adj.column)] = comb[i]

                    r_length = len(rows[adj.index])
                    rows[adj.index].add(comb[i])
                    if(r_length == len(rows[adj.index])):
                        next_comp = True
                        rows[vertex.index].remove(comb[0])
                        columns[vertex.column].remove(comb[0])
                        regions[re_v].remove(comb[0])
                        for j, rem in zip(range(1, i + 1),
                                          vertex.getAdjacents()):
                            if(adj == rem):
                                break
                            re_m = self.re1[rem.index] + self.re2[rem.column]
                            rows[rem.index].remove(comb[j])
                            columns[rem.column].remove(comb[j])
                            regions[re_m].remove(comb[j])
                        break

                    c_length = len(columns[adj.column])
                    columns[adj.column].add(comb[i])
                    if(c_length == len(columns[adj.column])):
                        next_comp = True
                        rows[vertex.index].remove(comb[0])
                        columns[vertex.column].remove(comb[0])
                        regions[re_v].remove(comb[0])
                        for j, rem in zip(range(1, i + 1),
                                          vertex.getAdjacents()):
                            if(adj == rem):
                                rows[rem.index].remove(comb[j])
                                break
                            re_m = self.re1[rem.index] + self.re2[rem.column]
                            rows[rem.index].remove(comb[j])
                            columns[rem.column].remove(comb[j])
                            regions[re_m].remove(comb[j])
                        break

                    re = self.re1[adj.index] + self.re2[adj.column]
                    re_length = len(regions[re])
                    regions[re].add(comb[i])
                    if(re_length == len(regions[re])):
                        next_comp = True
                        rows[vertex.index].remove(comb[0])
                        columns[vertex.column].remove(comb[0])
                        regions[re_v].remove(comb[0])
                        for j, rem in zip(range(1, i + 1),
                                          vertex.getAdjacents()):
                            if(adj == rem):
                                rows[rem.index].remove(comb[j])
                                columns[rem.column].remove(comb[j])
                                break
                            re_m = self.re1[rem.index] + self.re2[rem.column]
                            rows[rem.index].remove(comb[j])
                            columns[rem.column].remove(comb[j])
                            regions[re_m].remove(comb[j])
                        break
                    else:
                        found = True

                if(next_comp):
                    continue

                if(found):
                    ahead = True
                    if(v < length - 1):
                        ahead = self.solver(
                            rows, columns, regions, pos, v=v + 1)
                        if(ahead == "Complete"):
                            return "Complete"

                    if(ahead):
                        if(pos < self.i_lenght):
                            ahead = self.solver(
                                rows, columns, regions, pos=pos + 1, v=0)
                            if(ahead == "Complete"):
                                return "Complete"
                        else:
                            return "Complete"

                    if(not ahead):
                        rows[vertex.index].remove(comb[0])
                        columns[vertex.column].remove(comb[0])
                        regions[re_v].remove(comb[0])
                        for i, adj in enumerate(vertex.getAdjacents(), 1):
                            rows[adj.index].remove(comb[i])
                            columns[adj.column].remove(comb[i])
                            re = self.re1[adj.index] + self.re2[adj.column]
                            regions[re].remove(comb[i])
                else:
                    return False

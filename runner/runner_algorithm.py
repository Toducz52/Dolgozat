import copy
from builder_method.build_algorithm import build_algorithm_method
from graph_data.result_graph import Result_graph
from graph_data.result_run import Result_run
from PySide2.QtWidgets import QMessageBox
from graph_data.run_property import Run_property
import networkx as nx
from collections import OrderedDict
from itertools import permutations
import functools
import random
import time
import inspect
import sys
from util.util_graph_helper import is_coloring_specified_color_number

def create_msg_box(text, details):
    msg_box = QMessageBox()
    msg_box.setText(text)
    msg_box.setInformativeText("")
    msg_box.setDetailedText(details)
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.exec_()


def attrsToString(G, prop, name, isArray):
    weigth = nx.get_edge_attributes(G, prop)
    weigth = OrderedDict(sorted(weigth.items(), key=lambda x: x[1]))
    G_ = functools.reduce((lambda x, y: x + y), weigth.values(), 0)
    if isArray:
        return 'GSum(' + name + '): ' + str(G_) + ' -> ' + str(weigth)
    else:
        return 'GSum(' + name + '): ' + str(G_)


def all_perms(my_list):
    if len(my_list) <= 1:
        yield my_list
    else:
        for perm in all_perms(my_list[1:]):
            for i in range(len(perm) + 1):
                yield perm[:i] + my_list[0:1] + perm[i:]

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def summation(G, G2):

    elist = [(u, v, d) for (u, v, d) in G.edges(data=True)]

    for n1, n2, props in elist:
        for key, value in props.items():
            if n1 in G2 and n2 in G2:
                # ez a kod valamiert nem mukodott
                # if key in G2[n1][n2]:
                #     G2[n1][n2][key] += value
                # else:
                #     G2[n1][n2][key] = value
                try:
                    G2[n1][n2][key] += value
                except:
                    try:
                        G2[n1][n2][key] = value
                    except:
                        G2.add_edge(n1, n2)
                        G2[n1][n2][key] = value
            else:
                G2.add_edge(n1, n2)
                G2[n1][n2][key] = value

    return G2


class Runner_algorithm:

    @classmethod
    def run_simple(cls, alg_content: Run_property, result):

        alg = alg_content.alg

        alg.call_algorithm()

        result.add_result_graph(Result_graph(alg.graph, alg.args))

    @classmethod
    def run_all_permutation(cls, alg_content: Run_property, result):

        alg = alg_content.alg
        n = alg_content.array_size
        array_name = alg_content.array_name

        array = list(range(1, int(n) + 1))

        all_permutation = all_perms(array)

        for arr in  all_permutation:

            alg.args[array_name] = arr
            arg_copy = copy.deepcopy(alg.args)
            del alg.graph
            alg.graph = nx.Graph()
            alg.call_algorithm()
            result.add_result_graph(Result_graph(alg.graph, arg_copy))

    @classmethod
    def run_all_permutation_sum(cls, alg: Run_property, result_run):

        cls.run_all_permutation(alg, result_run)

        sum_graph = nx.Graph()

        for results_graph in [o.graph for o in result_run.result]:
            sum_graph = summation(sum_graph, results_graph)

        result_run.clear_result()
        result_run.add_result_graph(Result_graph(sum_graph, alg.args))

    @classmethod
    def run_random_array(cls, alg_content: Run_property, result):



        alg = alg_content.alg
        n = alg_content.array_size
        array_name = alg_content.array_name

        alg.args[array_name] = list(range(1, int(n) + 1))
        random.shuffle(alg.args[array_name])

        alg.call_algorithm()

        result.add_result_graph(Result_graph(alg.graph, alg.args))

    @classmethod
    def run_drawing_with_colors(cls, alg: Run_property, result_run: Result_run):

        if len(result_run.result) == 0:
            raise Exception("Nincs eredmény tömb.")

        ok_result = []

        for result in result_run.result:
            graph = result.graph
            if is_coloring_specified_color_number(graph, alg.color_number, alg.graph_name):
                ok_result.append(result)

        result_run.swap_result(ok_result)

mapping = {
    'run_simple': Runner_algorithm.run_simple,
    'run_all_permutation': Runner_algorithm.run_all_permutation,
    'run_all_permutation_sum': Runner_algorithm.run_all_permutation_sum,
    'run_random_array': Runner_algorithm.run_random_array,
    'run_drawing_with_colors': Runner_algorithm.run_drawing_with_colors
}


def start(controller_function_name, run_property: Run_property, result):

    mapping[controller_function_name](run_property, result)

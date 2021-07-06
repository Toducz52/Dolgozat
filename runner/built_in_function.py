import functools
import random
import time
# from networkx.algorithms.approximation import clique
import traceback
from collections import OrderedDict
from itertools import permutations

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from networkx.algorithms import approximation as apxa
from networkx.algorithms import clique


class Built_in_function:

    def __int__(self):
        pass

    @classmethod
    def addAttrsToGraph(cls, G, n1, n2, prop, value):
        if not G.has_edge(n1, n2):
            try:
                G.add_edge(n1, n2)
                G[n1][n2][prop] = value
            except Exception as ex:
                traceback.print_exc()
                raise ex
        else:
            if prop in G[n1][n2]:
                G[n1][n2][prop] = G[n1][n2][prop] + value
            else:
                G[n1][n2][prop] = value


    def test(self, text):
        print(text)




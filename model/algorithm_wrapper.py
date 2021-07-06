from runner.built_in_function import *
import networkx as nx
from util.my_time import Timer
from datetime import datetime
from util.util_regex import *


class Function_call:

    def __str__(self):
        return f"{self._v1} {self._v2} {self._prop} {self.start} {self.end}"

    def __init__(self, v1, v2, prop, start=None, end=None):
        self.end = end
        self.v1 = v1
        self.v2 = v2
        self.prop = prop
        self.start = start

    @property
    def v1(self):
        return self._v1

    @v1.setter
    def v1(self, value):
        if is_valid_node_name(value):
            self._v1 = value
        else:
            raise ValueError("csomopont 1 nem megfelelő.")

    @property
    def v2(self):
        return self._v2

    @v2.setter
    def v2(self, value):
        if is_valid_node_name(value):
            self._v2 = value
        else:
            raise ValueError("csomopont 2 nem megfelelő")

    @property
    def prop(self):
        return self._prop

    @prop.setter
    def prop(self, value):
        if is_valid_parameter_name(value):
            self._prop = value
        else:
            raise ValueError("a tulajdonság nem megfelelő")


class Algorithm_wrapper:
    """ simple sort class """

    built_in_methods = Built_in_function()

    def EL_BESZURAS(self, csomopont1, csomopont2, graf):
        self.built_in_methods.addAttrsToGraph(self.graph, csomopont1, csomopont2, graf, 1)

    def __init__(self):

        self.graph = nx.Graph()
        # self.graph_compare = nx.Graph()
        # self.graph_swap = nx.Graph()
        # self.graph_compare_sum = nx.Graph()
        # self.graph_swap_sum = nx.Graph()
        self.timer = Timer()
        self.args = {}
        self.function_name = None
        self.code = None
        self.save_name = None
        self.create_date = datetime.today().strftime('%Y-%m-%d-%H:%M')
        self.update_date = None
        self.readme = None
        self.function_call = []

    def initialization(self, save_name, function_name, readme, code, function_call, args=None,
                       create_date=None, update_date=None):

        if create_date is not None:
            self.create_date = create_date
        self.save_name = save_name
        self.function_call = function_call
        self.function_name = function_name
        if update_date is not None:
            self.update_date = update_date
        self.readme = readme
        self.code = code
        self.args = args
        return self

    def __str__(self):
        return f"""
        {self.function_name}
        {self.code}
        {self.save_name}
        {self.create_date}
        {self.update_date}
        {self.args}
        {self.readme}
        {self.function_call}"""

    def alma(self):
        pass
        # print("Endi")

    def algorithm(self) -> None:
        pass

    def call_algorithm(self):
        self.timer.start()
        # print(self.args)

        self.algorithm(**self.args)

        self.timer.stop()



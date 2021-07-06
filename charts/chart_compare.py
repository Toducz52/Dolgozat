from charts.mpl_widget import *
from matplotlib.widgets import Slider
from collections import OrderedDict
import itertools
from matplotlib.ticker import MaxNLocator
from charts.chart import *
import copy

class Chart_compare(Bar_chart_edge_numbers):

    def draw_(self, result_graph, fig, run_property):
        G = result_graph.graph

        self.weigth = nx.get_edge_attributes(G, self.prop)
        edges_sorted = OrderedDict(sorted(self.weigth.items(), key=lambda x: x[1], reverse=True))
        weigth_sorted = [w for w in edges_sorted.values()]
        edges_sorted_list = list(edges_sorted)
        self.labels = list(map(lambda x: f"({x[0]},{x[1]})", edges_sorted_list))

        self.y = weigth_sorted

        self.ax = fig.gca()

        try:
            weigth2 = nx.get_edge_attributes(self.result2.result[self.parent.current_index].graph, self.prop)
        except:
            weigth2 = []

        self.y2 = []

        weigth2_copy = copy.deepcopy(weigth2)


        for key, value in edges_sorted.items():
            if key in weigth2_copy:
                self.y2.append(weigth2_copy[key])
                del weigth2_copy[key]
            else:
                key = (key[1], key[0])
                if key in weigth2_copy:
                    self.y2.append(weigth2_copy[key])
                    del weigth2_copy[key]
                else:
                    self.y2.append(0)

        if weigth2:
            for key, value in weigth2_copy.items():
                self.y2.append(value)
                self.y.append(0)
                self.labels.append(f"({key[0]},{key[1]})")

        self.ax.set_title(str(sum(self.y)))

        self.N = 20 if len(weigth_sorted) >= 20 else len(weigth_sorted)

        self.x = range(0, len(self.y))

        self.max_ = max(self.y) if self.y is not None and len(self.y) != 0 else 1
        max_2 = max(self.y2) if self.y2 is not None and len(self.y2) != 0 else 1
        self.max_ = max(self.max_, max_2)

        self.yticks = get_y_ticks(self.max_)

        self.barpos = plt.axes([0.18, 0.05, 0.55, 0.03], facecolor="skyblue")
        self.slider = Slider(self.barpos, 'Barpos', 0, len(self.y) - self.N, valinit=0)
        self.slider.on_changed(self.bar)

        self.bar(0)

    def bar(self, pos):
        pos = int(pos)

        self.ax.clear()

        if pos + self.N > len(self.y2):
            self.n = len(self.x) - pos
        else:
            self.n = self.N

        n = self.n

        # self.ax.axis([pos - self.N + n, pos + n + 2, 0, self.max_])
        self.ax.set_xlim([pos - self.N + n, pos + n + 2])
        self.ax.set_ylim([0, self.yticks[-1]])
        self.ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        # self.ax.set_yticks(list(range(0, self.max_)))

        # self.ax.set_yticks(self.yticks)
        self.ax.get_xaxis().set_visible(False)

        X = self.x[pos:pos + n]
        Y = self.y[pos:pos + n]
        Y2 = self.y2[pos:pos + n]

        print(X)
        print(Y)
        print(Y2)

        self.ax.bar(X, Y, self.width)

        X1 = list(map(lambda x: x + self.width, X))

        self.ax.bar(X1, Y2, self.width, color=list(plt.rcParams['axes.prop_cycle'])[2]['color'])

        for i in range(pos, pos + n):
            # print(i)
            self.ax.annotate(self.labels[i], (self.x[i], self.y[i]))









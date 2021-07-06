from charts.mpl_widget import *
from matplotlib.widgets import Slider
from collections import OrderedDict
import itertools
from matplotlib.ticker import MaxNLocator


def get_y_ticks(max):
    div = 1

    if max > 30:
        for x in itertools.count(start=1):
            if max / x < 30:
                div = x
                break

    return list(range(0, max + div * 2, div))

class Bar_chart_edge_numbers(MplWidget):

    def bar(self, pos):

        pos = int(pos)

        self.ax.clear()

        if pos + self.N > len(self.weigth):
            self.n = len(self.x) - pos
        else:
            self.n = self.N

        n = self.n

        #self.ax.axis([pos - self.N + n, pos + n + 2, 0, self.max_])
        self.ax.set_xlim([pos - self.N + n, pos + n + 2])
        self.ax.set_ylim([0, self.yticks[-1]])
        self.ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        # self.ax.set_yticks(list(range(0, self.max_)))

        # self.ax.set_yticks(self.yticks)
        self.ax.get_xaxis().set_visible(False)

        X = self.x[pos:pos + n]
        Y = self.y[pos:pos + n]

        self.ax.bar(X, Y, width=self.width, align='edge', color='green', ecolor='black')

        for i in range(pos, pos + n):
            # print(i)
            self.ax.annotate(self.labels[i], (self.x[i], self.y[i]))

    def draw_(self, result_graph, fig, run_property):

        G = result_graph.graph

        self.weigth = nx.get_edge_attributes(G, self.prop)

        edges_sorted = OrderedDict(sorted(self.weigth.items(), key=lambda x: x[1], reverse=True))
        weigth_sorted = [w for w in edges_sorted.values()]
        edges_sorted_list = list(edges_sorted)
        self.labels = list(map(lambda x: f"({x[0]},{x[1]})", edges_sorted_list))

        self.y = weigth_sorted

        self.x = range(0, len(self.y))

        self.ax = fig.gca()

        self.ax.set_title(str(sum(self.y)))

        self.N = 20 if len(weigth_sorted) >= 20 else len(weigth_sorted)

        self.max_ = max(weigth_sorted) if weigth_sorted is not None and len(weigth_sorted) != 0 else 1

        self.yticks = get_y_ticks(self.max_)

        self.barpos = plt.axes([0.18, 0.05, 0.55, 0.03], facecolor="skyblue")
        self.slider = Slider(self.barpos, 'Barpos', 0, len(self.weigth) - self.N, valinit=0)
        self.slider.on_changed(self.bar)

        self.bar(0)

    def __init__(self, parent, run_property):
        super().__init__(parent, run_property)
        self.width = 0.25
        self.n = None


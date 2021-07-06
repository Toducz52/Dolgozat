import functools
from collections import OrderedDict

import networkx as nx
import matplotlib.pyplot as plt


def addAttrsToGraph(G, n1, n2, prop, value):
    if not G.has_edge(n1, n2):
        G.add_edge(n1, n2)
        G[n1][n2][prop] = value
    else:
        G[n1][n2][prop] = G[n1][n2][prop] + value


def plotGraph(G, plot, figureName, text):
    plt.axis("off")
    plot.append(plt.figure(len(plot)))
    plot[len(plot) - 1].suptitle(figureName)
    ax = plot[len(plot) - 1].add_subplot(111)
    ax.set_title(text)
    elist = [(u, v) for (u, v, d) in G.edges(data=True)]
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=150)
    nx.draw_networkx_edges(G, pos, edgelist=elist, width=0.5)
    nx.draw_networkx_labels(G, pos, font_size=11, font_family="sans-serif")
    plt.show(block=False)


def plotGraphWithLabels(G, plot, figureName, text):
    plt.axis("off")
    plot.append(plt.figure(len(plot)))
    plot[len(plot) - 1].suptitle(figureName)
    ax = plot[len(plot) - 1].add_subplot(111)
    ax.set_title(text)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, edge_color='black', width=1, linewidths=1,
            node_size=100, node_color='pink', alpha=0.9,
            labels={node: node for node in G.nodes()})
    labels = nx.get_edge_attributes(G, 'weigth')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red')
    plt.show()


def attrsToString(G, prop, name, isArray):
    weigth = nx.get_edge_attributes(G, prop)
    # print(weigth)
    weigth = OrderedDict(sorted(weigth.items(), key=lambda x: x[1]))
    G_ = functools.reduce((lambda x, y: x + y), weigth.values(), 0)
    if isArray:
        return 'GSum(' + name + '): ' + str(G_) + ' -> ' + str(weigth)
    else:
        return 'GSum(' + name + '): ' + str(G_)


def graph_edge_ordered(graph, prop) -> OrderedDict:
    weigth = nx.get_edge_attributes(graph, prop)
    return OrderedDict(sorted(weigth.items(), key=lambda x: x[1]))


def separate_graph_with_attr(g, prop):
    g_new = nx.Graph()

    if g is None:
        return g_new

    for (u, v, d) in g.edges(data=True):
        if prop in d:
            g_new.add_edge(u, v)
            g_new[u][v][prop] = d[prop]

    return g_new


def is_coloring_specified_color_number(graph, color_number, graph_name):
    graph_ = separate_graph_with_attr(graph, graph_name)

    d = nx.coloring.greedy_color(graph_, strategy='connected_sequential_dfs')
    v = d.values()

    if color_number < max(d.values()):
        return False

    return True


from charts.chart_number_of_edge_of_node import *

# egy csomopont eleinek sulyainak osszege
class Chart_sum_of_edge_prop_of_one_node(Chart_number_of_edge_of_node):

    def draw_(self, widget):
        graph = self.result_graph.graph

        prop = self.prop

        widget.set0 = QtCharts.QBarSet(str("count of edge"))

        count_of_edge_of_node = {}

        max_value = 0

        for node in self.nodes:
            edge_list = graph.edges(node)
            count = 0
            for edge in edge_list:
                if prop in graph[edge[0]][edge[1]] is not None:
                    count += graph[edge[0]][edge[1]][prop]
            max_value = count if count > max_value else max_value
            count_of_edge_of_node[node] = count

        sort_orders = sorted(count_of_edge_of_node.items(), key=lambda x: x[1], reverse=True)

        widget.categories = []

        for key, value in sort_orders:
            widget.set0.append(value)
            widget.categories.append(key)

        widget.barSeries = QtCharts.QBarSeries(widget)
        widget.barSeries.append(widget.set0)

        widget.chart = QtCharts.QChart()
        widget.chart.addSeries(widget.barSeries)

        widget.axisX = QtCharts.QBarCategoryAxis()
        widget.axisX.append(widget.categories)

        widget.chart.setAxisX(widget.axisX, widget.barSeries)
        # widget.axisX.setRange("Jan", "Jun")

        widget.axisY = QtCharts.QValueAxis()
        widget.axisY.setTickInterval(1)
        # widget.axisY.setRange(0, max_value + 2)
        widget.chart.setAxisY(widget.axisY, widget.barSeries)


        # widget.axisY.setLabelFormat("%.0f")

        if self.run_property.array_name is not None:
            arr = self.result_graph.args[self.run_property.array_name]
            self.chart.setTitle(arrayToString(arr))

        widget.chart.legend().setVisible(True)
        widget.chart.legend().setAlignment(Qt.AlignBottom)

        widget.chartView = QtCharts.QChartView(widget.chart)
        widget.chartView.setRenderHint(QPainter.Antialiasing)


def create_new_line(v1, v2, my_type):
    """self.built_in_methods.addAttrsToGraph(self.graph_compare, arr[j], arr[j + 1], 'weigth', 1)"""
    # return f"self.built_in_methods.addAttrsToGraph(self.graph, {v1}, {v2}, \'{my_type}\', 1)"
    return f"EL_BESZURAS(csomopont1={v1}, csomopont2={v2}, graf=\'{my_type}\')"
    # return f"addAttrsToGraph(self.graph_compare, {v1}, {v2}, {my_type}, 1)"


def addNewLineToCode(code, number_of_line, line):
    lines = code.split('\n')
    list.insert(lines, number_of_line, line)
    new_line = ''
    for index in range(0, len(lines) - 1):
        new_line = new_line + lines[index] + '\n'

    return new_line + lines[len(lines) - 1]

import copy


class Result_run_simple:
    def __init__(self, result_run):
        self.result = copy.deepcopy(result_run.result)
        self.run_property = copy.deepcopy(result_run.run_property)


from model.algorithm_wrapper import Algorithm_wrapper
from types import FunctionType
from util.util_result import Result
from util.util_mainwindow import get_parameter_list_and_f_name_in_f_header


def contained_self_parameter_in_code(code):
    head = code.split('\n')[0]
    result = get_parameter_list_and_f_name_in_f_header(head)
    if result[1][0] == 'self':
        return True
    else:
        return False


def create_new_header(function_name, parameter_list):

    parameters = ''
    for p in parameter_list:
        parameters += p + ','
    parameters = parameters[:-1]

    header = f"def {function_name}({parameters}):\n"

    return header


def change_header(code):
    header = code.split('\n')[0]
    result = list(get_parameter_list_and_f_name_in_f_header(header))
    result[1] = ['self'] + result[1]
    code_definition = code[len(header) + 1:]
    new_header = create_new_header(*result)
    return new_header + code_definition


def build_algorithm_method(alg: Algorithm_wrapper):

    code = alg.code

    if not contained_self_parameter_in_code(alg.code):
        code = change_header(alg.code)

    code = code.replace("EL_BESZURAS", "self.EL_BESZURAS")

    try:
        f_code = compile(code, 'algorithm', "exec")
        f_func = FunctionType(f_code.co_consts[0], globals(), 'algorithm')
    except Exception as er:
        return Result.Fail(er)

    setattr(Algorithm_wrapper, "algorithm", f_func)

    return Result.Ok(alg)

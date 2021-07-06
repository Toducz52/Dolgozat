from util.util_regex import first_match


def get_parameter_list_and_f_name_in_f_header(function_header: str):

    function_header_rest = function_header[4:]
    function_name = first_match(function_header_rest, "[a-zA-Z0-9_]+")

    function_header_rest = first_match(function_header_rest, "\([a-zA-Z0-9_,]+\)")
    function_header_rest = function_header_rest[1:]
    function_header_rest = function_header_rest[:-1]
    parameter_list = function_header_rest.split(',')

    return function_name, parameter_list

#
# import re
#
#
# def check_regex(reg, txt):
#     x = re.fullmatch(reg, txt)
#     return True if x else False
#
#
# def is_valid_function_head(function_head):
#     reg = r"\s*def\s+[a-zA-Z][a-zA-Z0-9]+\s*\(([a-zA-z][a-zA-z0-9]*,\s*)*([a-zA-z][a-zA-z0-9]*)\):\n"
#     return check_regex(reg, function_head)
#
#
# def is_valid_function_name(function_name):
#     reg = r"[a-zA-Z][a-zA-Z0-9_]*"
#     return check_regex(reg, function_name)
#
#
# def is_valid_parameter_name(function_name):
#     reg = r"[a-zA-Z][a-zA-Z0-9_\[\]]*"
#     return check_regex(reg, function_name)
#
#
# def first_match(line, regExpression):
#     reg = re.compile(regExpression)
#     r = reg.search(line)
#     return r.group(0) if r else None
#
#
# code = \
#     '''def bubbleSort(self, arr,n):
#          self.alma()
#          for i in range(n-1):
#              for j in range(0, n-i-1):
#                  if arr[j] > arr[j+1]:
#                      arr[j], arr[j+1] = arr[j+1], arr[j]
#     '''
#
#
# def get_parameter_list_and_f_name_in_f_header(function_header: str):
#     function_header_rest = function_header[4:]
#     function_name = first_match(function_header_rest, "[a-zA-Z0-9_]+")
#     print(function_header_rest)
#     print(function)
#     function_header_rest = first_match(function_header_rest, "\([a-zA-Z0-9_,]+\)")
#     print(function_header_rest)
#     function_header_rest = function_header_rest[1:]
#     function_header_rest = function_header_rest[:-1]
#     parameter_list = function_header_rest.split(',')
#
#     return function_name, parameter_list
#
#
# def contained_self_parameter_in_code(code):
#     header = code.split('\n')[0]
#     print(header)
#     result = get_parameter_list_and_f_name_in_f_header(header)
#     if result[1][0] == 'self':
#         return True
#     else:
#         return False
#
#
# def add_function_head_to_code(function_name, parameter_list):
#     parameters = ''
#     for p in parameter_list:
#         parameters += p + ','
#     parameters = parameters[:-1]
#
#     header = f"def {function_name}({parameters}):\n"
#
#     return header
#
#
# def change_header(code):
#     header = code.split('\n')[0]
#     print(header)
#     result = get_parameter_list_and_f_name_in_f_header(head)
#     new_header = add_function_head_to_code(*result)
#     print(header)
#
#
# ##if
# contained_self_parameter_in_code(code)
# ##    change_header(code)
#
#

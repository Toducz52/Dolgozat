import re


def check_regex(reg, txt):
    x = re.fullmatch(reg, txt)
    return True if x else False


def is_valid_function_head(function_head):
    reg = r"\s*def\s+[a-zA-Z][a-zA-Z0-9]+\s*\(([a-zA-z][a-zA-z0-9]*,\s*)*([a-zA-z][a-zA-z0-9]*)\):\n"
    return check_regex(reg, function_head)


def is_valid_function_name(function_name):
    reg = r"[a-zA-Z][a-zA-Z0-9_]*"
    return check_regex(reg, function_name)


def is_valid_parameter_name(parameter_name):
    reg = r"[a-zA-Z][a-zA-Z0-9_\[\]]*"
    return check_regex(reg, parameter_name)


def is_valid_node_name(node_name):
    if node_name == "":
        return False
    else:
        return True

def first_match(line, regExpression):
    reg = re.compile(regExpression)
    r = reg.search(line)
    return r.group(0) if r else None

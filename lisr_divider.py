# Разделитель списков

"""Идея в том, что можно найти index разделителя, и сделать срезы от него в разные стороны.
"""

def split_list(some_list: list, divider):
    if not isinstance(some_list, list):
        return "Это не список"
    elif divider not in some_list:
        return some_list
    else:
        return (
            some_list[:some_list.index(divider)], 
            some_list[some_list.index(divider)+1:]
        )

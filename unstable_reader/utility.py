def remove_quotes(string):
    return str(string).replace('"', "").replace("'", "")


def add_quotes(string):
    return f'"{str(string)}"'


def concat_strings(base, addition, separator=", "):
    return f"{base}{separator}{addition}" if base else addition


def merge_dict(dict1, dict2):
    dict3 = dict1.copy()
    for k, v in dict2.items():
        dict3[k] = merge_str_to_tuple(v, dict3[k]) if k in dict3 else v
    return dict3


def merge_str_to_tuple(item1, item2):
    if not isinstance(item1, tuple):
        item1 = (item1,)
    if not isinstance(item2, tuple):
        item2 = (item2,)
    return item1 + item2
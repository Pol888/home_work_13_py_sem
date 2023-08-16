h = {1: 2, 4: 5}


def get_2(d: dict, key, default_val=None):
    try:
        return d[key]
    except KeyError:
        return default_val


print(get_2(h, 0, 9))

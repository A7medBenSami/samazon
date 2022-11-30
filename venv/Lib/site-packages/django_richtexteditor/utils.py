def recursive_update(default, custom):
    """A recursive version of Python dict#update"""
    if not isinstance(default, dict) or not isinstance(custom, dict):
        raise TypeError('Params of recursive_update() must be a dictionnaries.')

    for key in custom:
        if isinstance(custom[key], dict) and isinstance(
                default.get(key), dict):
            default[key] = recursive_update(default[key], custom[key])
        else:
            default[key] = custom[key]

    return default

def key_from_configdict(d):
    """Return key (the most inner first item) of a config dictionnary"""
    if not isinstance(d, dict):
        raise TypeError('Params of key_from_configdict() must be a dictionnary.')
    try:
        item = [k for k, v in d.items()][0]
    except IndexError:
        item = ''
    return item

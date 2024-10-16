
def format_names(names=[]):
    """
    This function takes a list of names as input and returns a list of formatted names.
    The function will capitalize the first letter of each name, replace underscores with spaces,
    and return the formatted names.
    """
    nlist = []
    for name in names:
        name = name.replace('_',' ')
        nlist.append(name[0].upper() + name[1:])
    return nlist
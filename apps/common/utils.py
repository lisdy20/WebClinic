
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

def model_or_none(*,model,pk):
    """
    This function checks if a specific model and primary key exist in the database.
    If the model and primary key exist, it returns Model instance; otherwise, it returns None.
    """
    try:
        instance = model.objects.get(pk=pk)
        return instance
    except model.DoesNotExist:
        return None
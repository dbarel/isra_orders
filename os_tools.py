import os


def find_exl_file_in_dir(where: str = os.getcwd()) -> str:
    """return xl file name in dir"""
    ls = os.listdir(where)
    xl_file = None
    for item in ls:
        if item.endswith('.xlsx'):
            if xl_file:
                raise FileExistsError("there is more than 1 .xlsx file in this folder, move the unnecessary to anther "
                                      "folder")
            else:
                xl_file = item
    if not xl_file:
        raise FileNotFoundError("there is no .xlsx in this folder")
    return xl_file

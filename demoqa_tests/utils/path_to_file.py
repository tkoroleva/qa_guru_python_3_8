import os


def define_path(name_file):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__),
                     os.path.pardir, os.path.pardir, name_file))

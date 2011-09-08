import os
import sys

init_content = """from .base import *

try:
    from .local import *
except ImportError:
    pass
"""

def get_project_dir():
    dir_list = os.path.abspath(__file__).split('/')[:-1]
    return '/'.join(dir_list)

def make_it_so():
    """
    Read the current default settings.py into memory.
    Create the settings directory.
    Create the basic __init__.py file which imports base.py and looks
    for local.py.
    Write settings to base.py.
    Clean up and dump the old settings.py and the pyc file if it exists.
    """
    PROJECT_PATH = get_project_dir()

    if os.path.exists(PROJECT_PATH + '/settings'):
        raise Exception("A settings directory already exists.")

    try:
        settings = open(PROJECT_PATH + '/settings.py', 'r')
    except IOError:
        raise Exception("Cannot open your default settings file.")

    try:
        os.makedirs(PROJECT_PATH + '/settings')
    except Error:
        raise Exception("Could not create the settings folder.")

    try:
        init = open(PROJECT_PATH + '/settings/__init__.py', 'wb')
        init.write(init_content)
        init.close()
    except IOError:
        raise IOError("Could not create the __init__.py file.")

    try:
        base = open(PROJECT_PATH + '/settings/base.py', 'wb')
        base.write(settings.read())
        base.close()
        settings.close()
    except IOError:
        raise IOError("WTF")

    try:
        os.remove(PROJECT_PATH + '/settings.py')
    except OSError:
        raise OSError("Cannot delete the default settings file.")

    try:
        os.remove(PROJECT_PATH + '/settings.pyc')
    except OSError:
        pass

    try:
        local = open(PROJECT_PATH + '/settings/local.py', 'wb')
        local.write('# your local dev settings go here.')
        local.close()
    except IOError:
        raise IOError("Cannot write local.py file.")

    sys.stdout.write("Your settings are now a little more awesome.\n")


if __name__ == '__main__':
    make_it_so()

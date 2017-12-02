import sys
import pydevd


def set_debug_environment():
    # requires to have pycharm-debug-py3k.egg file in the same directory
    sys.path.append('pycharm-debug-py3k.egg')
    pydevd.settrace('localhost', port=4444, stdoutToServer=True, stderrToServer=True)

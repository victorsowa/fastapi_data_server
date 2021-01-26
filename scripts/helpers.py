import os
from datetime import datetime


def get_last_modified_time(filename):
    return os.path.getmtime(filename)

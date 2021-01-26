import os
from datetime import datetime
import json

import pandas as pd


def get_last_modified_time(filename):
    return os.path.getmtime(filename)


def parse_csv(filename):
    df = pd.read_csv(filename)
    df_json = df.to_json()
    return json.loads(df_json)

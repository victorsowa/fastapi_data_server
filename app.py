import os
import json

from fastapi import FastAPI
import pandas as pd

from scripts.helpers import get_last_modified_time


app = FastAPI()


@app.get("/")
def get_available_data():
    return os.listdir('data/')


@app.get("/get_data/{filename}")
def get_data(filename):
    df_from_file = pd.read_csv(f'data/{filename}')
    df_json_string = df_from_file.to_json()

    modified_time = get_last_modified_time(f'data/{filename}')

    return {
        'lastModified': modified_time,
        'data': json.loads(df_json_string)}

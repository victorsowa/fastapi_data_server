import os

from fastapi import FastAPI

from scripts.helpers import (get_last_modified_time,
                             parse_csv)


app = FastAPI()
DATA_DIRECTORY = 'data'


@app.get("/")
def get_available_data():
    return os.listdir('data/')


@app.get("/get_data/{filename}")
def get_data(filename):
    file_path = os.path.join(DATA_DIRECTORY, filename)
    parsed_csv = parse_csv(file_path)

    modified_time = get_last_modified_time(file_path)

    return {
        'lastModified': modified_time,
        'data': parsed_csv}

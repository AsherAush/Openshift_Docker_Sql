from fastapi import FastAPI
from dal import get_data

app = FastAPI()

@app.get("/data")
def read_data():
    return get_data()
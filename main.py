from fastapi import FastAPI
import json

app = FastAPI()

def load_config():
    with open("patients.json") as config_file:
        config = json.load(config_file)
    return config

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/about")
def about():
    return {"About": "This is a FastAPI application."} 

@app.get("/view")
def view_patients():
    data = load_config()
    return data
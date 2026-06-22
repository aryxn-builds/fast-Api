from fastapi import FastAPI , Path , HTTPException , Query
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


@app.get("/patients/{patient_id}")
def view_patient(patient_id: str = Path(..., description="ID of the patient in the DB", example="P001")):
    # load all data of the patients
    data = load_config()
    # check if the patient id exists in the data
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    
@app.get("/sort")
def sort_patients(sort_by : str = Query(..., description="Sort on the basis of height , weight or bmi "), order: str = Query("asc", description="Order of sorting: asc or desc")):
    data = load_config()
    if sort_by not in ["height", "weight", "bmi"]:
        raise HTTPException(status_code=400, detail="Invalid sort_by value. Must be 'height', 'weight', or 'bmi'.")
    
    sorted_data = sorted(data.items(), key=lambda x: x[1][sort_by], reverse=(order == "desc"))
    return {patient_id: details for patient_id, details in sorted_data}
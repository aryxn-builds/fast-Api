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



#  adding a new endpoint to view a specific patient by ID called path parameter. The endpoint will be /patients/{patient_id} and will return the details of the patient if found, or a 404 error if not found.


@app.get("/patients/{patient_id}")
def view_patient(patient_id: str = Path(..., description="ID of the patient in the DB", example="P001")):
    # load all data of the patients
    data = load_config()
    # check if the patient id exists in the data
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404, detail="Patient not found")
    
  
  
# adding a new endpoint to sort the patients based on height, weight or bmi. The endpoint will be /sort and will accept two query parameters: sort_by and order. The sort_by parameter will specify the attribute to sort by (height, weight, or bmi), and the order parameter will specify the order of sorting (asc or desc). The endpoint will return the sorted list of patients.  
@app.get("/sort")

def sort_patients(sort_by : str = Query(..., description="Sort on the basis of height , weight or bmi "), order: str = Query("asc", description="Order of sorting: asc or desc")):
  
  valid_sort_by = ["height", "weight", "bmi"]
  
  if sort_by not in valid_sort_by:
      raise HTTPException(status_code=400, detail=f"Invalid sort_by value. Must be one of {valid_sort_by}")
  
  if order not in ["asc", "desc"]:
      raise HTTPException(status_code=400, detail="Invalid order value. Must be 'asc' or 'desc'")
  
  data = load_config()
  
  sort_reverse = True if order == "desc" else False
  
  sorted_patients = sorted(data.values(), key=lambda x: x[sort_by], reverse=sort_reverse)
  return sorted_patients
    
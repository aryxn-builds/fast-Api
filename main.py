from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json


app = FastAPI()

class Patient(BaseModel):

    id: Annotated[str, Field(..., description='ID of the patient', examples=['P001'])]
    name: Annotated[str, Field(..., description='Name of the patient')]
    city: Annotated[str, Field(..., description='City where the patient is living')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the patient')]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of the patient')]
    height: Annotated[float, Field(..., gt=0, description='Height of the patient in mtrs')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the patient in kgs')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Normal'
        else:
            return 'Obese'
        


class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['male', 'female']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]


def load_config():
    with open("patients.json") as config_file:
        config = json.load(config_file)
    return config


def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)

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
def view_patient(patient_id: str = Path(..., description="ID of the patient in the DB", examples=["P001"])):
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



# adding a new endpoint to add a new patient to the database. The endpoint will be /patients and will accept a POST request with the patient details in the request body. The endpoint will validate the input data and return a success message if the patient is added successfully, or an error message if there is any validation error.
@app.post("/create")
def create_patient(patient: Patient):
    
    # load all data of the patients
    data = load_config()
    
     # check if the patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient with this ID already exists")
    
    
    # new patient add to the database
    data[patient.id] = patient.model_dump(exclude=['id'])
    
    # save into the json file
    save_data(data)
    
    return JSONResponse(status_code=201, content={'message':'patient created successfully'})




@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    existing_patient_info = data[patient_id]

    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    #existing_patient_info -> pydantic object -> updated bmi + verdict
    existing_patient_info['id'] = patient_id
    patient_pydandic_obj = Patient(**existing_patient_info)
    #-> pydantic object -> dict
    existing_patient_info = patient_pydandic_obj.model_dump(exclude='id')

    # add this dict to data
    data[patient_id] = existing_patient_info

    # save data
    save_data(data)

    return JSONResponse(status_code=200, content={'message':'patient updated'})
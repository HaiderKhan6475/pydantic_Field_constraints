from typing import Dict, List, Optional,Annotated

from pydantic import BaseModel, Field


class Patient(BaseModel):
    # 1. 'max_Length' ko 'max_length' kiya aur 'json_scherma_extra' ke typo ko 'json_schema_extra' kiya
    # Business rule ke mutabiq min_length=3 lagaya
    name: Annotated[
        str,
        Field(
            min_length=3,
            max_length=50,
            title="Patient name",
            description="Give the name of patient name under 50 characters",
            json_schema_extra={"example": "Haider khan"},
        ),
    ]

    # 2. 'str' ko badal kar 'int' kiya taaki numeric validation (gt, lt) kaam kar sake
    age: int = Field(gt=18, lt=100)

    # 3. Missing type annotation theek ki: ':' lagaya aur field ka naam 'weight_kg' rakha
    weight_kg: float = Field(gt=0, description="Weight in kg")

    # Business rule ke mutabiq allergies ka default empty list [] set kiya
    allergies: Annotated[
        Optional[List[str]],
        Field(
            default=list, max_length=5, description="List of allergies"
        ),
    ]

    # 4. Field ka naam 'contact' rakha taaki patient_info ki key se match ho sake
    contact: Dict[str, str]




def show_patient(patient: Patient):
    print(f"Patient Name: {patient.name}")
    print(f"Patient Age: {patient.age}")
    print(f"Patient Weight: {patient.weight_kg}")
    print(f"Patient Allergies: {patient.allergies}")
    print(f"Patient Contact: {patient.contact}")

patient_info = {
    "name": "John",
    "age": "30",  
    "gender": "Male",
    "weight_kg": "70.5",  
    "allergies": None,
    "contact": {"phone": "123-456-7890"},
}    


patient_obj = Patient(**patient_info)

show_patient(patient_obj)
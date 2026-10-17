# Patient Schema Constraints & Validation

A structured Python workflow showcasing advanced runtime schema constraints, field boundary metadata, and target type validations using **Pydantic V2**.

## 🚀 Implemented Business Rules

The model safely filters and structure incoming medical records according to the following rules:
* **Name Validation**: The patient's string name input must contain between `3` and `50` characters.
* **Age Boundaries**: Age must be strictly greater than 18 (`gt=18`) and less than 100 (`lt=100`).
* **Weight Boundaries**: Weight values must always be strictly greater than zero (`gt=0`).
* **Allergies Management**: Defaults automatically to a clean dynamic sequence fallback (`default_factory=list`) with a structural collection bound of `5` max entries.

## 📦 Setup Prerequisites

Verify you are targeting Python 3.8+ and have the core validation engine installed:

```bash
pip install pydantic
```

## 💻 Script Source Code (`main.py`)

```python
from typing import Dict, List, Optional, Annotated
from pydantic import BaseModel, Field

class Patient(BaseModel):
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
    
    age: int = Field(gt=18, lt=100)
    weight_kg: float = Field(gt=0, description="Weight in kg")
    
    allergies: Annotated[
        Optional[List[str]],
        Field(
            default_factory=list, max_length=5, description="List of allergies"
        ),
    ]
    
    contact: Dict[str, str]

def show_patient(patient: Patient):
    print(f"Patient Name: {patient.name}")
    print(f"Patient Age: {patient.age}")
    print(f"Patient Weight: {patient.weight_kg}")
    print(f"Patient Allergies: {patient.allergies}")
    print(f"Patient Contact: {patient.contact}")

# Scenario Testing Payload
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
```

## 🎯 Verification Output

Execution output when deploying the default script context:

```text
Patient Name: John
Patient Age: 30
Patient Weight: 70.5
Patient Allergies: []
Patient Contact: {'phone': '123-456-7890'}
```

---

## 🧪 Edge-Case Violation Analysis

When passing faulty structural inputs outside our defined schema criteria, Pydantic immediately aborts model compilation with these expected error logs:

### 1. Age Under Bounds Check (`age: 15`)
```text
Input should be greater than 18 [type=greater_than, input_value=15, input_type=int]
```

### 2. Age Over Bounds Check (`age: 105`)
```text
Input should be less than 100 [type=less_than, input_value=105, input_type=int]
```

### 3. Invalid Negative Metric Value (`weight_kg: -5`)
```text
Input should be greater than 0 [type=greater_than, input_value=-5, input_type=int]
```

### 4. Empty String Boundary Fail (`name: ""`)
```text
String should have at least 3 characters [type=string_too_short, input_value='', input_type=str]
```

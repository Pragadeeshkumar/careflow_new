from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# USER SCHEMAS
class UserCreate(BaseModel):
    username: str
    password: str
    role: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    role: str
    
    class Config:
        from_attributes = True

# PATIENT SCHEMAS
class PatientCreate(BaseModel):
    full_name: str
    dob: str
    gender: str
    phone: str
    allergy_status: bool
    allergy_details: Optional[str] = None

class PatientResponse(PatientCreate):
    id: int
    
    class Config:
        from_attributes = True

# VISIT SCHEMAS
class VisitCreate(BaseModel):
    patient_id: int
    department: str
    visit_type: str

class VisitResponse(BaseModel):
    id: int
    patient_id: int
    department: str
    visit_type: str
    status: str
    registered_at: datetime
    
    class Config:
        from_attributes = True

# QUEUE SCHEMAS
class QueueStatusResponse(BaseModel):
    token_number: str
    department: str
    priority_band: int
    estimated_wait_time_minutes: int
    patients_ahead: int

# DRUG & PRESCRIPTION SCHEMAS
class DrugAutocomplete(BaseModel):
    id: int
    generic_name: str
    brand_name: str
    strength: str
    dosage_form: str

    class Config:
        from_attributes = True

class PrescriptionItemCreate(BaseModel):
    drug_id: int
    dose: str
    frequency: str
    duration: str

class PrescriptionCreate(BaseModel):
    visit_id: int
    doctor_id: int
    items: List[PrescriptionItemCreate]

class PrescriptionItemResponse(PrescriptionItemCreate):
    id: int
    prescription_id: int
    
    class Config:
        from_attributes = True

class PrescriptionResponse(BaseModel):
    id: int
    visit_id: int
    doctor_id: int
    status: str
    items: List[PrescriptionItemResponse] = []
    
    class Config:
        from_attributes = True

# LAB SCHEMAS
class LabRequestCreate(BaseModel):
    visit_id: int
    doctor_id: int
    test_name: str

class LabRequestResponse(BaseModel):
    id: int
    visit_id: int
    doctor_id: int
    test_name: str
    status: str
    result_report_url: Optional[str] = None
    
    class Config:
        from_attributes = True

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String) # Patient, Receptionist, Doctor, LabTech, Pharmacist, Admin

class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    dob = Column(String)
    gender = Column(String)
    phone = Column(String)
    allergy_status = Column(Boolean, default=False)
    allergy_details = Column(String, nullable=True)

class Visit(Base):
    __tablename__ = "visits"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    department = Column(String)
    visit_type = Column(String) # appointment, walk-in
    status = Column(String) # registered, queued, consultation, pharmacy, completed
    registered_at = Column(DateTime, default=datetime.datetime.utcnow)

class QueueEntry(Base):
    __tablename__ = "queue_entries"
    id = Column(Integer, primary_key=True, index=True)
    visit_id = Column(Integer, ForeignKey("visits.id"))
    token_number = Column(String, unique=True, index=True)
    priority_band = Column(Integer, default=1)
    status = Column(String) # waiting, called, completed

class DrugMaster(Base):
    __tablename__ = "drug_master"
    id = Column(Integer, primary_key=True, index=True)
    rxnorm_code = Column(String, index=True)
    generic_name = Column(String, index=True)
    brand_name = Column(String, index=True)
    strength = Column(String)
    dosage_form = Column(String)
    route = Column(String)
    interaction_group = Column(String)
    contraindications = Column(String)

class Prescription(Base):
    __tablename__ = "prescriptions"
    id = Column(Integer, primary_key=True, index=True)
    visit_id = Column(Integer, ForeignKey("visits.id"))
    doctor_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String) # pending_pharmacy, dispensed

class PrescriptionItem(Base):
    __tablename__ = "prescription_items"
    id = Column(Integer, primary_key=True, index=True)
    prescription_id = Column(Integer, ForeignKey("prescriptions.id"))
    drug_id = Column(Integer, ForeignKey("drug_master.id"))
    dose = Column(String)
    frequency = Column(String)
    duration = Column(String)

class LabRequest(Base):
    __tablename__ = "lab_requests"
    id = Column(Integer, primary_key=True, index=True)
    visit_id = Column(Integer, ForeignKey("visits.id"))
    doctor_id = Column(Integer, ForeignKey("users.id"))
    test_name = Column(String)
    status = Column(String) # requested, sample_collected, ready
    result_report_url = Column(String, nullable=True)


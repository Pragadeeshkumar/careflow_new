from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import get_db

router = APIRouter(prefix="/prescriptions", tags=["E-Prescription"])

@router.get("/autocomplete", response_model=List[schemas.DrugAutocomplete])
def autocomplete_drugs(query: str, db: Session = Depends(get_db)):
    """E-Prescription Module: Medicine Autocomplete"""
    drugs = db.query(models.DrugMaster).filter(
        models.DrugMaster.generic_name.ilike(f"%{query}%") | 
        models.DrugMaster.brand_name.ilike(f"%{query}%")
    ).limit(10).all()
    return drugs

@router.post("/", response_model=schemas.PrescriptionResponse)
def create_prescription(prescription: schemas.PrescriptionCreate, db: Session = Depends(get_db)):
    """E-Prescription Module: Structured Entry & Safety Checks"""
    visit = db.query(models.Visit).filter(models.Visit.id == prescription.visit_id).first()
    if not visit:
        raise HTTPException(status_code=404, detail="Visit not found")
        
    patient = db.query(models.Patient).filter(models.Patient.id == visit.patient_id).first()
    
    # Safety Validation Layer
    for item in prescription.items:
        drug = db.query(models.DrugMaster).filter(models.DrugMaster.id == item.drug_id).first()
        if patient.allergy_status and patient.allergy_details and drug.interaction_group.lower() in patient.allergy_details.lower():
            raise HTTPException(status_code=400, detail=f"Safety Alert: Patient is allergic to {drug.generic_name} ({drug.interaction_group})")

    new_rx = models.Prescription(visit_id=prescription.visit_id, doctor_id=prescription.doctor_id, status="pending_pharmacy")
    db.add(new_rx)
    db.commit()
    db.refresh(new_rx)

    # Automatically update visit status
    visit.status = "pharmacy"

    rx_items_response = []
    for item in prescription.items:
        rx_item = models.PrescriptionItem(
            prescription_id=new_rx.id,
            drug_id=item.drug_id,
            dose=item.dose,
            frequency=item.frequency,
            duration=item.duration
        )
        db.add(rx_item)
        db.commit()
        db.refresh(rx_item)
        
        # Convert to dictionary for Pydantic
        item_dict = {
            "id": rx_item.id,
            "prescription_id": rx_item.prescription_id,
            "drug_id": rx_item.drug_id,
            "dose": rx_item.dose,
            "frequency": rx_item.frequency,
            "duration": rx_item.duration
        }
        rx_items_response.append(item_dict)

    return {
        "id": new_rx.id,
        "visit_id": new_rx.visit_id,
        "doctor_id": new_rx.doctor_id,
        "status": new_rx.status,
        "items": rx_items_response
    }

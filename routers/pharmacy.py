from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import get_db

router = APIRouter(prefix="/pharmacy", tags=["Pharmacy"])

@router.get("/queue")
def get_pharmacy_queue(db: Session = Depends(get_db)):
    prescriptions = db.query(models.Prescription).filter(models.Prescription.status == "pending_pharmacy").all()
    results = []
    for rx in prescriptions:
        visit = db.query(models.Visit).filter(models.Visit.id == rx.visit_id).first()
        patient = db.query(models.Patient).filter(models.Patient.id == visit.patient_id).first()
        items = db.query(models.PrescriptionItem).filter(models.PrescriptionItem.prescription_id == rx.id).all()
        
        rx_items = []
        for item in items:
            drug = db.query(models.DrugMaster).filter(models.DrugMaster.id == item.drug_id).first()
            rx_items.append({
                "drug_name": f"{drug.brand_name} ({drug.generic_name})",
                "dose": item.dose,
                "frequency": item.frequency,
                "duration": item.duration
            })
            
        results.append({
            "prescription_id": rx.id,
            "patient_name": patient.full_name,
            "visit_department": visit.department,
            "items": rx_items
        })
    return results

@router.put("/dispense/{prescription_id}")
def dispense_prescription(prescription_id: int, db: Session = Depends(get_db)):
    rx = db.query(models.Prescription).filter(models.Prescription.id == prescription_id).first()
    if not rx:
        raise HTTPException(status_code=404, detail="Prescription not found")
        
    rx.status = "dispensed"
    
    visit = db.query(models.Visit).filter(models.Visit.id == rx.visit_id).first()
    visit.status = "completed"
    
    db.commit()
    return {"message": "Prescription dispensed and visit completed"}

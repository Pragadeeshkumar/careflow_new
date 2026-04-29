from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import get_db

router = APIRouter(prefix="/visits", tags=["Visits"])

@router.post("/", response_model=schemas.VisitResponse)
def create_visit(visit: schemas.VisitCreate, db: Session = Depends(get_db)):
    patient = db.query(models.Patient).filter(models.Patient.id == visit.patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
        
    new_visit = models.Visit(
        patient_id=visit.patient_id,
        department=visit.department,
        visit_type=visit.visit_type,
        status="registered"
    )
    db.add(new_visit)
    db.commit()
    db.refresh(new_visit)
    return new_visit

@router.get("/", response_model=List[schemas.VisitResponse])
def get_visits(status: str = None, department: str = None, db: Session = Depends(get_db)):
    query = db.query(models.Visit)
    if status:
        query = query.filter(models.Visit.status == status)
    if department:
        query = query.filter(models.Visit.department == department)
    return query.all()

@router.put("/{visit_id}/status", response_model=schemas.VisitResponse)
def update_visit_status(visit_id: int, status: str, db: Session = Depends(get_db)):
    visit = db.query(models.Visit).filter(models.Visit.id == visit_id).first()
    if not visit:
        raise HTTPException(status_code=404, detail="Visit not found")
    visit.status = status
    db.commit()
    db.refresh(visit)
    return visit

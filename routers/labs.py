from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import get_db

router = APIRouter(prefix="/labs", tags=["Lab Technician"])

@router.post("/request", response_model=schemas.LabRequestResponse)
def request_lab(req: schemas.LabRequestCreate, db: Session = Depends(get_db)):
    visit = db.query(models.Visit).filter(models.Visit.id == req.visit_id).first()
    if not visit:
        raise HTTPException(status_code=404, detail="Visit not found")
        
    visit.status = "lab"
    
    new_req = models.LabRequest(
        visit_id=req.visit_id,
        doctor_id=req.doctor_id,
        test_name=req.test_name,
        status="requested"
    )
    db.add(new_req)
    db.commit()
    db.refresh(new_req)
    return new_req

@router.get("/queue", response_model=List[schemas.LabRequestResponse])
def get_lab_queue(db: Session = Depends(get_db)):
    return db.query(models.LabRequest).filter(models.LabRequest.status != "ready").all()

@router.put("/{request_id}/status", response_model=schemas.LabRequestResponse)
def update_lab_status(request_id: int, status: str, result_url: str = None, db: Session = Depends(get_db)):
    req = db.query(models.LabRequest).filter(models.LabRequest.id == request_id).first()
    if not req:
        raise HTTPException(status_code=404, detail="Lab request not found")
        
    req.status = status
    if result_url:
        req.result_report_url = result_url
        
    db.commit()
    db.refresh(req)
    return req

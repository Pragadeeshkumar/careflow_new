from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import get_db
import pickle
import random

router = APIRouter(prefix="/queue", tags=["Queue Management"])

# Load AI model
try:
    with open("wait_time_model.pkl", "rb") as f:
        wait_time_model = pickle.load(f)
except Exception:
    wait_time_model = None

@router.post("/checkin", response_model=schemas.QueueStatusResponse)
def check_in_patient(visit_id: int, priority_band: int = 1, db: Session = Depends(get_db)):
    """AI Queue Management: Generate Token & Wait Time"""
    visit = db.query(models.Visit).filter(models.Visit.id == visit_id).first()
    if not visit:
        raise HTTPException(status_code=404, detail="Visit not found")

    # Update visit status
    visit.status = "queued"

    # Get Queue Length for department
    queue_len = db.query(models.QueueEntry).join(models.Visit).filter(
        models.QueueEntry.status == "waiting",
        models.Visit.department == visit.department
    ).count()
    
    # Predict Wait Time
    if wait_time_model:
        try:
            features = [[queue_len, priority_band, 1]]
            wait_time = int(wait_time_model.predict(features)[0])
        except:
            wait_time = queue_len * 15 # Fallback
    else:
        wait_time = queue_len * 15 # 15 mins per patient fallback

    # Generate Token
    token = f"{visit.department[:3].upper()}-{random.randint(100, 999)}"
    
    entry = models.QueueEntry(visit_id=visit.id, token_number=token, priority_band=priority_band, status="waiting")
    db.add(entry)
    db.commit()
    
    return {
        "token_number": token,
        "department": visit.department,
        "priority_band": priority_band,
        "estimated_wait_time_minutes": wait_time,
        "patients_ahead": queue_len
    }

@router.get("/department/{department}")
def get_department_queue(department: str, db: Session = Depends(get_db)):
    entries = db.query(models.QueueEntry).join(models.Visit).filter(
        models.QueueEntry.status == "waiting",
        models.Visit.department == department
    ).order_by(models.QueueEntry.priority_band.desc(), models.QueueEntry.id.asc()).all()
    
    results = []
    for idx, e in enumerate(entries):
        results.append({
            "token_number": e.token_number,
            "priority_band": e.priority_band,
            "estimated_wait_time_minutes": (idx) * 15,
            "visit_id": e.visit_id
        })
    return results

@router.put("/call/{token_number}")
def call_patient(token_number: str, db: Session = Depends(get_db)):
    entry = db.query(models.QueueEntry).filter(models.QueueEntry.token_number == token_number).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Queue entry not found")
    
    entry.status = "called"
    visit = db.query(models.Visit).filter(models.Visit.id == entry.visit_id).first()
    visit.status = "consultation"
    
    db.commit()
    return {"message": f"Patient with token {token_number} called successfully"}

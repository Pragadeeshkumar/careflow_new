from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models
from database import get_db

router = APIRouter(prefix="/admin", tags=["Admin Analytics"])

@router.get("/dashboard")
def get_admin_dashboard(db: Session = Depends(get_db)):
    total_patients = db.query(models.Patient).count()
    total_visits_today = db.query(models.Visit).count() # Simplify for MVP
    
    department_stats = {}
    visits = db.query(models.Visit).all()
    for v in visits:
        department_stats[v.department] = department_stats.get(v.department, 0) + 1
        
    queue_lengths = {}
    queues = db.query(models.QueueEntry).join(models.Visit).filter(models.QueueEntry.status == "waiting").all()
    for q in queues:
        visit = db.query(models.Visit).filter(models.Visit.id == q.visit_id).first()
        queue_lengths[visit.department] = queue_lengths.get(visit.department, 0) + 1
        
    return {
        "total_patients": total_patients,
        "total_visits": total_visits_today,
        "department_distribution": department_stats,
        "live_queue_lengths": queue_lengths
    }

import database
import models
from sqlalchemy.orm import Session
import datetime

def seed():
    models.Base.metadata.create_all(bind=database.engine)
    db = database.SessionLocal()
    
    # Check if already seeded
    if db.query(models.DrugMaster).first():
        print("Database already seeded.")
        return

    # Seed Drugs
    drugs = [
        models.DrugMaster(rxnorm_code="1191", generic_name="Aspirin", brand_name="Bayer", strength="81mg", dosage_form="Tablet", route="Oral", interaction_group="NSAID", contraindications="Bleeding disorder"),
        models.DrugMaster(rxnorm_code="723", generic_name="Amoxicillin", brand_name="Amoxil", strength="500mg", dosage_form="Capsule", route="Oral", interaction_group="Penicillin", contraindications="Penicillin Allergy"),
        models.DrugMaster(rxnorm_code="161", generic_name="Acetaminophen", brand_name="Tylenol", strength="500mg", dosage_form="Tablet", route="Oral", interaction_group="Analgesic", contraindications="Liver disease"),
        models.DrugMaster(rxnorm_code="6809", generic_name="Metformin", brand_name="Glucophage", strength="1000mg", dosage_form="Tablet", route="Oral", interaction_group="Biguanide", contraindications="Renal failure")
    ]
    db.add_all(drugs)
    
    # Seed Patient
    patient = models.Patient(
        full_name="John Doe", 
        dob="1980-01-01", 
        gender="Male", 
        phone="555-1234", 
        allergy_status=True, 
        allergy_details="Penicillin"
    )
    db.add(patient)
    db.commit()

    # Seed Visit
    visit = models.Visit(
        patient_id=patient.id,
        department="Cardiology",
        visit_type="walk-in",
        status="registered",
        registered_at=datetime.datetime.utcnow()
    )
    db.add(visit)
    db.commit()

    # Seed Doctor
    doctor = models.User(username="drsmith", hashed_password="hashed_pwd", role="Doctor")
    db.add(doctor)
    db.commit()

    print("Database seeded successfully with test data!")
    db.close()

if __name__ == "__main__":
    seed()

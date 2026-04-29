from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models, database
from routers import auth, patients, visits, queue, prescriptions, labs, pharmacy, admin

# Create tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Hospital Workflow AI Backend", description="Multi-role Hospital System")

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(auth.router)
app.include_router(patients.router)
app.include_router(visits.router)
app.include_router(queue.router)
app.include_router(prescriptions.router)
app.include_router(labs.router)
app.include_router(pharmacy.router)
app.include_router(admin.router)

@app.get("/")
def root():
    return {"message": "Hospital Workflow System API is running."}

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(title="SENTINEX Backend API")

class AssessRequest(BaseModel):
    observations: List[Dict]
    settings: Dict

class AssessResponse(BaseModel):
    state: str
    action: str
    reason: str
    consent_required: bool
    model_version: str

@app.get("/health")
def health_check():
    return {"status": "healthy", "architecture": "s390x LinuxONE"}

@app.get("/api/v1/config")
def get_config():
    return {"thresholds": {"normal": 0.3, "elevated": 0.7}, "cooldown_seconds": 60}

@app.post("/api/v1/assess", response_model=AssessResponse)
def assess_risk(request: AssessRequest):
    if not request.observations:
        return AssessResponse(
            state="INSUFFICIENT_DATA",
            action="request_more_data",
            reason="No observations provided.",
            consent_required=False,
            model_version="v0.1.0-baseline"
        )
    
    return AssessResponse(
        state="NORMAL_MONITORING",
        action="keep_watching",
        reason="Data valid. Awaiting model integration.",
        consent_required=False,
        model_version="v0.1.0-baseline"
    )

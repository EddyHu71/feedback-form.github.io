from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Data model for feedback
class Feedback(BaseModel):
    service_rating: int
    quality_rating: int
    value_rating: int
    comments: Optional[str] = None

# In-memory storage for feedback (for demonstration purposes)
feedback_storage: List[Feedback] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the Feedback API"}

@app.post("/feedback")
def create_feedback(feedback: Feedback):
    feedback_storage.append(feedback)
    return {"message": "Feedback submitted successfully"}
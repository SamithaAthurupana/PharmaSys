from fastapi import APIRouter
from models.dashboard_model import get_dashboard_stats

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("/stats")
def dashboard_statistics():
    return get_dashboard_stats()

from fastapi import APIRouter
from app.schemas.health import HealthResponse

router = APIRouter()

@router.get("/", response_model=HealthResponse)
async def root():
    """
    Health check endpoint
    """
    return HealthResponse(
        status="healthy", 
        message="TODO List API is running"
    )

@router.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint
    """
    return HealthResponse(
        status="healthy", 
        message="TODO List API is operational"
    )



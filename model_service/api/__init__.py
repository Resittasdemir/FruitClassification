from fastapi import APIRouter
from .controllers.model_controller import model_router

router = APIRouter()

router.include_router(model_router, tags=["REŞİT TAŞDEMİR - CNN"])

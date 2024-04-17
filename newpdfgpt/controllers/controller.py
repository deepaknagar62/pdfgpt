
from fastapi import APIRouter
from routers import upload, chat, category

router = APIRouter()

router.include_router(upload.router, prefix="/api")
router.include_router(chat.router, prefix="/api")
router.include_router(category.router, prefix="/api")
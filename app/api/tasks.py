from fastapi import APIRouter, Depends

from app.core.celery_app import celery_app
from app.models.msg import Msg
from app.models.user import UserInDB

router = APIRouter()


@router.post("/test-celery/", response_model=Msg, status_code=201)
def test_celery(msg: Msg, current_user: UserInDB = Depends(get_current_active_superuser)):
    """
    Test Celery worker.
    """
    celery_app.send_task("app.worker.test_celery", args=[msg.msg])
    return {"msg": "Word received"}



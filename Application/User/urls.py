from fastapi import APIRouter

user_router = APIRouter(prefix='/users')


@user_router.get("/")
async def root():
    return {'users', 'users'}

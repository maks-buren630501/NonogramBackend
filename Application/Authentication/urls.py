from fastapi import APIRouter

authentication_router = APIRouter(prefix='/authentication')


@authentication_router.get("/")
async def root():
    return {'authentication', 'authentication'}

from fastapi import APIRouter,Depends
from src.core.deps import get_db
from src.dish.repository import DishRepository
from src.dish.service import DishService
from src.dish.schemas import DishCreate,DishResponse

router = APIRouter(
    prefix="/dishes",
    tags=["Dishes"]
)

async def get_dish_service(session = Depends(get_db) ):
    repository = DishRepository(session)
    return DishService(repository)
   

@router.post(
    "/",
    response_model=DishResponse,
    status_code=201,
)
async def create_dish(
    dish_data:DishCreate,
    service:DishService = Depends(get_dish_service)
):
    new_dish = await service.create_dish(dish_data)
    return new_dish
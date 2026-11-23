from src.dish.repository import DishRepository
from src.dish.schemas import DishCreate,DishResponse

class DishService:
    """菜品业务逻辑服务。

    该类负责协调菜品仓储对象，并执行菜品相关的业务操作。

    Attributes:
        repository: 用于访问菜品数据库数据的仓储对象。
    """

    def __init__(self, repository:DishRepository):
        self.repository = repository

    async def create_dish(self,dish_data:DishCreate) -> DishResponse:
        data = dish_data.model_dump()
        dish = await self.repository.create(data)
    
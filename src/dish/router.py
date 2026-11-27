# ===== 00 导入功能模块 =====
# APIRouter：FastAPI 提供的路由类；Depends：声明依赖，让框架调用指定函数并提供结果。
from fastapi import APIRouter,Depends
# get_db：deps.py 中提供 AsyncSession 数据库会话实例的函数。
from src.core.deps import get_db
# DishRepository：仓库类，负责操作数据库。
from src.dish.repository import DishRepository
# DishService：服务类，负责处理菜品业务。
from src.dish.service import DishService
# DishCreate：请求数据校验模型；DishResponse：响应数据模型。
from src.dish.schemas import DishCreate,DishResponse

# ===== 01 创建路由对象：统一管理菜品接口 =====
# 实例化 APIRouter，用 router 接收路由实例，后续通过它注册菜品接口。
# prefix 统一接口路径前缀；tags 用于 Swagger 接口分组。
router = APIRouter(
    prefix="/dishes",
    tags=["Dishes"]
)

# ===== 02 定义依赖函数：准备处理菜品业务所需的对象 =====
# 仓库需要操作数据库，因此通过 Depends 让 FastAPI 调用 deps.py 中的 get_db，
# 获取具备查询、添加数据和提交事务等能力的 AsyncSession 实例，由 session 接收。
# get_dish_service 是自定义协程函数，在处理请求时由 FastAPI 调用。
async def get_dish_service(session = Depends(get_db) ):
    # 创建仓库实例，传入数据库会话，使仓库具备操作数据库的条件。
    repository = DishRepository(session)
    # 创建服务实例，传入仓库实例，使服务层能够通过仓库操作数据库。
    # 返回服务实例，供第 04 步的请求处理函数使用。
    return DishService(repository)
   

# ===== 03 注册接口：建立客户请求与处理函数的对应关系 =====
# 程序启动时，通过 router.post() 将下方函数注册为 POST /dishes/ 接口。
# response_model 指定返回的数据格式；status_code 指定成功响应状态码。
@router.post(
    "/",
    response_model=DishResponse,
    status_code=201,
)
# ===== 04 定义请求处理函数：接收数据、调用服务、返回结果 =====
async def create_dish(
    # 客户提交菜品数据后，FastAPI 按 schemas.py 中的 Pydantic 模型 DishCreate
    # 校验数据，创建 DishCreate 实例，由 dish_data 接收。
    dish_data:DishCreate,
    # 第 02 步定义了 get_dish_service 函数，专门创建并返回 DishService 实例。
    # 收到请求时，Depends 让 FastAPI 调用该函数，service 接收返回的实例。
    # DishService 类型注解声明 service 预期接收的对象类型。
    service:DishService = Depends(get_dish_service)
):
    # 菜品数据和服务实例准备好后，调用 service.py 中的异步 create_dish 方法，
    # 将菜品数据传入，等待业务完成，由 new_dish 接收返回的 DishResponse 实例。
    new_dish = await service.create_dish(dish_data)
    # 将结果交给 FastAPI，按响应模型生成 JSON，成功时返回 201 状态码。
    return new_dish
# Annotated：给Python类型补充校验规则
# Literal：Python提供的类型标注工具，限制字段只能使用指定值
from typing import Annotated,Literal

# BaseModel：Pydantic提供的模型基类，用于数据校验
# Field：设置字段的默认值、限制和说明
from pydantic import BaseModel, Field

# datetime：表示日期和时间的数据类型
from datetime import datetime

# 定义菜品的公共数据字段
class DishBase(BaseModel):

    # 菜品必须是字符串
    # str：菜品名称必须是字符串
    # ...：必填字段
    # max_length：最多255个字符
    name: Annotated[
        str,
        Field(..., max_length=255, description="菜品名称")
    ]

    # str | None：允许字符串或者None
    # Field(None)：默认值为None
    description: Annotated[
    str | None,
    Field(None, description="菜品描述")
]

# 修改菜品时使用的请求模型
class DishUpdate(BaseModel):

    # str | None：允许字符串或 None
    # Field(None)：字段可省略，默认值为 None
    # max_length=255：菜品名称最多255个字符 
    name: Annotated[
    str | None,
    Field(None, max_length=255, description="菜品名称")
    ]

    # 描述同样可以单独修改
    description: Annotated[
        str | None,
        Field(None, description="菜品描述")
    ]

# 创建菜品时使用的模型
class DishCreate(DishBase):
    """用于创建菜品"""

# 定义菜品返回给前端的数据结构
class DishResponse(DishBase):

# 数据库生成的菜品ID
    id:int
# 数据库生成的创建时间
    created_at: datetime

# from_attributes=True：
    # 允许Pydantic从SQLAlchemy ORM对象的属性中读取字段
    model_config ={"from_attributes":True}

# 定义菜品列表的查询参数模型
class DishQureyParams(BaseModel):

    # search：我们定义的字段名
    # str | None：搜索词允许为空
    # = None：用户没有提供时，默认不指定搜索词
    search:Annotated[
        str| None,
        Field(description="搜索关键词")
    ]= None

    # Literal：Python提供的类型标注工具
    # 用户只能从 id、name、created_at 中选择排序字段
    # = "id"：默认按菜品ID排序
    order_by:Annotated[
        Literal["id","name","created_at"],
        Field(description="排序字段")
    ]="id"

    # asc：升序，desc：降序
    # 默认升序
    direction = Annotated[
        Literal["asc","desc"],
        Field(description="排序方向")
    ] ="asc"

    # limit：最多返回多少条数据
    # ge=1：最小值为1
    # le=500：最大值为500
    # = 10：默认返回10条
    limit:Annotated[
        int,
        Field(ge=1,le=500,description="每次反回的条数")
    ]=10

    # offset：跳过前面多少条记录
    # ge=0：最小值为0
    # = 0：默认从第一条开始
    offset:Annotated[
        int,
        Field(ge= 0,description = "查询其实偏移量")
    ]= 0
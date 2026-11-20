# Annotated：给Python类型补充校验规则
from typing import Annotated

# BaseModel：Pydantic提供的模型基类，用于数据校验
# Field：设置字段的默认值、限制和说明
from pydantic import BaseModel, Field

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
    description:Annotated[
        str | None,
        Field(None, max_length=255)
    ]

class DishCreate(DishBase):
    """用于创建菜品"""


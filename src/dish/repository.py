# Mapping：Python 提供的映射类型接口，用于标注字典一类的数据
from collections.abc import Mapping

# Any：Python 提供的类型标注，表示值可以是任意类型
from typing import Any

# IntegrityError：SQLAlchemy 的数据库完整性约束异常
from sqlalchemy.exc import IntegrityError

# AsyncSession：SQLAlchemy 提供的异步数据库会话类
from sqlalchemy.ext.asyncio import AsyncSession

# Dish：我们在 models.py 中自己定义的 ORM 模型类
from src.dish.models import Dish


# 菜品数据库操作类
class DishRepository:

    # __init__：Python 特殊方法，创建实例时自动执行
    # session：外部传入的数据库会话
    def __init__(self, session: AsyncSession):
        self.session = session

    # create：我们自己定义的新增菜品方法
    # dish_data：传入菜品数据，字段名为字符串，值允许多种类型
    # -> Dish：返回 Dish ORM 对象
    async def create(self, dish_data: Mapping[str, Any]) -> Dish:

        # **dish_data：将字典拆成关键字参数
        # 创建一个 Dish ORM 对象
        dish = Dish(**dish_data)

        # add()：把对象加入当前 Session，等待提交
        self.session.add(dish)

        try:
            # commit()：提交数据库事务，真正保存数据
            await self.session.commit()

        except IntegrityError:
            # rollback()：提交失败时回滚事务
            await self.session.rollback()
            raise

        # refresh()：重新读取保存后的记录，包括数据库生成的ID等
        await self.session.refresh(dish)

        # 把保存成功的 Dish 对象返回给调用者
        return dish


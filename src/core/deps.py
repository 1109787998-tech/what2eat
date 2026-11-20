from sqlalchemy.ext.asyncio import AsyncSession
from src.core.db import SessionLocal

# ③ 定义数据库依赖函数
async def get_db():
    # ④ 调用工厂，创建一个Session
    async with SessionLocal() as session:
        # ⑤ yield把Session提供给fatsapi调用者,完成后退出退出 async with 然后关闭session
        yield session
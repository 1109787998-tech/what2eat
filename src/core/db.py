#1.1 导入sqlalchemy异步引擎创建函数,和异步工厂
from sqlalchemy.ext.asyncio import (create_async_engine,async_sessionmaker)
#1.2 导入之前创建对象
from src.core.config import settings
import asyncio 
from sqlalchemy import text

#1.3 创建数据库引擎
engine = create_async_engine(
    settings.database_url,
    **settings.engine_options
)

#3.1 创建异步Sesssion工厂
SessionLocal = async_sessionmaker(       #创建Session工厂对象，并接收返回的Session工厂对象
    bind = engine,                            # 把这个工厂与之前的数据库引擎关联
    expire_on_commit=False                  # 提交事务之后，保留已加载对象属性的值。
)


#2.1 定义异步数据库连接测试函数
async def test_connection():
    #2.2 获取数据库连接
    async with engine.connect()as conn:
        #2.3 执行查询语句
        result = await conn.execute(text("SELECT 1"))
        #2.4 获取查询结果
        print(result.scalar())

    #2.5 释放引擎管理的连接资源
    await engine.dispose()

async def test_session():
    #4.1 创建数据库会话
    async with SessionLocal()as session:
        #4.2 通过Sesssion执行sql
        result = await session.execute(text("SELECT 1"))
        #4.3 查询结果
        value = result.scalar_one()
        print   ("Session查询结果:",value)
    await engine.dispose()

#检查创建的对象类型
print(type(SessionLocal).__name__)

if __name__ =="__main__":
     asyncio.run(test_session())
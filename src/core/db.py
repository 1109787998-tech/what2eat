# 1.导入创建数据库引擎、Session工厂的工具
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
# 2.从config.py获取配置对象
from src.core.config import Settings

settings = Settings()

# 3.创建数据库引擎
# 它接收数据库 URL 和连接池参数，创建一个 Engine 对象。
# Engine 负责管理数据库连接，包括连接池和连接的获取、复用。
engine = create_async_engine(
    settings.database_url,
    **settings.engine_options
)

# 4. 创建 Session 工厂
# 它接收已经创建好的 Engine，生成一个 Session 工厂对象。
# 以后业务代码调用 SessionLocal()，工厂就会创建一个 AsyncSession，让程序能够执行 SQL、管理事务。
SessionLocal = async_sessionmaker(
    bind = engine,  # 绑定到引擎
    expire_on_commit=False # 提交后不自动过期
)










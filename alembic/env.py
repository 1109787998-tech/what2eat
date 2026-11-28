import asyncio
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config

from alembic import context

# 新增_一阶段 获取数据库配置类
from src.core.config import Settings

# 新增_一阶段 orm公共的基类
from src.core.base_model import Base

# 新增_一阶段 导入 Dish 模型，让它注册到 Base.metadata
from src.dish.models import Dish

# 新增_二阶段 导入用户模型和访问令牌模型，使其表结构登记到 Base.metadata
from src.auth.model import User, AccessToken

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# 新增_一阶段  创建配置实例
settings = Settings()   #创建配置对象，读取 .env 中的数据库参数。

'''新增 将 PostgreSQL 连接地址交给 Alembic
# set_main_option()：设置 Alembic 主配置中的指定参数
# 参数1 name：配置项名称，"sqlalchemy.url" 表示数据库连接地址
# 参数2 value：配置项的值，从 settings.database_url 获取
# replace()：将 % 转义为 %%，适配 Alembic 的配置解析
# 作用：让 Alembic 获得 PostgreSQL 连接地址
'''
config.set_main_option(      
    "sqlalchemy.url",         
    settings.database_url.replace("%", "%%")
)


# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata


# 新增_一阶段 讲元数据交给目标元数据
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    """In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""

    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

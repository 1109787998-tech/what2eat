from datetime import datetime
from sqlalchemy import DateTime, MetaData,func
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column


#定位命名规则
#左边的 pk、uq、ck、fk、ix 表示要命名哪类数据库对象，右边的占位符决定这个对象最终叫什么名字
database_naming_convention ={
    "ix": "%(column_0_label)s_idx", #索引命名规则
    "uq": "%(table_name)s_%(column_0_name)s_key", #唯一约束命名规则
    "ck": "%(table_name)s_%(constraint_name)s_check", #检查约束命名规则
    "fk": "%(table_name)s_%(column_0_name)s_fkey",  #外键命名规则
    "pk":"%(table_name)s_pkey" #主键命名规则
}


class Base(DeclarativeBase): #是 DeclartiveBase SQLAlchemy 的声明式基类，让继承它的类可以定义成数据库模型表。
    
    metadata = MetaData(                # MetaDate是 SQLAlchemy 提供的类 metadata是已有属性
    naming_convention = database_naming_convention
    )


    cread_time:Mapped[datetime] = mapped_column(
        DateTime,
        server_default = func.now(),
        comment="创建时间",
    )

    updated_at:Mapped[datetime] = mapped_column(
        DateTime,
        server_default = func.now(),
        onupdate=func.now()
        comment="修改时间",
    )

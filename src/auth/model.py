#00 导入功能模块
# fastapi Users 提供的用户基础模型类,第三方库已经帮我们提前定义好了大部分用户字段，我们只需要通过继承获取这些字段
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
# 导入自己定义的数据库模型基类和时间字段类
from src.core.base_model import Base,DateTimeMixin

##01 定义用户扩展字段,客户设置自己的用户名
#第三方库提供了用户基础字段，我们现在需要自行扩展一个 name 字段，用于存储用户名
from sqlalchemy import String
from sqlalchemy.orm import Mapped,mapped_column

##03 第三方库提供的访问令牌基础模型类
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyBaseAccessTokenTableUUID

##02 定义 User 类
class User(SQLAlchemyBaseUserTableUUID,DateTimeMixin,Base):
    name:Mapped[str] = mapped_column(
        String(64),
        nullable=True,
    )

##03 定定义访问令牌数据库模型
# 继承令牌基础字段和数据库映射能力
# 客户输入邮箱和密码登录成功后，系统会发放一个 Token（访问令牌）访问接口时系统可以通过这个令牌识别他的身份
# alembic/env.py加新模型的导入，然后生成并执行迁移文件
class AccessToken(SQLAlchemyBaseAccessTokenTableUUID,Base):
    pass 


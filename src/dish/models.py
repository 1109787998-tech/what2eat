from sqlalchemy import Integer,String,Text
from src.core.base_model import Base
from sqlalchemy.orm import Mapped, mapped_column
from src.core.base_model import DateTimeMixin


class Dish(Base,DateTimeMixin):
    """菜品数据库模型，对应dishes表。

    Attributes:
        id: 菜品唯一标识，由数据库自动递增生成。
        name: 菜品名称，最长255个字符且不可重复。
        description: 菜品描述，可为空。
        created_at: 菜品创建时间，由数据库服务端生成。
        updated_at: 菜品更新时间，由数据库服务端自动维护。
    """

    __tablename__ = "dishes"


    id : Mapped[int] = mapped_column(
        Integer,
        primary_key=True, 
        autoincrement=True,
        comment="菜品id",
    )

    name : Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        comment="菜品名称"
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        comment="菜品名称"
    )
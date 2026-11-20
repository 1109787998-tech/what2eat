from sqlalchemy import Integer,String,Text
from src.core.base_model import Base
from sqlalchemy.orm import Mapped, mapped_column


class dish(Base):
    __tablename__ = "dish"


    id : Mapped[int] = mapped_column(
        Integer,
        primary_key=True, 
        autoincrement=True,
        comment="书籍id"
    )

    name : Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        comment="菜品名称"
    )

    description: Mapped[str] = mapped_column(
        Text(255),
        unique=True,
        comment="菜品名称"
    )
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,func


class Base(DeclarativeBase):
    cread_time:Mapped[datetime] = mapped_column(
        DateTime,
        server_default = func.now(),
        comment="创建时间",
    )

    cread_time:Mapped[datetime] = mapped_column(
        DateTime,
        server_default = func.now(),
        comment="修改时间",
    )

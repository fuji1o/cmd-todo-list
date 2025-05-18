from sqlalchemy import Boolean, Column, Integer, String

from App.database import Base


class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=False)
    is_done = Column(Boolean, default=False)

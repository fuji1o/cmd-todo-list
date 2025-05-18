from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///cmd_todo_list.db"
engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()

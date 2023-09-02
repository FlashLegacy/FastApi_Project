from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session

from config import DB_URL



engine = create_engine(DB_URL)

async_session_maker = sessionmaker(engine, class_= Session, expire_on_commit= False)

class Base(DeclarativeBase):
    pass
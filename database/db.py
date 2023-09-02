from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config import DB_URL


engine = create_async_engine(DB_URL)
sessionLocal = sessionmaker(bind= engine, class_= AsyncSession, expire_on_commit= False)

class Base(declarative_base):
    pass


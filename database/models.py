from sqlalchemy import String, Integer, JSON, Date, Float, ForeignKey, MetaData, Table, Column, Computed
from datetime import date

from db import Base

class Hotels(Base):
    __tablename__ = "hotels"

    id              = Column(Integer,   primary_key     = True)
    name            = Column(String,    nullable        = False)
    location        = Column(String,    nullable        = False)
    services        = Column(JSON)
    rooms_quantity  = Column(Integer,   nullable        = False)
    image_id        = Column(Integer)

class Users(Base):
    __tablename__ = "users"

    id              = Column(Integer,   primary_key     = True)
    email           = Column(String,    nullable        = False)
    hashed_password = Column(String,    nullable        = False)

class Rooms(Base):
    __tablename__ = "rooms"

    id              = Column(Integer,   primary_key     = True)
    hotel_id        = Column(Integer,   nullable        = False)
    name            = Column(String,    nullable        = False)
    description     = Column(String)
    price           = Column(Float,     nullable        = False)
    services        = Column(JSON)
    quantity        = Column(Integer,   nullable        = False)
    image_id        = Column(Integer)

class Booking(Base):
    __tablename__ = "booking"

    id              = Column(Integer,   primary_key     = True)
    room_id         = Column(ForeignKey("rooms.id"))
    user_id         = Column(ForeignKey("users.id"))
    date_from       = Column(Date,      nullable        = False)
    date_to         = Column(Date,      nullable        = False)
    price           = Column(Float,     nullable        = False)
    total_cost      = Column(Float,     Computed("(date_to - date_from) * price"))
    total_days      = Column(Integer,   Computed("(date_to - date_from)"))